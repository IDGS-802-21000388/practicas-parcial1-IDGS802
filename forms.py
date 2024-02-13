from wtforms import Form
from wtforms import IntegerField, Field, RadioField, StringField

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