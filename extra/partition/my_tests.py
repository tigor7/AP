import unittest

from test_utils  import *
from solve       import *

class My_Tests(unittest.TestCase):
    def test_from_data_to_item(self):
        content = """3 0 2
                     20
                     30
                     10
                  """
        items, left, right = from_data_to_items(content)
        self.assertEqual(0, left)
        self.assertEqual(2, right)
        self.assertEqual([20,30,10], items)
        return

    # Ejemplo:
    #           Entrada              Salida
    #           -------              ------
    #       items = [20,30,10]     [10,20,30]
    #    left_pos = 0              return 1
    #   right_pos = 2              # Posición final del pivote

    def test_1(self):
        content = """3 0 2
                     20
                     30                  
                     10
                  """
        items, left, right = from_data_to_items(content)
        pos_pivote = partition(items, left, right)

        self.assertEqual([10,20,30], items)
        self.assertEqual(pos_pivote, 1)
        return
