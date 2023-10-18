#!/usr/bin/env python3
import random

def game():
    print("\nJuega al Piedra, Papel o Tijera \n")

    while True:
        jugador_1 = eleccion_jugador_1()
        jugador_2 = eleccion_jugador_2()

        print(f"Jugador 1 eligió {traducir_eleccion(jugador_1)}")
        print(f"Jugador 2 eligió {traducir_eleccion(jugador_2)}")
        
        resultado = determinar_ganador(jugador_1, jugador_2)
        print(resultado)

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (si/no): ").lower()
        if jugar_de_nuevo != "si":
            break

def eleccion_jugador_1():
    while True:
        print("Ingrese un número para elegir:\n1 - Piedra\n2 - Papel\n3 - Tijera")
        jugador_1 = input("Jugador 1 ingrese un número: ")
        if jugador_1 in ["1", "2", "3"]:
            return int(jugador_1)
        else:
            print("\nIngrese un valor válido (1, 2 o 3)\n")

def eleccion_jugador_2():
    return random.randint(1, 3)

def traducir_eleccion(numero):
    if numero == 1:
        return "Piedra"
    elif numero == 2:
        return "Papel"
    else:
        return "Tijera"

def determinar_ganador(jugador_1, jugador_2):
    if jugador_1 == jugador_2:
        return "Empate"
    elif (jugador_1 == 1 and jugador_2 == 3) or \
         (jugador_1 == 2 and jugador_2 == 1) or \
         (jugador_1 == 3 and jugador_2 == 2):
        return "Gana Jugador 1"
    else:
        return "Game Over"


if __name__ == "__main__":
    game()
