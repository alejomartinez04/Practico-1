from Clientes.gestorclientes import GestorCliente
from Movimientos.gestormovimientos import GestorMovimientos
if __name__=='__main__':
    opcion=input("Ingrese opcion:\na. Ingresar el DNI de un cliente y actualizar su saldo.\nb. Ingresar el DNI de un cliente para saber si no tuvo movimientos el mes de abril.\nc. Ordenar los movimientos por numero de cuenta.")
    gc=GestorCliente
    gm=GestorMovimientos
    gc.leerdatos()
    gm.leerdatos()
    if opcion=='a':
        dni=int(input("Ingrese DNI: "))
        nom, ap, numc, saldoant = gc.buscar(dni)
        fecha, desc, imp, tipo = gm.buscar(numc)
        saldoactual=gc.actualizarsaldo(tipo, saldoant)
        print("Cliente: {} {}\nNumero de cuenta: {}\nSaldo anterior: {}\nMovimientos\nFecha: {}\nDescripcion: {}\nImporte: {}\nTipo de movimiento: {}\n Saldo actualizado: {}".format(nom, ap, numc, saldoant, fecha, desc, imp, tipo, saldoactual))
    elif opcion=='b':
        xdni=int(input("Ingrese DNI: "))
        xnom, xap, xnumc, xsaldoant = gc.buscar(xdni)
        xfecha, xdesc, ximp, xtipo = gm.buscar(xnumc)
        if xtipo!='C' and xtipo !='P':
            print("{} {} no tuvo movimientos durante el mes de abril".format(xnom, xap))