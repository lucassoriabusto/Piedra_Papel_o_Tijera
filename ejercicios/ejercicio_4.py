#!/usr/bin/env python3

def calculo_factorial():
    
    n = int(input("Calcule el factorial de "))
    
    factorial = 1
    for i in range(1, n + 1):
        factorial =  factorial * i
    print(factorial)
    
calculo_factorial()