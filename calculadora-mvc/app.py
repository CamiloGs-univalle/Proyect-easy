# app.py
from flask import Flask, jsonify, request, render_template
from modelo import ModeloCalculadora

app = Flask(__name__)
calculadora = ModeloCalculadora()

@app.route('/')
def index():
    return render_template('vista.html')  # Carga la vista web

@app.route('/calcular', methods=['GET'])
def calcular():
    operacion = request.args.get('operacion')
    
    try:
        # Usar la operación como expresión en el modelo
        resultado = eval(operacion)
        return jsonify({"resultado": resultado})
    except ZeroDivisionError:
        return jsonify({"error": "Error: División por cero"}), 400
    except Exception:
        return jsonify({"error": "Error: Expresión inválida"}), 400

if __name__ == '__main__':
    app.run(debug=True)
