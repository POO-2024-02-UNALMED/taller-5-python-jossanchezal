from zooAnimales.animal import Animal
class Pez(Animal):
    listado=[]
    salmones=0
    bacalaos=0
    def __init__(self, colorEscamas, cantidadAletas):
        super()
        self.colorEscamas=colorEscamas
        self.cantidadAletas=cantidadAletas
        Pez.listado.append(self)
    def cantidadPeces():
        cantidad=len(Pez.listado)
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