from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.museo import Museo
from schemas.museo_schema import museo_schema, museos_schema

museo_routes = Blueprint("museo_routes", __name__)

@museo_routes.route('/create_museo', methods=['POST'])
def create_museo():
    nombre = request.json.get('nombre')
    id_distrito = request.json.get('id_distrito')
    direccion = request.json.get('direccion')
    puntaje_reseña = request.json.get('puntaje_reseña')
    ha_inicio = request.json.get('ha_inicio')
    ha_fin = request.json.get('ha_fin')
    hc_inicio = request.json.get('hc_inicio')
    hc_fin = request.json.get('hc_fin')
    tarifa_normal = request.json.get('tarifa_normal')
    tarifa_niños = request.json.get('tarifa_niños')
    tarifa_ancianos = request.json.get('tarifa_ancianos')
    tarifa_discapacitados = request.json.get('tarifa_discapacitados')
    reserva_entrada = request.json.get('reserva_entrada')
    servicio_restaurante = request.json.get('servicio_restaurante')
    servicio_cafeteria = request.json.get('servicio_cafeteria')
    servicio_guiado = request.json.get('servicio_guiado')
    servicio_biblioteca = request.json.get('servicio_biblioteca')
    venta_objetos = request.json.get('venta_objetos')
    accesibilidad = request.json.get('accesibilidad')
    permiso_foto = request.json.get('permiso_foto')
    estacionamiento = request.json.get('estacionamiento')
    visita_virtual = request.json.get('visita_virtual')
    n_restaurantes_prox = request.json.get('n_restaurantes_prox')
    n_atracciones_prox = request.json.get('n_atracciones_prox')
    telefono = request.json.get('telefono')
    anexo = request.json.get('anexo')
    email = request.json.get('email')
    sitio_web = request.json.get('sitio_web')
    pag_facebook = request.json.get('pag_facebook')
    pag_instagram = request.json.get('pag_instagram')
    pag_tiktok = request.json.get('pag_tiktok')
    notas = request.json.get('notas')

    new_museo = Museo(
        nombre=nombre,
        id_distrito=id_distrito,
        direccion=direccion,
        puntaje_reseña=puntaje_reseña,
        ha_inicio=ha_inicio,
        ha_fin=ha_fin,
        hc_inicio=hc_inicio,
        hc_fin=hc_fin,
        tarifa_normal=tarifa_normal,
        tarifa_niños=tarifa_niños,
        tarifa_ancianos=tarifa_ancianos,
        tarifa_discapacitados=tarifa_discapacitados,
        reserva_entrada=reserva_entrada,
        servicio_restaurante=servicio_restaurante,
        servicio_cafeteria=servicio_cafeteria,
        servicio_guiado=servicio_guiado,
        servicio_biblioteca=servicio_biblioteca,
        venta_objetos=venta_objetos,
        accesibilidad=accesibilidad,
        permiso_foto=permiso_foto,
        estacionamiento=estacionamiento,
        visita_virtual=visita_virtual,
        n_restaurantes_prox=n_restaurantes_prox,
        n_atracciones_prox=n_atracciones_prox,
        telefono=telefono,
        anexo=anexo,
        email=email,
        sitio_web=sitio_web,
        pag_facebook=pag_facebook,
        pag_instagram=pag_instagram,
        pag_tiktok=pag_tiktok,
        notas=notas
    )

    db.session.add(new_museo)
    db.session.commit()

    result = museo_schema.dump(new_museo)

    data = {
        'message': 'Museo creado correctamente',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@museo_routes.route('/get_museos', methods=['GET'])
def get_museos():
    museos = Museo.query.all()

    if not museos:
        data = {
            'message': 'No hay museos registrados',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = museos_schema.dump(museos)

    data = {
        'message': 'Museos obtenidos correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@museo_routes.route('/get_museo/<int:id_museo>', methods=['GET'])
def get_museo(id_museo):
    museo = Museo.query.get(id_museo)

    if not museo:
        data = {
            'message': 'Museo no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)
    
    result = museo_schema.dump(museo)

    data = {
        'message': 'Museo obtenido correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@museo_routes.route('/update_museo/<int:id_museo>', methods=['PUT'])
def update_museo(id_museo):
    museo = Museo.query.get(id_museo)

    if not museo:
        data = {
            'message': 'Museo no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    id_distrito = request.json.get('id_distrito')
    direccion = request.json.get('direccion')
    puntaje_reseña = request.json.get('puntaje_reseña')
    ha_inicio = request.json.get('ha_inicio')
    ha_fin = request.json.get('ha_fin')
    hc_inicio = request.json.get('hc_inicio')
    hc_fin = request.json.get('hc_fin')
    tarifa_normal = request.json.get('tarifa_normal')
    tarifa_niños = request.json.get('tarifa_niños')
    tarifa_ancianos = request.json.get('tarifa_ancianos')
    tarifa_discapacitados = request.json.get('tarifa_discapacitados')
    reserva_entrada = request.json.get('reserva_entrada')
    servicio_restaurante = request.json.get('servicio_restaurante')
    servicio_cafeteria = request.json.get('servicio_cafeteria')
    servicio_guiado = request.json.get('servicio_guiado')
    servicio_biblioteca = request.json.get('servicio_biblioteca')
    venta_objetos = request.json.get('venta_objetos')
    accesibilidad = request.json.get('accesibilidad')
    permiso_foto = request.json.get('permiso_foto')
    estacionamiento = request.json.get('estacionamiento')
    visita_virtual = request.json.get('visita_virtual')
    n_restaurantes_prox = request.json.get('n_restaurantes_prox')
    n_atracciones_prox = request.json.get('n_atracciones_prox')
    telefono = request.json.get('telefono')
    anexo = request.json.get('anexo')
    email = request.json.get('email')
    sitio_web = request.json.get('sitio_web')
    pag_facebook = request.json.get('pag_facebook')
    pag_instagram = request.json.get('pag_instagram')
    pag_tiktok = request.json.get('pag_tiktok')
    notas = request.json.get('notas')

    museo.nombre = nombre
    museo.id_distrito = id_distrito
    museo.direccion = direccion
    museo.puntaje_reseña = puntaje_reseña
    museo.ha_inicio = ha_inicio
    museo.ha_fin = ha_fin
    museo.hc_inicio = hc_inicio
    museo.hc_fin = hc_fin
    museo.tarifa_normal = tarifa_normal
    museo.tarifa_niños = tarifa_niños
    museo.tarifa_ancianos = tarifa_ancianos
    museo.tarifa_discapacitados = tarifa_discapacitados
    museo.reserva_entrada = reserva_entrada
    museo.servicio_restaurante = servicio_restaurante
    museo.servicio_cafeteria = servicio_cafeteria
    museo.servicio_guiado = servicio_guiado
    museo.servicio_biblioteca = servicio_biblioteca
    museo.venta_objetos = venta_objetos
    museo.accesibilidad = accesibilidad
    museo.permiso_foto = permiso_foto
    museo.estacionamiento = estacionamiento
    museo.visita_virtual = visita_virtual
    museo.n_restaurantes_prox = n_restaurantes_prox
    museo.n_atracciones_prox = n_atracciones_prox
    museo.telefono = telefono
    museo.anexo = anexo
    museo.email = email
    museo.sitio_web = sitio_web
    museo.pag_facebook = pag_facebook
    museo.pag_instagram = pag_instagram
    museo.pag_tiktok = pag_tiktok
    museo.notas = notas

    db.session.commit()

    result = museo_schema.dump(museo)

    data = {
        'message': 'Museo actualizado correctamente',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@museo_routes.route('/delete_museo/<int:id_museo>', methods=['DELETE'])
def delete_museo(id_museo):
    museo = Museo.query.get(id_museo)

    if not museo:
        data = {
            'message': 'Museo no encontrado',
            'status': 404
        }

        return make_response(jsonify(data), 404)

    db.session.delete(museo)
    db.session.commit()

    data = {
        'message': 'Museo eliminado correctamente',
        'status': 200
    }

    return make_response(jsonify(data), 200)