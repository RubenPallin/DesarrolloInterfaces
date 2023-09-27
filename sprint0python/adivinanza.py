import random

numeros = list(range(1,4))
puntuacion = 0

mat_adivinanza = random.sample(numeros, 2)

if mat_adivinanza[0] == 1 or mat_adivinanza[1] == 1:
    print ("Soy un mes de vacaciones con nombre de emperador. A veces refresco el rostro, otras doy mucho calor.¿Quién soy?")
    print ("a) Junio")
    print ("b) Agosto")
    print ("c) Octubre")

    respuesta = input("Tu respuesta es...(a/b/c) ")

    if (respuesta.upper() == 'B'):
        print("Respuesta correcta")
        print("Has conseguido 10 puntos")
        puntuacion += 10
    else:
        print("Respuesta incorrecta")
        print("Has perdido 5 puntos")
        puntuacion -= 5

if mat_adivinanza[0] == 2 or mat_adivinanza[1] == 2:
    print ("Sal al campo por las noches si me quieres conocer, soy señor de grandes ojos, cara seria y gran saber. ¿Quién soy?")
    print ("a) Halcón")
    print ("b) Murciélago")
    print ("c) Búho")

    respuesta = input("Tu respuesta es...(a/b/c) ")

    if (respuesta.upper() == 'C'):
        print("Respuesta correcta")
        print("Has conseguido 10 puntos")
        puntuacion += 10
    else:
        print("Respuesta incorrecta")
        print("Has perdido 5 puntos")
        puntuacion -= 5

if mat_adivinanza[0] == 3 or mat_adivinanza[1] == 3: 
    print ("¿Qué cosa es? ¿Qué cosa es? Que corre mucho y no tiene pies.")
    print ("a) El viento")
    print ("b) El guepardo")
    print ("c) La ballena")

    respuesta = input("Tu respuesta es...(a/b/c) ")

    if (respuesta.upper() == 'A'):
        print("Respuesta correcta")
        print("Has conseguido 10 puntos")
        puntuacion += 10
    else:
        print("Respuesta incorrecta")
        print("Has perdido 5 puntos")
        puntuacion -= 5

print("Tu puntuación final ha sido de: "+str(puntuacion))
