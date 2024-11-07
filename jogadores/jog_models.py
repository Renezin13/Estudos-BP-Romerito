import sqlite3

def obter_conexao():
   return sqlite3.connect('db_rpg.db')  # Banco de dados SQLite armazenado em um arquivo local

class Jogador():
   def __init__(self, id, nome, classe, vida):
      self.id = id
      self.nome = nome
      self.classe = classe
      self.vida = vida

   @staticmethod
   def get(jog_id):
      conexao = obter_conexao()
      cursor = conexao.cursor()
      cursor.execute("SELECT * FROM tb_jogador WHERE jog_id = ?", (jog_id,))
      result = cursor.fetchone()
      conexao.close()
      if result:
         return Jogador(result[0], result[1], result[2], result[3])
      return None

   @staticmethod
   def create(nome, classe, vida):
      conexao = obter_conexao()
      cursor = conexao.cursor()
      cursor.execute("INSERT INTO tb_jogador (jog_nome, jog_class, jog_vida) VALUES (?, ?, ?)", (nome, classe, vida))
      conexao.commit()
      conexao.close()

   @staticmethod
   def list_all():
      conexao = obter_conexao()
      cursor = conexao.cursor()
      cursor.execute("SELECT * FROM tb_jogador")
      results = cursor.fetchall()
      conexao.close()

      jogadores = []
      for result in results:
         jogadores.append(Jogador(result[0], result[1], result[2], result[3]))
      return jogadores
