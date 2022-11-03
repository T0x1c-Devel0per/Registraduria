from Repositorios.RepositorioRol import RepositorioRol
from Modelos.Rol import Rol
class ControladorRol():
    def __init__(self):
        self.repositorioRol = RepositorioRol()
    def index(self):
        return self.repositorioRol.findAll()
    def create(self, infoRol):
        nuevoRol = Rol(infoRol)
        return self.repositorioRol.save(nuevoRol)
    def show(self, id):
        elRol = Rol(self.repositorioRol.findById(id))
        return elRol.__dict__
    def update(self, id, infoRol):
        rolActual = Rol(self.repositorioRol.findById(id))
        rolActual.nombreRol = infoRol["nombrerol"]
        return self.repositorioRol.save(rolActual)
    def delete(self, id):
        return self.repositorioRol.delete(id)
