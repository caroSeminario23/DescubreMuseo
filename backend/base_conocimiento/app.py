from flask import Flask
from flask_cors import CORS
from utils.db import db

from services.distrito import distrito_routes
from services.dia import dia_routes
from services.categoria import categoria_routes
from services.museo import museo_routes
from services.categoria_museo import categoria_museo_routes
from services.dia_atencion import dia_atencion_routes
from services.dia_concurrido import dia_concurrido_routes

from flask_sqlalchemy import SQLAlchemy
from config import DATABASE_CONNECTION

# Crear la aplicación
app = Flask(__name__)

# Configurar CORS para la aplicación
CORS(
    app,
    origins=['http://localhost:4200'],
    methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=['Content-Type', 'Authorization']
)

# Configurar la aplicación
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION

# Inicializar la base de datos
db.init_app(app)

# Registrar los blueprints
app.register_blueprint(distrito_routes, url_prefix='/distrito_routes')
app.register_blueprint(dia_routes, url_prefix='/dia_routes')
app.register_blueprint(categoria_routes, url_prefix='/categoria_routes')
app.register_blueprint(museo_routes, url_prefix='/museo_routes')
app.register_blueprint(categoria_museo_routes, url_prefix='/categoria_museo_routes')
app.register_blueprint(dia_atencion_routes, url_prefix='/dia_atencion_routes')
app.register_blueprint(dia_concurrido_routes, url_prefix='/dia_concurrido_routes')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        port=5000
        )