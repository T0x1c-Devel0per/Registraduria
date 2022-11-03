from Repositorios.RepositorioPermiso import RepositorioPermiso
from Modelos.Permiso import Permiso
class ControladorPermiso():
    def __init__(self):
        self.repositorioPermiso = RepositorioPermiso()
    def index(self):
        return self.repositorioPermiso.findAll()
    def create(self, infoPermiso):
        nuevoPermiso = Permiso(infoPermiso)
        return self.repositorioPermiso.save(nuevoPermiso)
    def show(self, id):
        elPermiso = Permiso(self.repositorioPermiso.findById(id))
        return elPermiso.__dict__
    def update(self, id, infoPermiso):
        permisoActual = Permiso(self.repositorioPermiso.findById(id))
        permisoActual.urlPermiso = infoPermiso["urlPermiso"]
        permisoActual.metodoPermiso = infoPermiso["metodoPermiso"]
        return self.repositorioPermiso.save(permisoActual)
    def delete(self, id):
        return self.repositorioPermiso.delete(id)
