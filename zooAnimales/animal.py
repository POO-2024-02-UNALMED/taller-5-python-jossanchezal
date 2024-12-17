from zooAnimales.anfibio import Anfibio
from zooAnimales.ave import Ave
from zooAnimales.mamifero import Mamifero
from zooAnimales.pez import Pez
from zooAnimales.reptil import Reptil
from gestion.zoologico import Zoologico
class Animal:
    def __init__(self,totalAnimales, nombre, edad, hablar, genero, zona):
        self.totalAnimales=totalAnimales
        self.nombre=nombre
        self.edad=edad
        self.hablar=hablar
        self.genero=genero
        self.zona=zona
    def movimiento():
        return "desplazarse"
    def totalPorTipo(self):
        cantidad_mamiferos = len(Mamifero.listado)
        cantidad_aves = len(Ave.listado)
        cantidad_reptiles = len(Reptil.listado)
        cantidad_anfibios = len(Anfibio.listado)
        cantidad_peces = len(Pez.listado)
        return f"Mamíferos: {cantidad_mamiferos}\nAves: {cantidad_aves}\nReptiles: {cantidad_reptiles}\nPeces: {cantidad_peces}\nAnfibios: {cantidad_anfibios}"
    def toString(self):
        if self.genero==None and self.zona==None:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat}, y mi género es {self.genero}."
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat}, y mi género es {self.genero}.\nLa zona en la que me ubico es {self.zona.nombre}, en el {self.zona.zoo.nombre}."