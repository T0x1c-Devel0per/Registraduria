from Repositorios.RepositorioUsuario import RepositorioUsuario
from Repositorios.RepositorioRol import RepositorioRol
from Modelos.Usuario import Usuario
from Modelos.Rol import Rol
class ControladorUsuario():
    def __init__(self):
        self.repositorioUsuario = RepositorioUsuario()
        self.repositorioRol = RepositorioRol()
    def index(self):
        return self.repositorioUsuario.findAll()
    def create(self, infoUsuario):
        nuevoUsuario = Usuario(infoUsuario)
        return self.repositorioUsuario.save(nuevoUsuario)
    def show(self, id):
        elUsuario = Usuario(self.repositorioUsuario.findById(id))
        return elUsuario.__dict__
    def update(self, id, infoUsuario):
        usuarioActual = Usuario(self.repositorioUsuario.findById(id))
        usuarioActual.nombreUsuario = infoUsuario["nombreUsuario"]
        usuarioActual.correo = infoUsuario["correo"]
        usuarioActual.contraseña = infoUsuario["contraseña"]
        return self.repositorioUsuario.save(usuarioActual)
    def delete(self, id):
        return self.repositorioUsuario.delete(id)
    """
       Relación Rol y Usuario
    """
    def asignarRol(self, id, id_rol):
        usuarioActual = Usuario(self.repositorioUsuario.findById(id))
        rolActual = Rol(self.repositorioRol.findById(id_rol))
        usuarioActual.rol = rolActual
        return self.repositorioUsuario.save(usuarioActual)