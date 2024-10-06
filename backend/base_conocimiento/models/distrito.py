from utils.db import db

class Distrito(db.Model):
    __tablename__ = "distrito"

    # Atributos
    id_distrito = db.Column(
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