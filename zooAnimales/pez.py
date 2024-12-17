from .animal import Animal
class Pez(Animal):
    _listado=[]
    salmones=0
    bacalaos=0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas=colorEscamas
        self._cantidadAletas=cantidadAletas
        Pez._listado.append(self)
    def cantidadPeces():
        cantidad=len(Pez._listado)
        return cantidad
    def movimiento():
        return "nadar "
    @classmethod
    def crearSalmon(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'rojo'
        cls._cantidadAletas = 6
        cls.setHabitat(cls, 'oceano')
        Pez.salmones += 1
        return Pez(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._cantidadAletas)

    @classmethod
    def crearBacalao(cls, nombre, edad, genero) -> Animal:
        cls._colorEscamas = 'gris'
        cls._cantidadAletas = 6
        cls.setHabitat(cls, 'oceano')
        Pez.bacalaos += 1
        return Pez(nombre, edad, cls.getHabitat(cls), genero, cls._colorEscamas, cls._cantidadAletas)
    def getListado(self):
        return Pez._listado
    def setListado(self,listado):
        Pez._listadoo=listado
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self,color):
        self._colorEscamas=color
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self,cantidad):
        self._cantidadAletas=cantidad