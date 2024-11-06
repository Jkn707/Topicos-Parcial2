from flask import Flask

app = Flask(__name__)

class Vuelo:
    def __init__(self, id, nombre, tipo, precio):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

@app.route('/factorial/<int:num>')
def mostrarFactorial(num):
    resultado = factorial(num)
    return f"El factorial de {num} es {resultado}"

if __name__ == '__main__':
    app.run(debug=True)
