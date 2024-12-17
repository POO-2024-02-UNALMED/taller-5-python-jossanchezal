from zooAnimales.animal import Animal
class Mamifero(Animal):
    _listado=[]
    leones=0
    caballos=0
    def __init__(self,caballos,leones,pelaje,patas):
        super()
        self._pelaje=pelaje
        self._patas=patas
        Mamifero._listado.append(self)
    def cantidadMamiferos(self):
        cantidad=len(Mamifero._listado)
        return cantidad
    def crearCaballo(self,nombre, edad, genero, zona):
        Mamifero.caballos+=1
        self.pelaje=True
        self.patas=4
        self.habitat="pradera"
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
    def crearLeon(self, nombre, edad, genero, zona):
        Mamifero.leones+=1
        self.pelaje=True
        self.patas=4
        self.habitat="selva"
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
    def setNombre(self,nombre):
        self._nombre=nombre
    def getListado(self):
        return Mamifero._listado
    def setListado(self,listado):
        Mamifero._listadoo=listado
    def getPelaje(self):
        return self._pelaje
    def setPelaje(self,pelaje):
        self._pelaje=pelaje
    def getPatas(self):
        return self._patas
    def setPatas(self,patas):
        self._patas=patas
