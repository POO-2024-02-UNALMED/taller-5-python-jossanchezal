from zooAnimales.animal import Animal
class Mamifero(Animal):
    listado=[]
    leones=0
    caballos=0
    def __init__(self,caballos,leones,pelaje,patas):
        super()
        self.pelaje=pelaje
        self.patas=patas
        Mamifero.listado.append(self)
    def cantidadMamiferos(self):
        cantidad=len(Mamifero.listado)
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
