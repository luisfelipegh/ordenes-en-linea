from IValidador import IValidador


class Repetidas(IValidador):
    def __init__(self):
        super().__init__()

    def ejecutar(self, orden):
        print("paso por el validador repetidas")
        orden.validadores.append("repetidas")
        return orden
