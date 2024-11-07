from flask import Flask
from calculadora.calc import calculadora_bp
from dados.dados import dados_bp
from jogadores.jogadores import jogadores_bp

app = Flask(__name__)

app.register_blueprint(calculadora_bp)
app.register_blueprint(dados_bp)
app.register_blueprint(jogadores_bp)

if __name__ == "__main__":
   app.run(debug=True)

