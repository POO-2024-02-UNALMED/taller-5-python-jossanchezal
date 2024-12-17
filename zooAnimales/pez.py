from zooAnimales.animal import Animal
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
    def crearSalmon(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        Pez.salmones+=1
        self.colorEscamas="rojo"
        self.cantidadAletas=6
        self.habitat="océano"
    def crarBacalao(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        Pez.bacalaos+=1
        self.colorEscamas="gris"
        self.cantidadAletas=6
        self.habitat="océano"
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