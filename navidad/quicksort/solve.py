import random
from partition import *

# Programa aqui el algoritmo de Quick Sort. Utiliza este VPL para programar
# una versión eligiendo privote fijo y otra con pivote aleatorio.

def quick_sort(items):
    def recursive(left, right):
        if left < right:
            pivot = partition(items, left, right, right)
            recursive(left, pivot - 1)
            recursive(pivot + 1, right)

    recursive(0, len(items) - 1)
