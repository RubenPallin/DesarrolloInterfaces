import random

opciones = ["piedra", "papel", "tijera"]
jugadas = 0
partidasGanadas = 0


while jugadas < 5:
    jugada_usuario = input("Cuál es tú jugada(piedra, papel o tijera): ")

    while jugada_usuario != "piedra" and jugada_usuario != "papel" and jugada_usuario != "tijera":
        print("Solo hay tres opciones espabila")
        jugada_usuario = input("Vuelve a elegir tu jugada(piedra, papel o tijera): ")

    # Turno de la máquina con el random
    jugada_maquina = random.choice(opciones)
    
    print("La jugada de la máquina ha sido "+jugada_maquina)

    if jugada_maquina == jugada_usuario:
        print("Ha sido un empate")
        print("Volced a tirar")

    elif jugada_maquina == "piedra" and jugada_usuario == "papel":
        print("Enhorabuena has ganado, el papel vence a la piedra")
        jugadas += 1
        partidasGanadas += 1

    elif jugada_maquina == "tijera" and jugada_usuario == "papel":
        print("Pierdes tijera vence al papel")
        jugadas += 1

    elif jugada_maquina == "tijera" and jugada_usuario == "piedra":
        print("Enhorabuena has ganado, la piedra vence a la tijera")
        jugadas += 1
        partidasGanadas += 1

    elif jugada_maquina == "piedra" and jugada_usuario == "tijera":
        print("Pierdes piedra vence a tijera")
        jugadas += 1

    elif jugada_maquina == "papel" and jugada_usuario == "piedra":
        print("Pierdes papel vence a piedra")
        jugadas += 1

    elif jugada_maquina == "papel" and jugada_usuario == "tijera":
        print("Enhorabuena has ganado, la tijera vence al papel")
        jugadas += 1
        partidasGanadas += 1

print("\t")
print("El juego ha finalizado.")
print("\t")

if partidasGanadas >= 3:
    print("Lo lograste, le ganaste a una máquina siéntete orgulloso. En total ganaste " + str(partidasGanadas) + " rondas de 5")
else:
    print("Lo siento, eres un paquete has perdido contra la máquina. En total ganaste " + str(partidasGanadas) + " rondas de 5")
