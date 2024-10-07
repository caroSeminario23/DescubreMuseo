from flask import Flask
from flask_cors import CORS
from utils.db import db
from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

# Crear la aplicación
app = Flask(__name__)

CORS(
    app,
    origins=['http://localhost:4200'],
    methods=['GET', 'POST', 'PUT', 'DELETE']
    allow_headers=['Content-Type', 'Authorization']
)

# Configurar la aplicación