from Saneador import Saneador
from Repetidas import Repetidas
from Cache import Cache
from Ingreso import Ingreso



class Orden:

    estado = ''
    validadores = []

    def __init__(self):
        self.estado = 'proceso'
        self.validadores = []

        pass

    def validarOrden(self, usuario):
        ingreso = Ingreso(usuario)

        if not ingreso.validarIngreso():
            self.estado = 'sin login'
            return self

        orden = Cache().ejecutar(self)
        orden = Repetidas().ejecutar(orden)
        orden = Saneador().ejecutar(orden)
        orden.estado = 'finalizada'

        return orden