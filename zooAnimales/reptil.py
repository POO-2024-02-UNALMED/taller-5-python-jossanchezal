from .animal import Animal
class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    def cantidadReptiles():
        cantidad=len(Reptil._listado)
        return cantidad
    def movimiento():
        return "reptar"
    @classmethod
    def crearIguana(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'verde'
        cls._largoCola = 3
        cls.setHabitat(cls, 'humedal')
        Reptil.iguanas += 1
        return Reptil(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._largoCola)

    @classmethod
    def crearSerpiente(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'blanco'
        cls._largoCola = 1
        cls.setHabitat(cls, 'jungla')
        Reptil.serpientes += 1
        return Reptil(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._largoCola)
    
    def getListado(self):
        return Reptil._listado
    def setListado(self,listado):
        Reptil._listadoo=listado
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,color):
        self._colorEscamas=color
    def getLargoCola(self):
        return self._largoCola
    def setLargoCola(self,largo):
        self._largoCola=largo
        

