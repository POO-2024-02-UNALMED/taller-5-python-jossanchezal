from zooAnimales.animal import Animal
class Ave(Animal):
    listado=[]
    aguilas=0
    halcones=0
    def __init__(self, halcones, aguilas, colorPlumas):
        super()
        self.colorPlumas=colorPlumas
        Ave.listado.append(self)
    def cantidadAves():
        cantidad=len(Ave.listado)
        return cantidad
    def movimiento():
        return "volar"
    def crearHalcon(self,nombre, edad, genero, zona):
        self.colorPlumas="café glorioso"
        self.habitat= "montañas"
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        Ave.halcones+=1
    def crearAguila(self,nombre, edad, genero, zona):
        self.nombre=nombre
        self.edad=edad
        self.genero=genero
        self.zona=zona
        Ave.aguilas+=1
        self.colorPlumas="blanco y amarillo"
        self.habitat="montañas"
