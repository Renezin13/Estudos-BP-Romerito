from flask import Blueprint, render_template, request
from .tipagem import d4, d12, d20, d6

dados_bp = Blueprint("Dados", __name__, template_folder="templates", url_prefix="/dados")

@dados_bp.route('/', methods=['GET', 'POST'])
def dados():
   resultado = None
   if request.method == 'POST':
         # Pegando os valores do formulário
         dado = request.form['dado']
         
         if dado == '4':
               resultado = d4()
         elif dado == '6':
               resultado = d6()
         elif dado == '12':
               resultado = d12()
         elif dado == '20':
               resultado = d20()
   
   return render_template("dados.html", resultado=resultado)
