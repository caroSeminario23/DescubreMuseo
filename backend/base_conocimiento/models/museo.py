from utils.db import db
from sqlalchemy.orm import relationship

class Museo(db.Model):
    __tablename__ = 'museo'

    # Atributos
    id_museo = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    
    nombre = db.Column(
        db.String(200),
        nullable=False,
        unique=True
        )
    
    id_distrito = db.Column(
        db.Integer,
        db.ForeignKey('distrito.id_distrito'),
        nullable=False
        )
    
    direccion = db.Column(
        db.String(300),
        nullable=False
        )
    
    puntaje_resena = db.Column(
        db.Numeric(2, 1),
        nullable=False
        )
    
    ha_inicio = db.Column(
        db.Time,
        nullable=False
        )
    
    ha_fin = db.Column(
        db.Time,
        nullable=False
        )
    
    hc_inicio = db.Column(
        db.Time,
        nullable=True
        )
    
    hc_fin = db.Column(
        db.Time,
        nullable=True
        )
    
    tarifa_normal = db.Column(
        db.Numeric(5, 2),
        nullable=False
        )
    
    tarifa_ninos = db.Column(
        db.Numeric(5, 2),
        nullable=True
        )
    
    tarifa_ancianos = db.Column(
        db.Numeric(5, 2),
        nullable=True
        )
    
    tarifa_discapacitados = db.Column(
        db.Numeric(5, 2),
        nullable=True
        )
    
    reserva_entrada = db.Column(
        db.Boolean,
        nullable=False
        )
    
    servicio_restaurante = db.Column(
        db.Boolean,
        nullable=False
        )
    
    servicio_cafeteria = db.Column(
        db.Boolean,
        nullable=False
        )
    
    servicio_guiado = db.Column(
        db.Boolean,
        nullable=False
        )
    
    servicio_biblioteca = db.Column(
        db.Boolean,
        nullable=False
        )
    
    venta_objetos = db.Column(
        db.Boolean,
        nullable=False
        )
    
    accesibilidad = db.Column(
        db.Boolean,
        nullable=False
        )
    
    permiso_foto = db.Column(
        db.Boolean,
        nullable=False
        )
    
    estacionamiento = db.Column(
        db.Boolean,
        nullable=False
        )
    
    visita_virtual = db.Column(
        db.Boolean,
        nullable=False
        )
    
    n_restaurantes_prox = db.Column(
        db.Integer,
        nullable=True
        )
    
    n_atracciones_prox = db.Column(
        db.Integer,
        nullable=True
        )
    
    telefono = db.Column(
        db.String(9),
        nullable=True,
        unique=True
        )
    
    anexo = db.Column(
        db.String(5),
        nullable=True
        )
    
    email = db.Column(
        db.String(250),
        nullable=True,
        unique=True
        )
    
    sitio_web = db.Column(
        db.Text,
        nullable=True
        )
    
    pag_facebook = db.Column(
        db.Text,
        nullable=True
        )
    
    pag_instagram = db.Column(
        db.Text,
        nullable=True
        )
    
    pag_tiktok = db.Column(
        db.Text,
        nullable=True
        )
    
    notas = db.Column(
        db.Text,
        nullable=True
        )
    
    # Relaciones
    distrito = relationship(
        'Distrito', 
        back_ref='museo-distrito'
        )
    
    # Constructor
    def __init__(self,
        nombre,
        id_distrito,
        direccion,
        puntaje_resena,
        ha_inicio,
        ha_fin,
        hc_inicio,
        hc_fin,
        tarifa_normal,
        tarifa_ninos,
        tarifa_ancianos,
        tarifa_discapacitados,
        reserva_entrada,
        servicio_restaurante,
        servicio_cafeteria,
        servicio_guiado,
        servicio_biblioteca,
        venta_objetos,
        accesibilidad,
        permiso_foto,
        estacionamiento,
        visita_virtual,
        n_restaurantes_prox,
        n_atracciones_prox,
        telefono,
        anexo,
        email,
        sitio_web,
        pag_facebook,
        pag_instagram,
        pag_tiktok,
        notas):

        self.nombre = nombre
        self.id_distrito = id_distrito
        self.direccion = direccion
        self.puntaje_resena = puntaje_resena
        self.ha_inicio = ha_inicio
        self.ha_fin = ha_fin
        self.hc_inicio = hc_inicio
        self.hc_fin = hc_fin
        self.tarifa_normal = tarifa_normal
        self.tarifa_ninos = tarifa_ninos
        self.tarifa_ancianos = tarifa_ancianos
        self.tarifa_discapacitados = tarifa_discapacitados
        self.reserva_entrada = reserva_entrada
        self.servicio_restaurante = servicio_restaurante
        self.servicio_cafeteria = servicio_cafeteria
        self.servicio_guiado = servicio_guiado
        self.servicio_biblioteca = servicio_biblioteca
        self.venta_objetos = venta_objetos
        self.accesibilidad = accesibilidad
        self.permiso_foto = permiso_foto
        self.estacionamiento = estacionamiento
        self.visita_virtual = visita_virtual
        self.n_restaurantes_prox = n_restaurantes_prox
        self.n_atracciones_prox = n_atracciones_prox
        self.telefono = telefono
        self.anexo = anexo
        self.email = email
        self.sitio_web = sitio_web
        self.pag_facebook = pag_facebook
        self.pag_instagram = pag_instagram
        self.pag_tiktok = pag_tiktok
        self.notas = notas