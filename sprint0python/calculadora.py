from operaciones import suma_numeros, resta_numeros, multiplicacion_numeros, division_numeros

continuar = "s"

while continuar == "s":
    num1 = int(input("Introduce un valor para num1: "))
    num2 = int(input("Introduce un valor para num2: "))

    op = input("Elige una función que quieras realizar con los números introducidos:  ")

    if op == "suma":
        resultado = suma_numeros(num1,num2)
    elif op == "resta":
        resultado = resta_numeros(num1,num2)
    elif op== "division":
        resultado = division_numeros(num1,num2)
    elif op == "multiplicacion":
        resultado = multiplicacion_numeros(num1,num2)
    else:
        print("Esa operación no está disponible.")

    print("El resultado es " + str(resultado))
    
    continuar = input("Quieres hacer otra operación?(s/n)")

    while continuar != "s" and continuar != "n":
        print("Esa opción no es válida")
        seguir = input("Quieres seguir jugando?(s/n)")
        
print("El programa ha finalizado")
