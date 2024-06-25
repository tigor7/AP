# Copia aqui tu solución del VPL Partition

def partition(items, left_pos, right_pos, pivot):
   """
   :param vector: numpy vector containing integer numbers
   :param left: left index of our subarray
   :param right: right index of our subarray
   :param pivot: index to the pivot element
   :return: index to the pivot on its definitive position
   """
   def swap(left, right):
      items[left], items[right] = items[right], items[left]

   swap(left_pos, pivot)
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
   return -1

