class Ingreso:

    def __init__(self, usuario):
        self.usuario = usuario

    def validarIngreso(self):
        return self.usuario.perfil.nombre in ['admin', 'biller']