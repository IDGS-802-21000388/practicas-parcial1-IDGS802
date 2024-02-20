from flask import Flask, request, render_template
import forms, math
from io import open

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

# Calculadora 
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

# distancia de numeros
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

# Signos zodiacales
@app.route('/signoZodiacal', methods=["GET","POST"])
def signo():
    signoForm = forms.signoForm(request.form)
    if request.method == "POST":
        nombre = signoForm.nombre.data
        apaterno = signoForm.apaterno.data
        amaterno = signoForm.amaterno.data
        dia = signoForm.dia.data
        mes = signoForm.mes.data
        anio = signoForm.anio.data
        sexo = signoForm.sexo.data
        edad = 2024 - anio
        datosPersonales = [nombre, apaterno, amaterno, dia, mes, anio, sexo]
        signoZod = ''
        if anio == 2022 or anio == 2010 or anio == 1998 or anio == 1986 or anio == 1974 or anio == 1962:
            signoZod = 'Tigre'
        elif anio == 2023 or anio == 2011 or anio == 1999 or anio == 1987 or anio == 1975 or anio == 1963:
            signoZod = 'Conejo'
        elif anio == 2024 or anio == 2012 or anio == 2000 or anio == 1988 or anio == 1976 or anio == 1964:
            signoZod = 'Dragon'
        elif anio == 2025 or anio == 2013 or anio == 2001 or anio == 1989 or anio == 1977 or anio == 1965:
            signoZod = 'Serpiente'
        elif anio == 2026 or anio == 2014 or anio == 2002 or anio == 1990 or anio == 1978 or anio == 1966:
            signoZod = 'Caballo'
        elif anio == 2027 or anio == 2015 or anio == 2003 or anio == 1991 or anio == 1979 or anio == 1967:
            signoZod = 'Cabra'
        elif anio == 2028 or anio == 2016 or anio == 2004 or anio == 1992 or anio == 1980 or anio == 1968:
            signoZod = 'Mono'
        elif anio == 2029 or anio == 2017 or anio == 2005 or anio == 1993 or anio == 1981 or anio == 1969:
            signoZod = 'Gallo'
        elif anio == 2030 or anio == 2018 or anio == 2006 or anio == 1994 or anio == 1982 or anio == 1970:
            signoZod = 'Perro'
        elif anio == 2031 or anio == 2019 or anio == 2007 or anio == 1995 or anio == 1983 or anio == 1971:
            signoZod = 'Cerdo'
        elif anio == 2020 or anio == 2008 or anio == 1996 or anio == 1984 or anio == 1972 or anio == 1960:
            signoZod = 'Rata'
        elif anio == 2021 or anio == 2009 or anio == 1997 or anio == 1985 or anio == 1973 or anio == 1961:
            signoZod = 'Buey'

        src = "../static/bootstrap/img/" + signoZod + ".png"
        btnLimpiar = request.form.get("btnLimpiar")
        btnSiguiente = request.form.get("btnSiguiente")

        if btnLimpiar == 'Limpiar':
            signoForm.nombre.data = ''
            signoForm.apaterno.data = ''
            signoForm.amaterno.data = ''
            signoForm.dia.data = ''
            signoForm.mes.data = ''
            signoForm.anio.data = ''
            signoForm.sexo.data = ''

        elif btnSiguiente == 'Siguiente':
            return render_template('resultadoSigno.html', src = src, datosPersonales = datosPersonales, edad = edad, signoZod = signoZod)

    return render_template('signoZodiacal.html', form = signoForm)

@app.route('/palabras', methods=["GET","POST"])
def palabra():
    enviar_form = forms.EnviarForm(request.form)
    buscar_form = forms.BuscarForm(request.form)
    resultados = '' 
    print(request.form)
    if request.method == "POST":
        if 'btnEnviar' in request.form and enviar_form.validate():
            ingles = enviar_form.ingles.data
            espanol = enviar_form.espanol.data
            with open('palabras.txt', 'a') as archivo_texto:
                archivo_texto.write(f"\n{ingles}:{espanol}")
           
        elif 'btnBuscar' in request.form and buscar_form.validate():
            palabra = buscar_form.palabra.data
            idioma = buscar_form.radios.data
            with open('palabras.txt', 'r') as archivo_texto:
                for lineas in archivo_texto.readlines():
                    partes = lineas.strip().split(":")
                    if idioma == 'ingles':
                        if partes[0].lower() == palabra.lower():
                            resultados = f"Se encontró la palabra: {partes[1]}"
                            break
                    elif idioma == 'español':
                        if partes[1].lower() == palabra.lower():
                            resultados = f"Se encontró la palabra: {partes[0]}"
                            break
                if not resultados:
                    resultados = "La palabra no existe"

    return render_template('palabras.html', enviar_form=enviar_form, buscar_form=buscar_form, resultados=resultados)


if __name__ == '__main__':
    app.run(debug=True)