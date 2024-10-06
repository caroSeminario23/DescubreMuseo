from utils.db import db

class Dia(db.Model):
    __tablename__ = "dia"

    # Atributos
    id_dia = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    
    nombre = db.Column(
        db.String(20),
        nullable=False,
        unique=True
        )
    
    # Constructor
    def __init__(self, 
                 nombre):
        
        self.nombre = nombre