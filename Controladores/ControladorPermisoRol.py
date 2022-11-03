from Modelos.PermisoRol import PermisoRol
from Modelos.Rol import Rol
from Modelos.Permiso import Permiso
from Repositorios.RepositorioPermisoRol import RepositorioPermisoRol
from Repositorios.RepositorioRol import RepositorioRol
from Repositorios.RepositorioPermiso import RepositorioPermiso
class ControladorPermisoRol():
    def __init__(self):
        self.repositorioPermisoRol = RepositorioPermisoRol()
        self.repositorioRol = RepositorioRol()
        self.repositorioPermiso = RepositorioPermiso()
    def index(self):
        return self.repositorioPermisoRol.findAll()
    """
    Asignacion estudiante y materia a inscripción
    """
    def create(self,infoPermisoRol,id_rol,id_permiso):
        nuevoPermisoRol=PermisoRol(infoPermisoRol)
        elRol=Rol(self.repositorioRol.findById(id_rol))
        elPermiso=Permiso(self.repositorioPermiso.findById(id_permiso))
        nuevoPermisoRol.rol=elRol
        nuevoPermisoRol.permiso=elPermiso
        return self.repositorioPermisoRol.save(nuevoPermisoRol)
    def show(self,id):
        elPermisoRol=PermisoRol(self.repositorioPermisoRol.findById(id))
        return elPermisoRol.__dict__
    """
    Modificación de inscripción (estudiante y materia)
    """
    def update(self,id,id_rol,id_permiso):
        elPermisoRol=PermisoRol(self.repositorioPermisoRol.findById(id))
        elRol = Rol(self.repositorioRol.findById(id_rol))
        elPermiso = Permiso(self.repositorioPermiso.findById(id_permiso))
        elPermisoRol.rol = elRol
        elPermisoRol.permiso = elPermiso
        return self.repositorioPermisoRol.save(elPermisoRol)
    def delete(self, id):
        return self.repositorioPermisoRol.delete(id)
    "Obtener todos los inscritos en una materia"
    def listarPermisoRol(self,id_permiso):
        return self.repositorioPermisoRol.getListadoPermisoRol(id_permiso)