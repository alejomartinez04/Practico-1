class cliente:
    __nom:str
    __ap:str
    __dni:int
    __numcuenta:int
    __saldoant:float
    def __init__(self, xnom, xap, xdni, xnumc, xsaldo):
        self.__nom=xnom
        self.__ap=xap
        self.__dni=xdni
        self.__numcuenta=xnumc
        self.__saldoant=xsaldo

    def getnom(self):
        return self.__nom
    def getap(self):
        return self.__ap
    def getdni(self):
        return self.__dni
    def getnumc(self):
        return self.__numcuenta
    def getsaldoant(self):
        return self.__saldoant