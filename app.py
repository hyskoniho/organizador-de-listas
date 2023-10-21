from flask import Flask, render_template, request, jsonify
import filter

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar-texto', methods=['POST'])
def processar_texto():
    dados = request.get_json()
    texto = dados.get('texto')

    listaFinal = filter.main(texto.splitlines())

    return jsonify({'mensagem': "\n".join(listaFinal)})

if __name__ == '__main__':
    app.run()
