from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.PermisoRol import PermisoRol

from bson import ObjectId

class RepositorioPermisoRol(InterfaceRepositorio[PermisoRol]):
    def getListadoPermisoRol(self, id_permiso):
        theQuery = {"permiso.$id": ObjectId(id_permiso)}
        return self.query(theQuery)
