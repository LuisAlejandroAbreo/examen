def menu():
    print("""\n\n\n*** CAJERO AUTOMATICO ***
1. Consultar saldo
2. Depositar saldo
3. Retirar dinero
0. Salir
---------
Opcion(0-3)? """)
    
def leer_opcion():
    op = input()
    while(not op.isdigit() or int(op) < 0  or int(op) > 3):
        print("Error. Opción inválida. Dígite un numero de 0 a 3")
        input("Presione cualquier letra para continuar....")
        print("\n\n")
        menu()
        op = input(
        )
    return int(op)

def validar_monto(monto):
    return monto > 0

def validar_saldo(monto, saldo):
    return monto <= saldo

def consultar_saldo(saldo):
    print(f"\nSu saldo actual es de ${saldo}")
    return saldo

def depositar(saldo):
    try:
        monto = float(input("Ingrese el monto que desea depositar: "))
        if validar_monto(monto):
            saldo += monto
            print(f"\nDepositó con éxito el dinero!!!")
        else:
            print("\nError: El deposito debe ser mayor que cero.")
    except ValueError:
        print("\nError: Ingrese un valor numérico válido.")
    return saldo


def retirar(saldo):
    try:
        monto = float(input("Ingrese el monto a retirar "))
        if not validar_monto(monto):
            print("\nError: El monto debe ser mayor que cero.")
        elif not validar_saldo(monto, saldo):
            print("\nFondos insuficientes para realizar el retiro del dinero.")
        else:
            saldo -= monto
            print(f"\nSe retiró con éxito el dinero!!!!")
    except ValueError:
        print("\nError: Ingrese un valor numérico válido.")
    return saldo    

def main():
    saldo = 1000

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            saldo = consultar_saldo(saldo)
        elif opcion == "2":
            saldo = depositar(saldo)
        elif opcion == "3":
            saldo = retirar(saldo)
        elif opcion == "0":
            print("\nGracias por usar el cajero automatico. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")

main()