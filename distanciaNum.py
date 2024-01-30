from flask import Flask, request, render_template
import forms, math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/distNumeros', methods=["GET","POST"])
def alumnos():
    num_form = forms.NumForm(request.form)
    res = 0
    if request.method == "POST":
        x1 = num_form.x1.data
        x2 = num_form.x2.data
        y1 = num_form.y1.data
        y2 = num_form.y2.data

        parte1 = (x1-x2) * (x1-x2)
        parte2 = (y1-y2) * (y1-y2)
        parte3 = parte1+parte2
        res = math.sqrt(int(parte3))

    return render_template('distanciaNumeros.html', form = num_form, res = res)

if __name__ == '__main__':
    app.run(debug=True)