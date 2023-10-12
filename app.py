from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processar-texto', methods=['POST'])
def processar_texto():
    dados = request.get_json()
    texto = dados.get('texto')


    lista = texto.splitlines()
    listaFinal = []

    for x in range(len(lista)):
        for char in '1234567890-.':
            if char in lista[x]:
                lista[x] = lista[x].replace(char, "")

        while lista[x][0] == " ":
            lista[x] = lista[x][1:]

        lista[x] = lista[x][0].upper() + lista[x][1:]
        
    lista = sorted(lista)   
    for x in range(len(lista)):
        nome_completo = lista[x].split()
        for y in range(len(nome_completo)):
            if nome_completo[y][0].islower():
                palavra = nome_completo[y][0].upper() + nome_completo[y][1:]
                nome_completo[y] = palavra
        lista[x] = " ".join(nome_completo)

    for x in range(len(lista)):
        if lista[x] != lista[x-1]:
            listaFinal.append(lista[x] + " ")

    
    return jsonify({'mensagem': "\n".join(listaFinal)})

if __name__ == '__main__':
    app.run()
