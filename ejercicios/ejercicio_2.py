#!/usr/bin/env python3

def operations():
    
    while True:
        try:
            a = float(input("Primer numero: "))
            break
        except ValueError:
            print("El valor introducido no es un número. Intenta de nuevo")
            
    operation = input("Operador (+, -, *, /): ")
    
    lista = ["+", "-", "*", "/"]
    while operation not in lista:
        print("El valor introducido no es un operador. Intenta de nuevo")
        operation = input("Operador (+, -, *, /): ")
           
    while True:    
        try:
            b = float(input("Segundo numero: "))
            break
        except ValueError:
            print("El valor introducido no es un número. Intenta de nuevo")
            
    if operation == "+":
        resultado = a + b
    elif operation == "-":
        resultado = a - b
    elif operation == "*":
        resultado = a * b
    elif operation == "/":
        if b != 0:
            resultado = a / b
        else:
            print("Error: No se puede dividir por cero.")
            return
    
    print(f"El resultado es: {resultado}")

while True:
    operations()
    
    respuesta = input("¿Quieres realizar otra operación? (s/n): ")
    if respuesta.lower() != 's':
        break