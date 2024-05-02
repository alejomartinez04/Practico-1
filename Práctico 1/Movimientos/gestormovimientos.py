import csv
import numpy as np
from clasemovimientos import movimiento
class GestorMovimientos:
    __listamovs:np.array
    def __init__(self):
        self.__listamovs=np.empty([0],dtype=movimiento)
    def agregarmov(self, nuevomov):
        self.__listamovs=np.append(self.__listamovs, nuevomov)
    def leerdatos(self):
        archivo=open('MovimientosAbril2024.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                numc=int(fila[0])
                fecha=int(fila[1])
                desc=fila[2]
                tipo=fila[3]
                imp=float(fila[4])
                nuevo=movimiento(numc, fecha, desc, tipo, imp)
                self.agregarmov(nuevo)
        archivo.close()
    def buscar(self, numc):
        i=0
        bandera=True
        while i < len(self.__listamovs) and bandera:
            if numc==self.__listamovs[i].getnumc():
                fecha=self.__listamovs[i].getfecha()
                desc=self.__listamovs[i].getdesc()
                tipo=self.__listamovs[i].gettipo()
                imp=self.__listamovs[i].getimp()
                bandera=False
            else:
                i+1
        return fecha, desc, tipo, imp