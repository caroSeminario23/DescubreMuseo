from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.dia_concurrido import DiaConcurrido
from schemas.dia_concurrido_schema import dia_concurrido_schema, dias_concurridos_schema

dia_concurrido_routes = Blueprint("dia_concurrido_routes", __name__)

@dia_concurrido_routes.route("/create_dia_concurrido", methods=["POST"])
def create_dia_concurrido():
    id_museo = request.json.get('id_musea')
    id_dia = request.json.get('id_dia')

    new_dia_concurrido = DiaConcurrido(
        id_museo=id_museo,
        id_dia=id_dia
        )
    db.session.add(new_dia_concurrido)
    db.session.commit()

    result = dia_concurrido_schema.dump(new_dia_concurrido)

    data = {
        'message': 'Dia concurrido creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@dia_concurrido_routes.route("/get_dias_concurrido", methods=["GET"])
def get_dias_concurrido():
    dias_concurrido = DiaConcurrido.query.all()

    if not dias_concurrido:
        data = {
            'message': 'No se encontraron dias concurridos registrados',
            'status': 404,
        }

        return make_response(jsonify(data), 404)


    result = dias_concurridos_schema.dump(dias_concurrido)

    data = {
        'message': 'Dias concurridos obtenidos correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@dia_concurrido_routes.route("/get_dia_concurrido/<int:id_museo>/<int:id_dia>", methods=["GET"])
def get_dia_concurrido(id_museo, id_dia):
    dia_concurrido = DiaConcurrido.query.filter_by(id_museo=id_museo, id_dia=id_dia).first()

    if not dia_concurrido:
        data = {
            'message': 'Dia concurrido no encontrado',
            'status': 404,
        }

        return make_response(jsonify(data), 404)

    result = dia_concurrido_schema.dump(dia_concurrido)

    data = {
        'message': 'Dia concurrido obtenido correctamente',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data), 200)

@dia_concurrido_routes.route("/delete_dia_concurrido/<int:id_museo>/<int_id_dia>", methods=["DELETE"])
def delete_dia_concurrido(id_museo, id_dia):
    dia_concurrido = DiaConcurrido.query_by(id_museo=id_museo, id_dia=id_dia).first()

    if not dia_concurrido:
        data = {
            'message': 'Dia concurrido no encontrado',
            'status': 404,
        }

        return make_response(jsonify(data), 404)

    db.session.delete(dia_concurrido)
    db.session.commit()

    data = {
        'message': 'Dia concurrido eliminado correctamente',
        'status': 200,
    }

    return make_response(jsonify(data), 200)


