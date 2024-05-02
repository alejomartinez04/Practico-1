import csv
from claseclientes import cliente
class GestorCliente:
    __listaclientes:list
    def __init__(self):
        self.__listaclientes=[]
    def agregarcliente(self, nuevocliente):
        self.__listaclientes.append=nuevocliente
    def leerdatos(self):
        archivo=open('ClientesFarmaCiudad.csv')
        reader=csv.reader(archivo, delimiter=';')
        band=True
        for fila in reader:
            if band:
                band=False
            else:
                nom=fila[0]
                ap=fila[1]
                dni=int(fila[2])
                numcuenta=int(fila[3])
                saldoant=float(fila[4])
                nuevo=cliente(nom, ap, dni, numcuenta, saldoant)
                self.agregarcliente(nuevo)
        archivo.close()
    def buscar(self, dni):
        i=0
        bandera=True
        while i < len(self.__listaclientes) and bandera:
            if dni==self.__listaclientes[i].getdni():
                nom=self.__listaclientes[i].getnom()
                ap=self.__listaclientes[i].getap()
                numc=self.__listaclientes[i].getnumc()
                saldoant=self.__listaclientes[i].getsaldoant()
                bandera=False
            else:
                i+1
        return nom, ap, numc, saldoant
    def actualizarsaldo(self, xtipo, xsaldoant):
        saldo=0
        if xtipo=='C':
            saldo+=xsaldoant
        else:
            saldo-=xsaldoant
        return saldo