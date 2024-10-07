from utils.ma import ma
from models.dia_atencion import DiaAtencion
from marshmallow import fields

from schemas.museo_schema import Museo_Schema
from schemas.dia_schema import Dia_Schema

class DiaAtencion_Schema(ma.Schema):
    class Meta:
        model = DiaAtencion
        fields = (
            'id_museo', 
            'id_dia',
            'museo',
            'dia'
            )
        
    museo = ma.Nested(Museo_Schema)
    dia = ma.Nested(Dia_Schema)

dia_atencion_schema = DiaAtencion_Schema()
dias_atencion_schema = DiaAtencion_Schema(many=True)