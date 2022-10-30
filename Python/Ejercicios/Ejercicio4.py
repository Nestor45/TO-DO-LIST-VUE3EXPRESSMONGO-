band = True
while band:
    print("Convertidor de divisas")
    print("[1] Pesos a dolares")
    print("[2] Dolares a pesos")
    print("[3] Pesos a Euros")
    print("[4] Euros a pesos")
    print("[5] Salir")
    op = input("Escriba la opcion que sea: ")
    if op == '5':
        break
    elif op == '1':
        print("Pesos a dolares")
        pesos = float(input("Ingrese la cantidad en pesos:"))
        print(f"{pesos} pesos Mexicanos son {pesos*20.1078} dolares")
        continue #El ciclo del bucle vuelve al inicio
    elif op == '2':
        print("Dolares a pesos")
        pesos = float(input("Ingrese la cantidad en Dolares:"))
        print(f"{pesos} Dolares son {pesos*20.1078} Pesos Mexicanos")
        continue #El ciclo del bucle vuelve al inicio
    elif op == '3':
        print("Pesos a Euros")
        pesos = float(input("Ingrese la cantidad en pesos:"))
        print(f"{pesos} pesos Mexicanos son {pesos*19.6435} Euros")
        continue #El ciclo del bucle vuelve al inicio
    elif op == '4':
        print("Euros a Pesos")
        pesos = float(input("Ingrese la cantidad en Euros:"))
        print(f"{pesos} Euros son {pesos*19.6435} Pesos Mexicanos")
        continue #El ciclo del bucle vuelve al inicio
    else:
        print("*************Opcion no valida****************")