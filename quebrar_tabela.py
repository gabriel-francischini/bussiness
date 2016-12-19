# Importa a biblioteca odbc
import pyodbc
import math

# Variável com o caminho para o banco
db_file = r'''C:\Users\Latitude\Desktop\qCEP.mdb'''

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

# Executa uma consulta ao banco
cursor.execute("select * from CEP_COM order by endereco_cep")

# Prepara para contar todas as entradas do banco de dados
# a variável entrada será uma entrada do banco de dados enquanto
# existirem entradas na tabela. Quando não houver mais entradas, ela será
# tera um valor booleano Falso
entrada = True


print("\nContando o total de CEPs cadastrados no banco de dados...")


# Contador das entradas
total_entradas = 0

while entrada:
	# A linha de teste a seguir não é mais necessária
	#print(entrada)

	entrada = cursor.fetchone()
	total_entradas += 1


print("\nHá " + str(total_entradas) + " entradas no banco de dados")

# Encontra o melhor número (inteiro) de tabelas para usar
numero_de_tabelas = math.ceil(math.sqrt(total_entradas))

# Calcula quantas entradas de CEP devem haver em cada tabela
entradas_por_tabela = math.ceil(total_entradas/numero_de_tabelas)

print("Serão " + str(numero_de_tabelas) + " tabelas necessárias, cada uma com " + str(entradas_por_tabela) + " entradas, totalizando " + str(numero_de_tabelas * entradas_por_tabela) + " entradas")

# Algoritmo para garantir que os CEPs estão em ordem CRESCENTE
# (isso é fundamental para o algoritmo funcionar)

print("Verificando se a tabela é ordenável...")

# Define uma variável para guardar se a tabela está ordenada ou não
ordenado = True

# Faz a consulta
cursor.execute("select * from CEP_COM order by Endereco_CEP")

cep_anterior = 0

# Inicia a entrada com o primeiro valor
entrada = cursor.fetchone()
contador_ordem = 1

# Uncomment a linha a seguir para verificar que o python
# da erro ao tentar converter texto que não represente inteiro para inteiro
#int("012Blu")

# A segunda coluna corresponde ao endereco_cep, a primeira ao codigo, etc
codigo = 0
endereco_cep = 1
endereco_logradouro = 2
bairro_descricao = 3
cidade_descricao = 4
uf_sigla = 5

while entrada:

	contador_ordem = contador_ordem + 1
	
	#print(" " + str(contador_ordem), end='')
	
	# Descomente a linha a seguir para receber feedback visual
	# sobre a entrada sendo verificada
	#print(entrada[endereco_cep])

	if(int(entrada[endereco_cep]) >= cep_anterior):
		ordenado = True
	
	else:
		ordenado = False
		break

	cep_anterior = int(entrada[endereco_cep])

	entrada = cursor.fetchone()




print("Há " + str(total_entradas) + " entradas, das quais " + str(contador_ordem) + " estão ordenadas.")

if contador_ordem != total_entradas:
	print("A tabela não pode ser ordenada usando o valor Endereco_CEP. Abortando execução.")
	quit()




# Agora quebraremos as tabelas

str_criar_tabela1 = "CREATE TABLE "
str_criar_tabela2 = "(Codigo int, Endereco_CEP varchar(255), Endereco_logradouro varchar(255), Bairro_Descricao varchar(255), Cidade_Descricao varchar(255), uf_sigla varchar(255) )"
str_inserir_tabela1 = "INSERT INTO "
str_inserir_tabela2 = " (Codigo, Endereco_CEP, Endereco_logradouro, Bairro_Descricao, Cidade_Descricao, uf_sigla) VALUES "

# O código a seguir cria as tabelas
print("Criando as tabelas...\n\n\n")

# Faz a consulta
cursor.execute("select * from CEP_COM order by Endereco_CEP")
entrada = cursor.fetchone()

contador_tabela_atual = 0
contador_itens = 0

# Não é possível iterar pela query e modificar o banco simultaneamente na mesma conexão
# portanto duas conexões serão usadas (uma de leitura e outra de gravação)
conn2 = pyodbc.connect(odbc_conn_str)
cursor2 = conn2.cursor()

cep_inicio = 0
cep_ultimo = 0

print("\n\n")

while entrada:

	if(contador_itens > (entradas_por_tabela)):
		contador_itens = 0

	nome_da_tabela = "table" + str(contador_tabela_atual)

	if(contador_itens == 0):
		print("\n\n\n\t IF ({} <= valor_cep) AND (valor_cep <= {}) THEN \n\t\t tabela_consulta = \"{}\"\n\t END IF".format(cep_inicio, cep_ultimo, nome_da_tabela) )
		cep_inicio = int(entrada[endereco_cep])
		contador_tabela_atual = contador_tabela_atual + 1
		contador_itens = contador_itens + 1
		nome_da_tabela = "table" + str(contador_tabela_atual)
		criar_tabela = str_criar_tabela1 + nome_da_tabela + str_criar_tabela2
		conn2.commit()
		#print(criar_tabela)
		cursor2.execute(criar_tabela)

	inserir_valores = str_inserir_tabela1 + nome_da_tabela + str_inserir_tabela2 + "( " + str(entrada[codigo]).replace("\'", "\'\'").replace("\"", "\'\'\'\'") + ", \'" + str(entrada[endereco_cep]).replace("\'", "\'\'").replace("\"", "\'\'\'\'") + "\', \'" + str(entrada[endereco_logradouro]).replace("\'", "\'\'").replace("\"", "\'\'\'\'") + "\', \'" + str(entrada[bairro_descricao]).replace("\'", "\'\'").replace("\"", "\'\'\'\'") + "\', \'" + str(entrada[cidade_descricao]).replace("\'", "\'\'").replace("\"", "\'\'\'\'") + "\', \'" + str(entrada[uf_sigla]).replace("\'", "\'\'").replace("\"", "\'\'\'\'") + "\')" 
	#print(inserir_valores)

	cep_ultimo = int(entrada[endereco_cep])
	cursor2.execute(inserir_valores)
	contador_itens = contador_itens + 1
	entrada = cursor.fetchone()


#cursor.execute(str_criar_tabela1 + str(contador_tabela_atual) + str_criar_tabela2)
# Salva as alterações no banco de dados
conn2.commit()