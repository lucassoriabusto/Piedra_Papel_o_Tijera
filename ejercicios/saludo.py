#!/usr/bin/env python3

def saludo():
    nombre = input("Cómo te llamas?: ")
    estado = input("¿Cómo estás?: ")
    saludo = f"Hola {nombre}!!. Me alegro que estés {estado}"
    print(saludo)

saludo()