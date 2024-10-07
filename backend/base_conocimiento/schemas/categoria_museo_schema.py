from utils.ma import ma
from models.categoria_museo import CategoriaMuseo
from marshmallow import fields

from schemas.museo_schema import Museo_Schema
from schemas.categoria_schema import Categoria_Schema

class CategoriaMuseo_Schema(ma.Schema):
    class Meta:
        model = CategoriaMuseo
        fields = (
            "id_categoria",
            "id_museo",
            "museo",
            "categoria"
        )
    museo = ma.Nested(Museo_Schema)
    categoria = ma.Nested(Categoria_Schema)

categoria_museo_schema = CategoriaMuseo_Schema()
categorias_museo_schema = CategoriaMuseo_Schema(many=True) 
    