from IValidador import IValidador


class Cache(IValidador):
    def __init__(self):
        super().__init__()

    def ejecutar(self, orden):
        print("paso por el validador Cache")
        orden.validadores.append("Cache")
        return orden
