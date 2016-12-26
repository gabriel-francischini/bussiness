import os
import pyodbc

def printar(string):
	print(string)

def fazer_nada(wahtever):
	pass
	return None


def atualizar_remote_bid(diretorio_raiz = r"Y:\AUTO TEST DRIVE\2016\12_DEZEMBRO", letra_lote = "C", 
						 nome_tabela = "AUTO_TD_NOVO_FORM",	caminho_banco = r'''Z:\AUTO HONDA\TESTDRIVE\EXPORTACAO\TD_Data_V2015.mdb''',
						 nome_do_arquivo_temporario = "arquivo_td_temp.txt", mostrar = printar, func_max = fazer_nada, func_passo = fazer_nada):
	# Pasta a ser pesquisada
	#diretorio_raiz = r"Y:\AUTO TEST DRIVE\2016\12_DEZEMBRO"
	#letra_lote = "C"
	#nome_tabela = "AUTO_TD_NOVO_FORM"
	#caminho_banco = r'''Z:\AUTO HONDA\TESTDRIVE\EXPORTACAO\TD_Data_V2015.mdb'''
	#nome_do_arquivo_temporario = "arquivo_td_temp.txt"
		
	
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
	mostrar("Conectando ao banco de dados...")
	# Conexão com o odbc
	conn = pyodbc.connect(odbc_conn_str)
	conn_editar = pyodbc.connect(odbc_conn_str)
	# Todas as operações sobre o banco de dados são feitas através do cursor
	cursor = conn.cursor()
	cursor_editar = conn_editar.cursor()
	# Verifica se é necessário continuar verificando a lista atual ou se já podemos ir para a próxima entrada
	encontrou = False
	
	mostrar("Procurando arquivos...")
	
	
	arquivo_temp = open(nome_do_arquivo_temporario, 'w')
	
	for (diretorio, nao_sei_o_que_e_essa_variavel, lista_arquivos) in os.walk(diretorio_raiz):
		for arquivo in lista_arquivos:
			# Computa o diretório total absoluto do arquivo
			diretorio_total = diretorio + "\\" + arquivo
	
			arquivo_temp.write("" + diretorio_total + "\n")	
	
	arquivo_temp.close()
	
	# Conta a quantidade de arquivos na tabela
	cursor.execute("select * from "+ nome_tabela + " where remote_bid like '0' order by batchtrack")
	entrada = cursor.fetchone()

	numero_de_remote_bid_a_corrigir = 0

	while  entrada:
		numero_de_remote_bid_a_corrigir += 1
		entrada = cursor.fetchone()

	func_max(numero_de_remote_bid_a_corrigir)

	numero_de_remote_bid_corrigidos = 0

	# Confere a tabela
	cursor.execute("select * from "+ nome_tabela + " where remote_bid like '0' order by batchtrack")
	
	entrada = cursor.fetchone()
	
	while  entrada:
	
		lote = entrada[17]
		tif = entrada[20].rsplit("[ 1 ]",1)[0]
	
		nome_RGV = lote.strip() + "\\" + tif
	
		if(letra_lote not in lote):
			#mostrar("O lote " + nome_RGV + " não contém a letra " + letra_lote)
	
			entrada = cursor.fetchone()
			continue
	
		arquivo_temp = open(nome_do_arquivo_temporario, 'r')
	
		# Para cada grupo Diretório/Lista de Arquivos encontrado
		for linha in arquivo_temp:
	
			diretorio = linha.rsplit("\\", 1)[0].split(letra_lote, 1)[0].strip()
			arquivo = linha.rsplit("\\", 1)[1].strip()
	
			#mostrar("O diretorio é:\t" + diretorio + "\t e o arquivo é:\t" + arquivo)
	
			#(diretorio, nao_sei_o_que_e_essa_variavel, lista_arquivos)
	
			# Para cada arquivo na lista de arquivos
			#for arquivo in lista_arquivos:
	
			if( (letra_lote + diretorio.rsplit("\\", 1)[1]) != lote):
				#mostrar("Diretorio: " + letra_lote + diretorio.rsplit("\\", 1)[1] + "\t Lote: " + lote + "\tDiferem. Pulando.")
				continue
	
	
			# Computa o diretório total absoluto do arquivo
			diretorio_total = diretorio + "\\" + arquivo
	
			diretorio_parcial = diretorio_total.rsplit("\\", 2)
			diretorio_parcial = letra_lote + diretorio_parcial[1] + "\\" + diretorio_parcial[2]
	
			#mostrar("Testando \t'" + nome_RGV + "'\n contra \t'" + diretorio_parcial + "'\n do lote " + lote)
	
			if(nome_RGV == diretorio_parcial ):
				#tif_impar = ""
				#try:
				#	tif_impar = entrada[20].rsplit("[ 1 ]",1)[0]
				#	tif_impar = tif_impar.rsplit(".tif", 1)[0]
				#	tif_impar = int(tif_impar) - 1
				#	tif_impar = "{:0>8}".format(tif_impar)
				#	tif_impar = tif_impar + ".tif"
				#except:
				#	tif_impar = entrada[20].rsplit("[ 1 ]",1)[0]
				#	tif_impar = entrada[20]
				#	mostrar("OCORREU ERRO AO CONVERTER NUMERO DO TIFF: '" + tif_impar + "' COM LOTE: '" + lote+ "'. ABORTANDO ATUALIZAÇÃO DESTE REMOTE_BID")
				#	encontrou = True
				#	break
				
				mostrar("Atualizando remote_bid do arquivo " + diretorio_total + "\t onde BatchTrack = '{}' e BatchPgDta = '{}'".format(entrada[17], entrada[20]))
				cursor_editar.execute("UPDATE " + nome_tabela + " SET remote_bid=? WHERE BatchTrack=? AND BatchPgDta=?", ((diretorio + "\\" + tif), entrada[17], entrada[20]) )
				encontrou = True
				cursor_editar.commit()

				numero_de_remote_bid_corrigidos += 1
				func_passo(numero_de_remote_bid_corrigidos)
				break
	
		arquivo_temp.close()
	
		if(not encontrou):
			mostrar("O arquivo " + nome_RGV + " não encontrado no sistema de arquivos")
			
			numero_de_remote_bid_corrigidos += 1
			func_passo(numero_de_remote_bid_corrigidos)
			pass
		
		entrada = cursor.fetchone()
	
	
	cursor_editar.commit()
	
	
	
	
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
	#			#mostrar("Testando " + diretorio_parcial + " contra " + nome_RGV)
	#
	#			if(diretorio_parcial == nome_RGV):
	#				mostrar("O arquivo " + diretorio_total + " tem no sistema de arquivos mas não nas tabelas")
	#
	#				encontrou = True
	#
	#			entrada = cursor.fetchone()
	#
	#		if (encontrou):
	#			mostrar("Entrada processada")
	#
	#			encontrou = False
	#			continue
	#
	#		if (not entrada):
	#			mostrar("O arquivo " + diretorio_total + " não consta no banco de dados com remote_bid 0")
	#			
	#			continue
	#
	#


if __name__ == '__main__':
	atualizar_remote_bid()