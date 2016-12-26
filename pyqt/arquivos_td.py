import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog
from TDGui import Ui_JanelaPrincipal
from remote_bid_td import atualizar_remote_bid
import time

class GerenciadorDeJanelas(QMainWindow):
	
	def __init__(self):
		super().__init__()

		self.janelaPrincipal = Ui_JanelaPrincipal()
		self.janelaPrincipal.setupUi(self)
		self.textoLog = ""


		self.janelaPrincipal.caminhoDB.setText(r'''Z:\AUTO HONDA\TESTDRIVE\EXPORTACAO\TD_Data_V2015.mdb''')
		self.janelaPrincipal.raizArquivosTD.setText(r"Y:\AUTO TEST DRIVE\2016\12_DEZEMBRO")
		self.janelaPrincipal.caminhoTemp.setText(".\\arquivo_td_temp.txt")
		self.janelaPrincipal.campoPrefixoLotes.setText("C")
		self.janelaPrincipal.campoTabela.setText("AUTO_TD_NOVO_FORM")
		self.janelaPrincipal.barraProgresso.reset()

		self.conectarSinaisESlots()

	def acharCaminhoDB(self, whatever):
		arquivo = self.acharArquivo()
		if arquivo != None:
			self.janelaPrincipal.caminhoDB.setText(arquivo)

	def acharCaminhoArquivosTD(self, whatever):
		arquivo = self.acharArquivo()
		if arquivo != None:
			self.janelaPrincipal.raizArquivosTD.setText(arquivo)

	def acharCaminhoTemp(self, whatever):
		arquivo = self.acharArquivo()
		if arquivo != None:
			self.janelaPrincipal.caminhoTemp.setText(arquivo)

	def acharArquivo(self, modo = QFileDialog.ExistingFile):
		selecionarArquivo = QFileDialog(self)
		selecionarArquivo.setFileMode(QFileDialog.ExistingFile);
		selecionarArquivo.setNameFilter(("Qualquer arquivo (*.*)"));
		selecionarArquivo.setViewMode(QFileDialog.Detail);

		if(selecionarArquivo.exec()):
			if len(selecionarArquivo.selectedFiles()) < 1:
				self.mostrar("ERRO AO SELECIONAR ARQUIVO. Desculpe pelo incômodo, mas aparentemente nenhum arquivo foi selecionado.")
				return None
			return selecionarArquivo.selectedFiles()[0]

		return None


	def conectarSinaisESlots(self):
		self.janelaPrincipal.botaoExecutar.clicked.connect(self.chamarAtualizar)
		self.janelaPrincipal.botaoSelecionarDB.clicked.connect(self.acharCaminhoDB)
		self.janelaPrincipal.botaoSelecionarRaiz.clicked.connect(self.acharCaminhoArquivosTD)
		self.janelaPrincipal.botaoSelecionarTemp.clicked.connect(self.acharCaminhoTemp)

	def chamarAtualizar(self,whatever):
		self.textoLog = ""
		caminhoDB = self.janelaPrincipal.caminhoDB.text()
		diretorioRaiz = self.janelaPrincipal.raizArquivosTD.text()
		arquivo_temporario = self.janelaPrincipal.caminhoTemp.text()
		letra_lote = self.janelaPrincipal.campoPrefixoLotes.text()
		tabela = self.janelaPrincipal.campoTabela.text()

		self.mostrar("Caminho do banco de dados: '{}', pasta onde pesquisar: '{}', arquivo temporário a ser criado: '{}', prefixo dos lotes: '{}', tabela selecionada: '{}'".format(caminhoDB, diretorioRaiz, arquivo_temporario, letra_lote, tabela))

		try:
			self.janelaPrincipal.barraProgresso.setMinimum(0)
			atualizar_remote_bid(diretorio_raiz = diretorioRaiz, letra_lote = letra_lote, nome_tabela = tabela,	caminho_banco = caminhoDB,
							 nome_do_arquivo_temporario = arquivo_temporario, mostrar = self.mostrar, 
							 func_max = self.janelaPrincipal.barraProgresso.setMaximum, func_passo = self.janelaPrincipal.barraProgresso.setValue)
		except:
			self.mostrar("UM ERRO OCORREU AO TENTAR ATUALIZAR O REMOTE BID:")
			e = sys.exc_info()
			for i in e:
				self.mostrar(str(i))

	#def mostrarBlu(self):
	#	self.mostrar("Blu"*100)

	def mostrar(self, string = "Blu"):
		self.janelaPrincipal.statusbar.showMessage(str(string), 10*1000)
		texto_horario ="[" + time.asctime(time.localtime(time.time())) + "]: " + string + "\n"

		with open("td_remote_bid.log", 'a') as log:
			log.write(texto_horario) 

		self.textoLog += texto_horario
		self.janelaPrincipal.caixaLog.setPlainText(self.textoLog)
		#self.janelaPrincipal.caixaLog.setHtml(self.textoLog)
		


if __name__ == '__main__':
	
	app = QApplication(sys.argv)

	programa = GerenciadorDeJanelas()
	programa.setWindowTitle('Atualização de Remote Bid')
	

	programa.show()
	
	sys.exit(app.exec_())

	quit()