class movimiento:
    __numc:int
    __fecha:int
    __descripcion:str
    __tipodemov:str
    __imp:float
    def __init__(self, xnumc, xfecha, xdesc, xtipo, ximp):
        self.__numc=xnumc
        self.__fecha=xfecha
        self.__descripcion=xdesc
        self.__tipodemov=xtipo
        self.__imp=ximp

    def getnumc(self):
        return self.__numc
    def getfecha(self):
        return self.__fecha
    def getdesc(self):
        return self.__descripcion
    def gettipo(self):
        return self.__tipodemov
    def getimp(self):
        return self.__imp