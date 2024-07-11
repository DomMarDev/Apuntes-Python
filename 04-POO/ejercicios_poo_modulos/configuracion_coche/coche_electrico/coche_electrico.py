from coche.coche import Cotxe
from coche_electrico.bateria import Bateria

class Coche_electrico(Cotxe):
    def __init__(self, marca, modelo, anyo):
        super().__init__(marca, modelo, anyo)
        self.modelo_bateria = Bateria()