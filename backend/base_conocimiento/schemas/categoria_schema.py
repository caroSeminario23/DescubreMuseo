from utils.ma import ma
from models.categoria import Categoria
from marshmallow import fields

class Categoria_Schema(ma.Schema):
    class Meta:
        model = Categoria
        fields = (
            'id_categoria', 
            'nombre'
            )
        
categoria_schema = Categoria_Schema()
categorias_schema = Categoria_Schema(many=True)