class Zoologico():
    def __init__(self,nombre, ubicacion):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=[]
    def agregarZonas(self,zona):
        self._zonas.append(zona)
        zona._zoo = self
    def cantidadTotalAnimales(self):
        cantidad=0
        for i in self._zonas:
            x= i.cantidadAnimales()
            cantidad+=x
        return  cantidad
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre
    def getUbicacion(self):
        return self._ubicacion
    def setUbicacion(self,ubicacion):
        self._ubicacion=ubicacion
    def getZona(self):
        return self._zonas
    def setZona(self,zonas):
        self._Zonas=zonas
    

    
