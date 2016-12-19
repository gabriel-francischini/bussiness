import os
import pyodbc

# Pasta a ser pesquisada
diretorio_raiz = r"C:\Users\Latitude\Desktop\11_NOVEMBRO"


### Código a seguir foi CTRL+C & CTRL+V do quebrar_tabela.py
# Variável com o caminho para o banco
db_file = r'''C:\Users\Latitude\Desktop\BASE_FORM_V15.mdb'''
#  Usuário e senhas para acessar o banco
user = 'admin'
password = ''
# Driver usado para se conectar
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
# Para versões mais novas do driver odbc
odbc_conn_str = 'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=%s;UID=%s;PWD=%s' %\
                (db_file, user, password)
# Conexão com o odbc
conn = pyodbc.connect(odbc_conn_str)
# Todas as operações sobre o banco de dados são feitas através do cursor
cursor = conn.cursor()

cursor.execute("DROP TABLE LINK")

# Cria a tabela na qual salvar o endereço dos arquivos
cursor.execute("CREATE TABLE LINK (link varchar(255) not null, constraint codigo primary key (link))")

# Para cada grupo Diretório/Lista de Arquivos encontrado
for (diretorio, nao_sei_o_que_e_essa_variavel, lista_arquivos) in os.walk(diretorio_raiz):

	# Para cada arquivo na lista de arquivos
	for arquivo in lista_arquivos:

		# Computa o diretório total absoluto do arquivo
		diretorio_total = diretorio + "\\" + arquivo
		#diretorio_total = diretorio_total.replace("\\", conn.searchescape + "\\").replace(":", conn.searchescape + ":").replace(".", conn.searchescape + ".").strip()

		print("Incluindo arquivo: " + diretorio_total)

		incluir_arquivo = "INSERT INTO LINK (link) VALUES (?)"

		#print("Comando de inlcuir: " + incluir_arquivo)

		# Insere na tabela
		cursor.execute(incluir_arquivo, (diretorio_total))

		conn.commit()




