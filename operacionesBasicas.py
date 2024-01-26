from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/calculadora')
def calculadora():
    return render_template('operaciones.html')


@app.route('/resultado', methods=["GET", "POST"])
def mult1():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if operacion == 'suma':
            resultado = str(int(num1) + int(num2))
        elif operacion == 'resta':
            resultado = str(int(num1) - int(num2))
        elif operacion == 'multiplicacion':
            resultado = str(int(num1) * int(num2))
        elif operacion == 'division':
            resultado = str(int(num1) / int(num2))
    
    return render_template('operaciones.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)