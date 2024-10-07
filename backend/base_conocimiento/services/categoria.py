from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.categoria import Categoria
from schemas.categoria_schema import categoria_schema, categorias_schema

categoria_routes = Blueprint("categoria_routes", __name__)

@categoria_routes.route("/create_categoria", methods=["POST"])
def create_categoria():
    nombre = request.json.get('nombre')

    new_categoria = Categoria(nombre=nombre)

    db.session.add(new_categoria)
    db.session.commit()

    result = categoria_schema.dump(new_categoria)

    data = {
        "message": "Categoria creada exitosamente",
        'status': 201,
        'data': result
        }
    
    return make_response(jsonify(data), 201)

@categoria_routes.route("/get_categorias", methods=["GET"])
def get_categorias():
    categorias = Categoria.query.all()
    
    if not categorias:
        data = {
            'message': 'No hay categorias registradas',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = categorias_schema.dump(categorias)

    data = {
        'message': 'Categorias encontradas correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)

@categoria_routes.route("/get_categoria/<int:id_categoria>", methods=["GET"])
def get_categoria(id_categoria):
    categoria = Categoria.query.get(id_categoria)

    if not categoria:
        data = {
            'message': 'Categoria no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    result = categoria_schema.dump(categoria)

    data = {
        'message': 'Categoria encontrada correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)
@categoria_routes.route("/update_categoria/<int:id_categoria>", methods=["PUT"])
def update_categoria(id_categoria):
    categoria = Categoria.query.get(id_categoria)

    if not categoria:
        data = {
            'message': 'Categoria no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')

    categoria.nombre = nombre

    db.session.commit()

    result = categoria_schema.dump(categoria)

    data = {
        'message': 'Categoria actualizada correctamente',
        'status': 200,
        'data': result
    }
    
    return make_response(jsonify(data), 200)
@categoria_routes.route("/delete_categoria/<int:id_categoria>", methods=["DELETE"])
def delete_categoria(id_categoria):
    categoria = Categoria.query.get(id_categoria)

    if not categoria:
        data = {
            'message': 'Categoria no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)
    
    db.session.delete(categoria)
    db.session.commit()

    data = {
        'message': 'Categoria eliminada correctamente',
        'status': 200
    }
    
    return make_response(jsonify(data), 200)
    