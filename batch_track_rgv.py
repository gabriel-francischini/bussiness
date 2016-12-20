import os

# Pasta a ser pesquisada
diretorio_raiz = r"Y:\AUTO HONDA\RGV\2016\12_DEZEMBRO"
letra_lote = "F"
nome_tabela = "DATAV16"
caminho_banco = r'''C:\Users\Latitude\Desktop\PYTHON SCRIPTS\BASE_FORM_V15.mdb'''
nome_do_arquivo_temporario = "arquivo_td_temp.txt"

import pyodbc


### Código a seguir foi CTRL+C & CTRL+V do quebrar_tabela.py
# Variável com o caminho para o banco
db_file = caminho_banco
#  Usuário e senhas para acessar o banco
user = 'admin'
password = ''
# Driver usado para se conectar
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
# Para versões mais novas do driver odbc
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
print("Conectando ao banco de dados...")
# Conexão com o odbc
conn = pyodbc.connect(odbc_conn_str)
conn_editar = pyodbc.connect(odbc_conn_str)
# Todas as operações sobre o banco de dados são feitas através do cursor
cursor = conn.cursor()
cursor_editar = conn_editar.cursor()
# Verifica se é necessário continuar verificando a lista atual ou se já podemos ir para a próxima entrada
encontrou = False

print("Procurando arquivos...")


arquivo_temp = open(nome_do_arquivo_temporario, 'w')

for (diretorio, nao_sei_o_que_e_essa_variavel, lista_arquivos) in os.walk(diretorio_raiz):
	for arquivo in lista_arquivos:
		# Computa o diretório total absoluto do arquivo
		diretorio_total = diretorio + "\\" + arquivo

		arquivo_temp.write("" + diretorio_total + "\n")	

arquivo_temp.close()


print("Conferindo BatchPgDta's...")

cursor.execute("select * from "+ nome_tabela + "")
entrada = cursor.fetchone()

while  entrada:

	if entrada[20] is None:
		CSID = entrada[8]
		numero_tif = CSID.rsplit("-", 1)[1].strip()
		novo_batchpgdta = "{:0>8}.tif[ 1 ]".format(numero_tif) 
		
		print("Atualizando \tBatchPgDta = '{}' do arquivo onde \tBatchTrack = '{}' e \tCSID = '{}'".format(novo_batchpgdta, entrada[17], CSID))
		cursor_editar.execute("UPDATE " + nome_tabela + " SET BatchPgDta=? WHERE BatchTrack=? AND CSID=?", (novo_batchpgdta, entrada[17], CSID) )
		encontrou = True
		cursor_editar.commit()
	else:
		if len(entrada[20]) != len("00000002.tif[ 1 ]"):
			CSID = entrada[8]
			numero_tif = CSID.rsplit("-", 1)[1].strip()
			novo_batchpgdta = "{:0>8}.tif[ 1 ]".format(numero_tif) 
		
			print("Atualizando \tBatchPgDta = '{}' para \t'{}' do arquivo onde \tBatchTrack = '{}' e \tCSID = '{}'".format(entrada[20], novo_batchpgdta, entrada[17], CSID))
			cursor_editar.execute("UPDATE " + nome_tabela + " SET BatchPgDta=? WHERE BatchTrack=? AND CSID=?", (novo_batchpgdta, entrada[17], CSID) )
			encontrou = True
			cursor_editar.commit()	


	entrada = cursor.fetchone()



print("Conferindo Remote_BID's...")


# Confere a tabela
cursor.execute("select * from "+ nome_tabela + " where remote_bid like '0' order by batchtrack")

entrada = cursor.fetchone()

