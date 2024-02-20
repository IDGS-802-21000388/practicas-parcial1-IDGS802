from wtforms import Form, validators
from wtforms import IntegerField, RadioField, StringField

class EnviarForm(Form):
    ingles = StringField("ingles",
           [validators.DataRequired(message='El campo es requerido')])
    espanol = StringField("español",
            [validators.DataRequired(message='El campo es requerido')])

class BuscarForm(Form):
    radios = RadioField('Selecciona un idioma', choices=[("ingles","ingles"),("español","español")])
    palabra = StringField("palabra",
            [validators.DataRequired(message='El campo es requerido')])

class NumForm(Form):
    x1 = IntegerField("x1")
    x2 = IntegerField("x2")
    y1 = IntegerField("y1")
    y2 = IntegerField("y2")

class signoForm(Form):
    nombre = StringField("nombre")
    apaterno = StringField("apaterno")
    amaterno = StringField("amaterno")
    dia = IntegerField("dia")
    mes = IntegerField("mes")
    anio = IntegerField("anio")
    sexo = RadioField('Sexo', choices=[("Masculino","Masculino"),("Femenino","Femenino")])
