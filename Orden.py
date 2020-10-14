from Saneador import Saneador
from Repetidas import Repetidas
from Cache import Cache



class Orden:

    estado = ''
    validadores = []

    def __init__(self):
        self.estado = 'proceso'
        self.validadores = []

        pass

    def validarOrden(self, usuario):

        if not self.validarLogin(usuario):
            self.estado = 'sin login'
            return self
        orden = Cache().ejecutar(self)
        orden = Repetidas().ejecutar(orden)
        orden = Saneador().ejecutar(orden)
        orden.estado = 'finalizada'
        return orden

    def validarLogin(self, usuario):

        return usuario.perfil.nombre in ['admin','biller']