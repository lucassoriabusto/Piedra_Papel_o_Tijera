#!/usr/bin/env python3

def gestionar_lista():
    lista_compra = ["manzanas", "plátanos", "leche", "pan"]
    
    while True: 
        menu = str(input("1- Mostrar, 2- Agregar, 3- Quitar: "))
        
        if menu == "1":
            print(lista_compra)
        elif menu == "2":
            lista_compra = agregar_a_lista(lista_compra)
            print(lista_compra)
        elif menu == "3":
            lista_compra = quitar_a_lista(lista_compra)
            print(lista_compra)
        else:
            print("Opción no válida. Introduce 1, 2 o 3.")
        break
    
    
def agregar_a_lista(lista_compra):
    print(f"La lista contiene: {lista_compra}")
    x = input("Agregar elemento de la lista: ")
    lista_compra.append(x)
    return lista_compra

def quitar_a_lista(lista_compra):
    print(f"La lista contiene: {lista_compra}")
    y = input("Quitar elemento de la lista: ")
    if y in lista_compra:
        lista_compra.remove(y)
    return lista_compra

gestionar_lista()