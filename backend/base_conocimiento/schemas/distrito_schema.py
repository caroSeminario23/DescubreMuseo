from utils.ma import ma
from models.distrito import Distrito
from marshmallow import fields

class Distrito_Schema(ma.Schema):
    class Meta:
        model = Distrito
        fields = (
            'id',
            'nombre'
            )
distrito_schema =Distrito_Schema()
distritos_schema = Distrito_Schema(many=True)


