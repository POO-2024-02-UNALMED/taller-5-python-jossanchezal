from .animal import Animal
class Mamifero(Animal):
    _listado=[]
    leones=0
    caballos=0
    def __init__(self, nombre, edad, habitat, genero, pelaje, patas):
        super().__init__(nombre, edad, habitat, genero)
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    def cantidadMamiferos(self):
        cantidad=len(Mamifero._listado)
        return cantidad
   
    @classmethod
    def crearCaballo(cls, nombre, edad, genero) -> Animal:
        cls._pelaje = True
        cls._patas = 4
        cls.setHabitat(cls, 'pradera')
        Mamifero.caballos += 1
        return Mamifero(nombre, edad, cls.getHabitat(cls), genero, cls._pelaje, cls._patas)
    
    @classmethod
    def crearLeon(cls, nombre, edad, genero) -> Animal:
        cls._pelaje = True
        cls._patas = 4
        cls.setHabitat(cls, 'selva')
        Mamifero.leones += 1
        return Mamifero(nombre, edad, cls.getHabitat(cls), genero, cls._pelaje, cls._patas)
    
    def setNombre(self,nombre):
        self._nombre=nombre
    def getListado(self):
        return Mamifero._listado
    def setListado(self,listado):
        Mamifero._listadoo=listado
    def isPelaje(self):
        return self._pelaje
    def setPelaje(self,pelaje):
        self._pelaje=pelaje
    def getPatas(self):
        return self._patas
    def setPatas(self,patas):
        self._patas=patas
