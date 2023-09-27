num1 = 0
num2 = 0

def suma_numeros(num1, num2):
	suma = num1 + num2
	return suma

def resta_numeros(num1, num2):
	resta = num1 - num2
	return resta

def multiplicacion_numeros(num1, num2):
	multiplicacion = num1 * num2
	return multiplicacion

def division_numeros(num1, num2):
    if num2 == 0:
        return "No se puede dividir por cero."
    else:
        return num1 / num2
