class Zoologico:
    def __init__(self,nombre, ubicacion,zonas):
        self._nombre=nombre
        self._ubicacion=ubicacion
        self._zonas=zonas
    def agregarZonas(self,zona):
        self._zonas.append(zona)
    def cantidadTotalAnimales(self):
        cantidad=0
        for i in self._zonas:
            x=len(i)
            cantidad+=x
        return  cantidad
    
