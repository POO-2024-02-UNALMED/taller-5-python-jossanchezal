from zooAnimales.animal import Animal
class Reptil(Animal):
    _listado=[]
    iguanas=0
    serpientes=0
    def __init__(self, colorEscamas, largoCola):
        super()
        self._colorEscamas=colorEscamas
        self._largoCola=largoCola
        Reptil._listado.append(self)
    def cantidadReptiles():
        cantidad=len(Reptil._listado)
        return cantidad
    def movimiento():
        return "reptar"
    def crearIguana(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        self.colorEscamas="verde"
        self.largoCola=3
        self.habitat="humedal"
    def crearSerpientres(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        self.colorEscamas="blanco"
        self.largoCola=1
        self.habitat="jungla"
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
        

