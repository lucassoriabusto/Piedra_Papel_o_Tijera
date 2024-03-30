#!/usr/bin/env python3

import random

def adivina():
    
    numero_random = random.randint(0, 9)
    intentos = 0
    
    while True:
        try:  
            numero = int(input("Adivine el numero: "))
        except ValueError:
            print("El valor introducido no es un número válido")
            continue
        
        intentos += 1
            
        if numero == numero_random:
            print(f"¡Felicidades! Adivinaste el número {numero_random} en {intentos} intentos.")
            break
        elif numero > numero_random:
            print("¡Demasiado grande! Trata con un número más pequeño.")
        else:
            print("¡Demasiado pequeño! Trata con un número más grande.")
        
adivina()
    