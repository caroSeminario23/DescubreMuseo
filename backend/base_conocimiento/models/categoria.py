from utils.db import db

class Categoria(db.Model):
    __tablename__ = "categoria"

    # Atributos
    id_categoria = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    
    nombre = db.Column(
        db.String(50),
        nullable=False,
        unique=True
        )
    
    # Constructor
    def __init__(self, 
                 nombre):
        
        self.nombre = nombre