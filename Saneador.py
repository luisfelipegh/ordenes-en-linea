from IValidador import IValidador


class Saneador(IValidador):
    def __init__(self):
        super().__init__()

    def ejecutar(self, orden):
        print("paso por el validador Saneador")
        orden.validadores.append("Saneador")
        return orden
