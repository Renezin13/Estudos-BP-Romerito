from flask import Blueprint, render_template, request, redirect, url_for
from .jog_models import Jogador

jogadores_bp = Blueprint("Jogadores", __name__, template_folder="templates", url_prefix="/jogador")

@jogadores_bp.route('/', methods=['GET', 'POST'])
def listar_jogadores():
   jogadores = Jogador.list_all()
   return render_template("listar_jogadores.html", jogadores=jogadores)

# Rota para cadastrar um novo jogador
@jogadores_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_jogador():
   if request.method == 'POST':
      nome = request.form['nome']
      classe = request.form['classe']
      vida = request.form['vida']
      
      # Cria o jogador no banco de dados
      Jogador.create(nome, classe, vida)
      return redirect(url_for('Jogadores.listar_jogadores'))
   
   return render_template("cadastrar_jogador.html")
