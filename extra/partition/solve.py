
def partition(items, left_pos, right_pos):
   """
      items: lista no vacía que sólo contiene números enteros
    left_pos: posición del primer elemento de la sublista de items
   right_pos: posición del ultimo elemento de la sublista de items
   
   Dada una lista no vacía de números enteros (items) programa el
   algoritmo de partición para QuickSort utilizando como pivote el
   elemento más a la izquierda de la sublista de items que hay entre
   las posiciones left_pos y right_pos (ámbas incluidas).

   Retorna la posición definitiva del pivote en la lista de items.

   Ejemplo:
              Entrada               Salida
      ----------------------     -------------
          items = [20,30,10]      [10,20,30]
       left_pos = 0               return 1 # Posición final del pivote
      right_pos = 2

    En este ejemplo la sublista es la lista completa (left_pos = 0,
    right_pos = 2), el pivote es el valor 20 y la función retorna
    la lista de items modificada tras la partición y el valor 1
    que es la posición final del pivote 20 en la lista de salida.
   """
   def swap(left, right):
      items[left], items[right] = items[right], items[left]

   pivot = left_pos
   left_pos += 1
   while True:
      while left_pos <= right_pos and items[left_pos] < items[pivot]:
         left_pos += 1

      while right_pos >= left_pos and items[right_pos] > items[pivot]:
         right_pos -= 1

      if left_pos > right_pos:
         break
      swap(left_pos, right_pos)

   swap(right_pos, pivot)

   return right_pos
