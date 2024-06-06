import pymssql

def testar_conexao_sql_server(server, user, password, database):
    try:
        # Conectar ao servidor SQL Server
        conn = pymssql.connect(server, user, password, database)
        print("Conexão bem-sucedida!")

        cursor = conn.cursor()

        # Consulta SQL para listar tabelas
        query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'"

        # Executar a consulta
        cursor.execute(query)

        # Obter todas as tabelas
        tabelas = cursor.fetchall()

        # Imprimir o nome das tabelas
        print("Tabelas no banco de dados:")
        for tabela in tabelas:
            print(tabela[0])

        # Fechar a conexão
        conn.close()
    except Exception as e:
        print("Erro ao conectar ao banco de dados:", e)

# Substitua os valores abaixo pelos correspondentes ao seu servidor SQL Server
server = "localhost"
user = "sa"
password = "Jogador@crud"
database = "crudNextPython"

testar_conexao_sql_server(server, user, password, database)