while  entrada:

	lote = entrada[17]	
	#letra_lote = lote[0]
	tif = entrada[20].rsplit("[ 1 ]",1)[0]

	nome_RGV = lote.strip() + "\\" + tif

	if(letra_lote not in lote):
		#print("O lote " + nome_RGV + " não contém a letra " + letra_lote)

		entrada = cursor.fetchone()
		continue

	arquivo_temp = open(nome_do_arquivo_temporario, 'r')

	# Para cada grupo Diretório/Lista de Arquivos encontrado
	for linha in arquivo_temp:

		diretorio = linha.rsplit("\\", 1)[0].split(letra_lote, 1)[0].strip()
		arquivo = linha.rsplit("\\", 1)[1].strip()

		#print("O diretorio é:\t" + diretorio + "\t e o arquivo é:\t" + arquivo)

		#(diretorio, nao_sei_o_que_e_essa_variavel, lista_arquivos)

		# Para cada arquivo na lista de arquivos
		#for arquivo in lista_arquivos:

		if( (letra_lote + diretorio.rsplit("\\", 1)[1]) != lote):
			#print("Diretorio: " + letra_lote + diretorio.rsplit("\\", 1)[1] + "\t Lote: " + lote + "\tDiferem. Pulando.")
			continue


		# Computa o diretório total absoluto do arquivo
		diretorio_total = diretorio + "\\" + arquivo

		diretorio_parcial = diretorio_total.rsplit("\\", 2)
		diretorio_parcial = letra_lote + diretorio_parcial[1] + "\\" + diretorio_parcial[2]

		#print("Testando \t'" + nome_RGV + "'\n contra \t'" + diretorio_parcial + "'\n do lote " + lote)

		if(nome_RGV == diretorio_parcial ):
			tif_impar = ""
			try:
				tif_impar = entrada[20].rsplit("[ 1 ]",1)[0]
				tif_impar = tif_impar.rsplit(".tif", 1)[0]
				tif_impar = int(tif_impar) - 1
				tif_impar = "{:0>8}".format(tif_impar)
				tif_impar = tif_impar + ".tif"
			except:
				tif_impar = entrada[20].rsplit("[ 1 ]",1)[0]
				tif_impar = entrada[20]
				print("OCORREU ERRO AO CONVERTER NUMERO DO TIFF: '" + tif_impar + "' COM LOTE: '" + lote+ "'. ABORTANDO ATUALIZAÇÃO DESTE REMOTE_BID")
				encontrou = True
				break
			
			print("Atualizando Remote_BID (frente correspondente: '"+ tif_impar + "') do arquivo " + diretorio_total + "\t onde BatchTrack = '{}' e BatchPgDta = '{}'".format(entrada[17], entrada[20]))
			cursor_editar.execute("UPDATE " + nome_tabela + " SET remote_bid=? WHERE BatchTrack=? AND BatchPgDta=?", ((diretorio + "\\" + tif_impar), entrada[17], entrada[20]) )
			encontrou = True
			cursor_editar.commit()
			break

	arquivo_temp.close()

	if(not encontrou):
		print("O arquivo " + nome_RGV + " não encontrado no sistema de arquivos")
		pass
	
	entrada = cursor.fetchone()


cursor_editar.commit()

conn.close()
conn_editar.close()


# Para cada grupo Diretório/Lista de Arquivos encontrado
#for (diretorio, nao_sei_o_que_e_essa_variavel, lista_arquivos) in os.walk(diretorio_raiz):
#
#	# Para cada arquivo na lista de arquivos
#	for arquivo in lista_arquivos:
#
#		# Computa o diretório total absoluto do arquivo
#		diretorio_total = diretorio + "\\" + arquivo
#
#		diretorio_parcial = diretorio_total.rsplit("\\", 2)
#		diretorio_parcial = letra_lote + diretorio_parcial[1] + "\\" + diretorio_parcial[2]
#
#
#		# Confere a tabela
#		cursor.execute("select * from DATAV16 where remote_bid like '0' order by batchtrack")
#
#		entrada = cursor.fetchone()
#
#
#		while  (not encontrou) and (entrada):
#
#			lote = entrada[17]
#			tif = entrada[20].rsplit("[ 1 ]",1)[0]
#			nome_RGV = lote + "\\" + tif
#
#			#print("Testando " + diretorio_parcial + " contra " + nome_RGV)
#
#			if(diretorio_parcial == nome_RGV):
#				print("O arquivo " + diretorio_total + " tem no sistema de arquivos mas não nas tabelas")
#
#				encontrou = True
#
#			entrada = cursor.fetchone()
#
#		if (encontrou):
#			print("Entrada processada")
#
#			encontrou = False
#			continue
#
#		if (not entrada):
#			print("O arquivo " + diretorio_total + " não consta no banco de dados com remote_bid 0")
#			
#			continue
#
#