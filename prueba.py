#!/usr/bin/env python3

import random

def lanzar_dado():
    dado = random.randint(1, 6)
    return dado

def resultado(dado):
    print(f"El dado a caido en el {dado}")
    
dado = lanzar_dado()
resultado(dado) 