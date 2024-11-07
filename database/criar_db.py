import sqlite3

# Caminho onde o arquivo do banco de dados .db será criado
db_path = 'db_rpg.db'

# Conectar ao banco de dados SQLite (cria o arquivo db_rpg.db se ele não existir)
conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# Ler o conteúdo do arquivo schema.sql e executar os comandos
with open('database/schema.sql', 'r') as arquivo:  # Use o caminho correto para o seu schema.sql
   script_sql = arquivo.read()
   cursor.executescript(script_sql)  # Executa o script SQL para criar o banco e as tabelas

# Confirmar e fechar a conexão
conexao.commit()
conexao.close()

print(f"Banco de dados '{db_path}' criado com sucesso com base no arquivo schema.sql")
