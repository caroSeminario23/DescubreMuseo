from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.distrito import Distrito
from schemas.distrito_schema import distrito_schema, distritos_schema

distrito_routes = Blueprint("distrito_routes", __name__)

@distrito_routes.route('/create_distrito', methods=['POST'])
def create_distrito():
    nombre = request.json.get('nombre')

    new_distrito = Distrito(nombre=nombre)

    db.session.add(new_distrito)
    db.session.commit()

    result = distrito_schema.dump(new_distrito)

    data = {
        'message': 'Distrito creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@distrito_routes.route('/get_distritos', methods=['GET'])
def get_distritos():
    distritos = Distrito.query.all()

    if not distritos:
        data = {
            'message': 'No hay distritos registrados',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = distritos_schema.dump(distritos)

    data = {
        'message': 'Distritos obtenidos correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@distrito_routes.route('/get_distrito/<int:id_distrito>', methods=['GET'])
def get_distrito(id_distrito):
    distrito = Distrito.query.get(id_distrito)

    if not distrito:
        data = {
            'message': 'Distrito no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = distrito_schema.dump(distrito)

    data = {
        'message': 'Distrito obtenido correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@distrito_routes.route('/update_distrito/<int:id_distrito>', methods=['PUT'])
def update_distrito(id_distrito):
    distrito = Distrito.query.get(id_distrito)

    if not distrito:
        data = {
            'message': 'Distrito no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')

    distrito.nombre = nombre

    db.session.commit()

    result = distrito_schema.dump(distrito)

    data = {
        'message': 'Distrito actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@distrito_routes.route('/delete_distrito/<int:id_distrito>', methods=['DELETE'])
def delete_distrito(id_distrito):
    distrito = Distrito.query.get(id_distrito)

    if not distrito:
        data = {
            'message': 'Distrito no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(distrito)
    db.session.commit()

    data = {
        'message': 'Distrito eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)