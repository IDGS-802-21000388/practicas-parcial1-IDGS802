from wtforms import Form
from wtforms import IntegerField, Field, RadioField, StringField

class NumForm(Form):
    nombre = StringField("nombre")
    apaterno = StringField("apaterno")
    amaterno = StringField("amaterno")
    dia = IntegerField("dia")
    mes = IntegerField("mes")
    anio = IntegerField("anio")
    sexo = RadioField('Sexo', choices=[("Masculino","Masculino"),("Femenino","Femenino")])