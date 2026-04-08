from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor funcionando!"

@app.route('/calcular')
def calcular():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    op = request.args.get("op")

    if op == "+":
        resultado = a + b
        operacao = "Adição"
    elif op == "-":
        resultado = a - b
        operacao = "Subtração"
    elif op == "x":
        resultado = a * b
        operacao = "Multiplicação"
    elif op == "/":
        resultado = a / b
        operacao = "Divisão"
    else:
        return "Operação inválida"

    return jsonify({
        "a": a,
        "b": b,
        "operacao": operacao,
        "resultado": resultado
    })

app.run()