from zooAnimales.animal import Animal
class Anfibio(Animal):
    listado=[]
    ranas=0
    salamandras=0
    def __init__(self,colorPiel, venenoso):
        super()
        self.colorPiel=colorPiel
        self.venenoso=venenoso
        Anfibio.listado.append(self)
    def cantidadAnfibios():
        cantidad=len(Anfibio.listado)
        return cantidad
    def movimiento():
        return "saltar"
    def crearRana(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        self.colorPiel="rojo"
        self.venenoso=True
        self.habitat="selva"
    def crearSalamandra(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        self.colorPiel="negro y amarillo"
        self.venenoso=False
        self.habitat="selva"
