#!/usr/bin/env python3

def par_o_impar():
    
    while True:
        try:
            r = input("Ingese un numero o exit para salir: ")
            
            if r.lower() == "exit":
                return None
            else:
                n = int(r)
                break

        except ValueError:
            print("El valor introducido no es un número válido")
    
    if n % 2 == 0:
        print(f"{n} es par")
    else:
        print(f"{n} es impar")
    

while True:
    if par_o_impar() is None:
        break