from zooAnimales.animal import Animal
class Ave(Animal):
    _listado=[]
    aguilas=0
    halcones=0
    def __init__(self, nombre, edad, habitat, genero, colorPlumas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas=colorPlumas
        Ave._listado.append(self)
    def cantidadAves():
        cantidad=len(Ave._listado)
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
    def setNombre(self,nombre):
        self._nombre=nombre
    def getListado(self):
        return Ave._listado
    def setListado(self,listado):
        Ave._listado=listado
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self,color):
        self._colorPlumaso=color
