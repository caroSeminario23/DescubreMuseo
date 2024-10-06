from utils.db import db
from sqlalchemy.orm import relationship

class CategoriaMuseo(db.Model):
    __tablename__ = 'categoria_museo'

    # Atributos
    id_categoria = db.Column(
        db.Integer,
        db.ForeignKey('categoria.id_categoria'),
        primary_key=True,
        nullable=False
        )
    
    id_museo = db.Column(
        db.Integer,
        db.ForeignKey('museo.id_museo'),
        primary_key=True,
        nullable=False
        )
    
    # Relaciones
    categoria = relationship(
        'Categoria',
        backref='categoria_museo-categoria'
        )
    
    museo = relationship(
        'Museo',
        backref='categoria_museo-museo'
        )
    
    # Constructor
    def __init__(self, 
                 id_categoria, 
                 id_museo):
        
        self.id_categoria = id_categoria
        self.id_museo = id_museo