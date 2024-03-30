#!/usr/bin/env python3

def contador_de_palabras():
    
    while True:
        frase = input("Ingrese una frase: ")
        
        if not isinstance(frase, str):
            print("Error: La entrada no es una cadena (str).")
            continue
        
        if not frase:
            print("Error: No se ingresó ninguna frase.")
            continue
        
        frase_en_lista = frase.split()
        
        contador = 0
        for x in frase_en_lista:
            contador += 1
        
        print("Número de palabras en la frase:", contador)
        break

contador_de_palabras()
