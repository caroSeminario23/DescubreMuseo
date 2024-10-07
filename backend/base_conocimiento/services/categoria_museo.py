from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.categoria_museo import CategoriaMuseo
from schemas.categoria_museo_schema import categoria_museo_schema, categorias_museo_schema

categoria_museo_routes = Blueprint("categoria_museo_routes", __name__)

@categoria_museo_routes.route("/create_categoria_museo", methods=["POST"])
def create_categoria_museo():
    id_categoria = request.json.get('id_categoria')
    id_museo = request.json.get('id_museo')

    new_categoria_museo = CategoriaMuseo(
        id_categoria=id_categoria,
        id_museo=id_museo
    )

    db.session.add(new_categoria_museo)
    db.session.commit()

    result = categoria_museo_schema.dump(new_categoria_museo)

    data = {
        'message': 'Categoria de museo creada correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@categoria_museo_routes.route("/get_categorias_museo", methods=["GET"])
def get_categorias_museo():
    categorias_museo = CategoriaMuseo.query.all()

    if not categorias_museo:
        data = {
            'message': 'No hay categorias de museo registradas',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = categorias_museo_schema.dump(categorias_museo)

    data = {
        'message': 'Categorias de museo obtenidas correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@categoria_museo_routes.route("/get_categoria_museo/<int:id_categoria>/<int:id_museo>", methods=["GET"])
def get_categoria_museo(id_categoria, id_museo):
    categoria_museo = CategoriaMuseo.query.filter_by(id_categoria=id_categoria, id_museo=id_museo).first()

    if not categoria_museo:
        data = {
            'message': 'Categoria de museo no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = categoria_museo_schema.dump(categoria_museo)

    data = {
        'message': 'Categoria de museo obtenida correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@categoria_museo_routes.route("/delete_categoria_museo/<int:id_categoria>/<int:id_museo>", methods=["DELETE"])
def delete_categoria_museo(id_categoria, id_museo):
    categoria_museo = CategoriaMuseo.query.filter_by(id_categoria=id_categoria, id_museo=id_museo).first()

    if not categoria_museo:
        data = {
            'message': 'Categoria de museo no encontrada',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(categoria_museo)
    db.session.commit()

    data = {
        'message': 'Categoria de museo eliminada correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)