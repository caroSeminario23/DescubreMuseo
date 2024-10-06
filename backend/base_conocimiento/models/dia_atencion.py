from utils.db import db
from sqlalchemy.orm import relationship

class DiaAtencion(db.Model):
    __tablename__ = "dia_atencion"

    # Atributos
    id_museo = db.Column(
        db.Integer,
        db.ForeignKey('museo.id_museo'),
        primary_key=True,
        nullable=False
        )
    
    id_dia = db.Column(
        db.Integer,
        db.ForeignKey('dia.id_dia'),
        primary_key=True,
        nullable=False
        )
    
    # Relaciones
    museo = db.relationship(
        'Museo',
        backref='dia_atencion-museo'
        )
    
    dia = db.relationship(
        'Dia',
        backref='dia_atencion-dia'
        )
    
    # Constructor
    def __init__(self, 
                 id_museo, 
                 id_dia):
        
        self.id_museo = id_museo
        self.id_dia = id_dia