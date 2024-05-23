from flask import Blueprint, request, jsonify
from model.BotonEmergencia import BotonEmergencia
from utils.db import db

boton_emergencia_blueprint = Blueprint('BotonEmergencia', __name__)

@boton_emergencia_blueprint.route('/BotonEmergencia/v1', methods=['GET'])
def getMensaje():
    result = {}
    result["data"] = 'flask-crud-backend'
    return jsonify(result)

@boton_emergencia_blueprint.route('/BotonEmergencia/v1/listar', methods=['GET'])
def getBotonEmergencia():
    result = {}
    boton_emergencia = BotonEmergencia.query.all()
    result["data"] = boton_emergencia
    result["status_code"] = 200
    result["msg"] = "Se recuperaron los botones de emergencia sin inconvenientes"
    return jsonify(result), 200

@boton_emergencia_blueprint.route('/BotonEmergencia/v1/insert', methods=['POST'])
def insert():
    result = {}
    body = request.get_json()
    nombres = body.get('nombres')
    apellidos = body.get('apellidos')
    telefono = body.get('telefono')
    direccion = body.get('direccion')
    correo = body.get('correo')
    test_puntuacion = body.get('test_puntuacion')
    
    if not nombres or not apellidos or not telefono or not direccion or not correo or not test_puntuacion:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    boton_emergencia = BotonEmergencia(nombres, apellidos, telefono, direccion, correo, test_puntuacion)
    db.session.add(boton_emergencia)
    db.session.commit()
    result["data"] = boton_emergencia
    result["status_code"] = 201
    result["msg"] = "Se agregó el botón de emergencia"
    return jsonify(result), 201

@boton_emergencia_blueprint.route('/BotonEmergencia/v1/update', methods=['POST'])
def update():
    result = {}
    body = request.get_json()
    id_boton_emergencia = body.get('id_boton_emergencia')
    nombres = body.get('nombres')
    apellidos = body.get('apellidos')
    telefono = body.get('telefono')
    direccion = body.get('direccion')
    correo = body.get('correo')
    test_puntuacion = body.get('test_puntuacion')
    
    if not id_boton_emergencia or not nombres or not apellidos or not telefono or not direccion or not correo or not test_puntuacion:
        result["status_code"] = 400
        result["msg"] = "Faltan datos"
        return jsonify(result), 400
    
    boton_emergencia = BotonEmergencia.query.get(id_boton_emergencia)
    if not boton_emergencia:
        result["status_code"] = 400
        result["msg"] = "Botón de emergencia no existe"
        return jsonify(result), 400
    
    boton_emergencia.nombres = nombres
    boton_emergencia.apellidos = apellidos
    boton_emergencia.telefono = telefono
    boton_emergencia.direccion = direccion
    boton_emergencia.correo = correo
    boton_emergencia.test_puntuacion = test_puntuacion
    db.session.commit()
    
    result["data"] = boton_emergencia
    result["status_code"] = 202
    result["msg"] = "Se modificó el botón de emergencia"
    return jsonify(result), 202

@boton_emergencia_blueprint.route('/BotonEmergencia/v1/delete', methods=['DELETE'])
def delete():
    result = {}
    body = request.get_json()
    id_boton_emergencia = body.get('id_boton_emergencia')    
    if not id_boton_emergencia:
        result["status_code"] = 400
        result["msg"] = "Debe consignar un id válido"
        return jsonify(result), 400
    
    boton_emergencia = BotonEmergencia.query.get(id_boton_emergencia)
    if not boton_emergencia:
        result["status_code"] = 400
        result["msg"] = "Botón de emergencia no existe"
        return jsonify(result), 400
    
    db.session.delete(boton_emergencia)
    db.session.commit()
    
    result["data"] = boton_emergencia
    result["status_code"] = 200
    result["msg"] = "Se eliminó el botón de emergencia"
    return jsonify(result), 200