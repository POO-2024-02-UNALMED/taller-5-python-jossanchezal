from zooAnimales.animal import Animal
class Reptil(Animal):
    listado=[]
    iguanas=0
    serpientes=0
    def __init__(self, colorEscamas, largoCola):
        super()
        self.colorEscamas=colorEscamas
        self.largoCola=largoCola
        Reptil.listado.append(self)
    def cantidadReptiles():
        cantidad=len(Reptil.listado)
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
        

