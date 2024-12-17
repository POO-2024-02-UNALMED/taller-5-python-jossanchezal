from zooAnimales.animal import Animal
class Zona:
    def __init__(self,nombre,zoo,animales):
        self._nombre=nombre
        self._zoo=zoo
        self._animales=animales
    def agregarAnimales(self,animal):
        self._animales.append(animal)
    def cantidadAnimales(self):
        cantidad=len(self._animales)
        return cantidad

        