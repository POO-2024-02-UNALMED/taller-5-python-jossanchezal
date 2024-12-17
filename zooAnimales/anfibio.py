from .animal import Animal
class Anfibio(Animal):
    _listado=[]
    ranas=0
    salamandras=0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._colorPiel = colorPiel
        self._venenoso = venenoso
        Anfibio._listado.append(self)
        Animal.setTotalAnimales(Animal.getTotalAnimales() + 1)

    def cantidadAnfibios():
        cantidad=len(Anfibio._listado)
        return cantidad
    def movimiento():
        return "saltar"
    def crearRana(self,nombre, edad, genero, zona):
        self._nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        self.colorPiel="rojo"
        self.venenoso=True
        self.habitat="selva"
    def crearSalamandra(self,nombre, edad, genero, zona):
        self._nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        self.colorPiel="negro y amarillo"
        self.venenoso=False
        self.habitat="selva"
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre
    @classmethod
    def getListado(cls):
        return cls._listado
    def setListado(self,listado:list):
        self._listadoo=listado
    def getColorPiel(self):
        return self._colorPiel
    def setColorPiel(self,color):
        self._colorPiel=color
    def getVenenoso(self):
        return self._venenoso
    def setVenenoso(self):
        if self._venenoso==True:
            self._venenoso=False
        else:
            self._venenoso==True
