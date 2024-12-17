from .animal import Animal
class Ave(Animal):
    _listado=[]
    aguilas=0
    halcones=0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    def cantidadAves():
        cantidad=len(Ave._listado)
        return cantidad
    def movimiento():
        return "volar"
    @classmethod
    def crearHalcon(cls, nombre, edad, genero) -> Animal:
        cls._colorPlumas = 'cafe glorioso'
        cls.setHabitat(cls, 'montanas')
        Ave.halcones += 1
        return Ave(nombre, edad, cls.getHabitat(cls), genero, cls._colorPlumas)

    @classmethod
    def crearAguila(cls, nombre, edad, genero) -> Animal:
        cls._colorPlumas = 'blanco y amarillo'
        cls.setHabitat(cls, 'montanas')
        Ave.aguilas += 1
        return Ave(nombre, edad, cls.getHabitat(cls), genero, cls._colorPlumas)
    def setNombre(self,nombre):
        self._nombre=nombre
    def getListado(self):
        return Ave._listado
    def setListado(self,listado):
        Ave._listado=listado
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,color):
        self._colorPlumaso=color
