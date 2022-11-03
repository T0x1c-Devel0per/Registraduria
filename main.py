from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorUsuario import ControladorUsuario
from Controladores.ControladorRol import ControladorRol
from Controladores.ControladorPermiso import ControladorPermiso
from Controladores.ControladorPermisoRol import ControladorPermisoRol
miControladorUsuario = ControladorUsuario()
miControladorRol = ControladorRol()
miControladorPermiso = ControladorPermiso()
miControladorPermisoRol = ControladorPermisoRol()

@app.route("/", methods=['GET'])
def test():
    json = {}
    json["message"] = "Server running ..."
    return jsonify(json)


@app.route("/usuarios", methods=['GET'])
def getUsuarios():
    json = miControladorUsuario.index()
    return jsonify(json)


@app.route("/usuarios", methods=['POST'])
def crearUsuario():
    data = request.get_json()
    json = miControladorUsuario.create(data)
    return jsonify(json)


@app.route("/usuarioss/<string:id>", methods=['GET'])
def getUsuario(id):
    json = miControladorUsuario.show(id)
    return jsonify(json)


@app.route("/usuarios/<string:id>", methods=['PUT'])
def modificarUsuario(id):
    data = request.get_json()
    json = miControladorUsuario.update(id, data)
    return jsonify(json)


@app.route("/usuarios/<string:id>", methods=['DELETE'])
def eliminarUsuario(id):
    json = miControladorUsuario.delete(id)
    return jsonify(json)
@app.route("/usuarios/<string:id>/rol/<string:id_rol>",methods=['PUT'])
def asignarRolAUsuario(id,id_rol):
    json=miControladorUsuario.asignarRol(id,id_rol)
    return jsonify(json)

########################################################################################################################

@app.route("/rol", methods=['GET'])
def getRoles():
    json = miControladorRol.index()
    return jsonify(json)


@app.route("/rol", methods=['POST'])
def crearRol():
    data = request.get_json()
    json = miControladorRol.create(data)
    return jsonify(json)


@app.route("/rol/<string:id>", methods=['GET'])
def getRol(id):
    json = miControladorRol.show(id)
    return jsonify(json)


@app.route("/rol/<string:id>", methods=['PUT'])
def modificarRol(id):
    data = request.get_json()
    json = miControladorRol.update(id, data)
    return jsonify(json)


@app.route("/rol/<string:id>", methods=['DELETE'])
def eliminarRol(id):
    json = miControladorRol.delete(id)
    return jsonify(json)
########################################################################################################################

@app.route("/permiso", methods=['GET'])
def getPermisos():
    json = miControladorPermiso.index()
    return jsonify(json)


@app.route("/permiso", methods=['POST'])
def crearPermiso():
    data = request.get_json()
    json = miControladorPermiso.create(data)
    return jsonify(json)


@app.route("/permiso/<string:id>", methods=['GET'])
def getPermiso(id):
    json = miControladorPermiso.show(id)
    return jsonify(json)


@app.route("/permiso/<string:id>", methods=['PUT'])
def modificarPermiso(id):
    data = request.get_json()
    json = miControladorPermiso.update(id, data)
    return jsonify(json)


@app.route("/permiso/<string:id>", methods=['DELETE'])
def eliminarPermiso(id):
    json = miControladorPermiso.delete(id)
    return jsonify(json)


########################################################################################################################
@app.route("/permisoRol",methods=['GET'])
def getPermisosRoles():
    json=miControladorPermisoRol.index()
    return jsonify(json)
@app.route("/permisoRol/<string:id>",methods=['GET'])
def getPermisoRol(id):
    json=miControladorPermisoRol.show(id)
    return jsonify(json)
@app.route("/permisoRol/rol/<string:id_rol>/permiso/<string:id_permiso>",methods=['POST'])
def crearPermisosRol(id_rol,id_permiso):
    data = request.get_json()
    json=miControladorPermisoRol.create(data,id_rol,id_permiso)
    return jsonify(json)
@app.route("/permisoRol/<string:id_permisoRol>/rol/<string:id_rol>/permiso/<string:id_permiso>",methods=['PUT'])
def modificarPermisosRol(id_permisoRol,id_rol,id_permiso):
    data = request.get_json()
    json=miControladorPermisoRol.update(id_permisoRol,data,id_rol,id_permiso)
    return jsonify(json)
@app.route("/permisoRol/<string:id_permisoRol>",methods=['DELETE'])
def eliminarPermisosRol(id_permisoRol):
    json=miControladorPermisoRol.delete(id_permisoRol)
    return jsonify(json)
@app.route("/permisoRol/permiso/<string:id_permiso>",methods=['GET'])
def permisos(id_permiso):
    json=miControladorPermisoRol.listarPermisoRol(id_permiso)
    return jsonify(json)
########################################################################################################################
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : " + "http://" + dataConfig["url-backend"] + ":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])
