from utils.ma import ma
from models.dia import Dia
from marshmallow import fields

class Dia_Schema(ma.Schema):
    class Meta:
        model = Dia
        fields = (
            'id_dia', 
            'nombre'
            )
        
dia_schema = Dia_Schema()
dias_schema = Dia_Schema(many=True)