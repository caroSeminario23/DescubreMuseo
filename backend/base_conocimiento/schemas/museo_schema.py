from utils.ma import ma
from marshmallow import fields
from models.museo import Museo

from schemas.distrito_schema import Distrito_Schema

class Museo_Schema(ma.Schema):
    class Meta:
        model = Museo
        fields = (
            'id_museo', 
            'nombre',
            'id_distrito',
            'direccion',
            'puntaje_resena',
            'ha_inicio',
            'ha_fin',
            'hc_inicio',
            'hc_fin',
            'tarifa_normal',
            'tarifa_ninos',
            'tarifa_ancianos',
            'tarifa_discapacitados',
            'reserva_entrada',
            'servicio_restaurante',
            'servicio_cafeteria',
            'servicio_guiado',
            'servicio_biblioteca',
            'venta_objetos',
            'accesibilidad',
            'permiso_foto',
            'estacionamiento',
            'visita_virtual',
            'n_restaurantes_prox',
            'n_atracciones_prox',
            'telefono',
            'anexo',
            'email',
            'sitio_web',
            'pag_facebook',
            'pag_instagram',
            'pag_tiktok',
            'notas',
            'distrito'
            )
        
    distrito = ma.Nested(Distrito_Schema)

museo_schema = Museo_Schema()
museos_schema = Museo_Schema(many=True)