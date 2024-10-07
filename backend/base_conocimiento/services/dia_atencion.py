from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.dia_atencion import DiaAtencion
from schemas.dia_atencion_schema import dia_atencion_schema, dias_atencion_schema

dia_atencion_routes = Blueprint("dia_atencion_routes", __name__)

@dia_atencion_routes.route('/create_dia_atencion', methods=['POST'])
def create_dia_atencion():
    id_museo = request.json.get('id_museo')
    id_dia = request.json.get('id_dia')

    new_dia_atencion = DiaAtencion(
        id_museo=id_museo,
        id_dia=id_dia
    )

    db.session.add(new_dia_atencion)
    db.session.commit()

    result = dia_atencion_schema.dump(new_dia_atencion)

    data = {
        'message': 'Día de atención creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@dia_atencion_routes.route('/get_dias_atencion', methods=['GET'])
def get_dias_atencion():
    dias_atencion = DiaAtencion.query.all()

    if not dias_atencion:
        data = {
            'message': 'No hay días de atención registrados',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = dias_atencion_schema.dump(dias_atencion)

    data = {
        'message': 'Días de atención obtenidos correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@dia_atencion_routes.route('/get_dia_atencion/<int:id_museo>/<int:id_dia>', methods=['GET'])
def get_dia_atencion(id_museo, id_dia):
    dia_atencion = DiaAtencion.query.filter_by(id_museo=id_museo, id_dia=id_dia).first()

    if not dia_atencion:
        data = {
            'message': 'Día de atención no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = dia_atencion_schema.dump(dia_atencion)

    data = {
        'message': 'Día de atención obtenido correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@dia_atencion_routes.route('/delete_dia_atencion/<int:id_museo>/<int:id_dia>', methods=['DELETE'])
def delete_dia_atencion(id_museo, id_dia):
    dia_atencion = DiaAtencion.query.filter_by(id_museo=id_museo, id_dia=id_dia).first()

    if not dia_atencion:
        data = {
            'message': 'Día de atención no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    db.session.delete(dia_atencion)
    db.session.commit()

    data = {
        'message': 'Día de atención eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)