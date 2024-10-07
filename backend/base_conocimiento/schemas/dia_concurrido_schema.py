from utils.ma import ma
from marshmallow import fields
from models.dia_concurrido import DiaConcurrido

from schemas.museo_schema import Museo_Schema
from schemas.dia_schema import Dia_Schema

class DiaConcurrido_Schema(ma.Schema):
    class Meta:
        model = DiaConcurrido
        fields = (
            'id_museo', 
            'id_dia',
            'museo',
            'dia'
            )
    
    museo = ma.Nested(Museo_Schema)
    dia = ma.Nested(Dia_Schema)

dia_concurrido_schema = DiaConcurrido_Schema()
dias_concurridos_schema = DiaConcurrido_Schema(many=True)