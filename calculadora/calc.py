from flask import Blueprint, render_template, request
from .matematica import soma, subtracao, multiplicacao, resto

calculadora_bp = Blueprint("Calculadora", __name__, template_folder="templates", url_prefix="/calc")

@calculadora_bp.route('/', methods=['GET', 'POST'])
def calculadora():
      resultado = None
      if request.method == 'POST':
            # Pegando os valores do formulário
            a = int(request.form['a'])
            b = int(request.form['b'])
            operacao = request.form['operacao']
            
            # Executando a operação selecionada
            if operacao == 'soma':
                  resultado = soma(a, b)
            elif operacao == 'subtracao':
                  resultado = subtracao(a, b)
            elif operacao == 'multiplicacao':
                  resultado = multiplicacao(a, b)
            elif operacao == 'resto':
                  resultado = resto(a, b)
      
      return render_template("calculadora.html", resultado=resultado)
