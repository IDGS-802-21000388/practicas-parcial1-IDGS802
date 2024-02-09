from flask import Flask, request, render_template
import forms

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/signoZodiacal', methods=["GET","POST"])
def signo():
    num_form = forms.NumForm(request.form)
    if request.method == "POST":
        nombre = num_form.nombre.data
        apaterno = num_form.apaterno.data
        amaterno = num_form.amaterno.data
        dia = num_form.dia.data
        mes = num_form.mes.data
        anio = num_form.anio.data
        sexo = num_form.sexo.data
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
            num_form.nombre.data = ''
            num_form.apaterno.data = ''
            num_form.amaterno.data = ''
            num_form.dia.data = ''
            num_form.mes.data = ''
            num_form.anio.data = ''
            num_form.sexo.data = ''

        elif btnSiguiente == 'Siguiente':
            return render_template('resultadoSigno.html', src = src, datosPersonales = datosPersonales, edad = edad, signoZod = signoZod)

    return render_template('signoZodiacal.html', form = num_form)

if __name__ == '__main__':
    app.run(debug=True)