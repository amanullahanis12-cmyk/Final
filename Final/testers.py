'''Tests the hash table and the sorting algorithm'''
'''author Amanullah Anis'''
'''version 1.0 '''
'''since 1.0 '''

''' 
* OS: Windows
* IDE: Visual Studio
* Copyright : This is my own original work 
* based on specifications issued by our instructor
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified, nor used generative AI as a final draft. 
* I have not given other fellow student(s) access to my program.
'''
import unittest
from main import *
class Testmain(unittest.TestCase):
    def test_Hash(self):
        tht = Hash()
        tht.insert(1,[(3,2),(10,20),(31,2),(101,20)])
        tht.insert(2,[(8,5),(2,3),(1,2),(7,7),(12,0)])
        tht.insert(5,[(2,2),(123,21),(33,21),(105,120),(13,133)])
        self.assertEqual(tht.ht, {1:[(3,2),(10,20),(31,2),(101,20)],2:[(8,5),(2,3),(1,2),(7,7),(12,0)],5:[(2,2),(123,21),(33,21),(105,120),(13,133)]})
        self.assertEqual(tht.get(1), [(3,2),(10,20),(31,2),(101,20)])
        self.assertEqual(tht.contains(1), True)
        self.assertEqual(tht.contains(10), False)
        tht.remove(1)
        self.assertEqual(tht.ht, {2:[(8,5),(2,3),(1,2),(7,7),(12,0)],5:[(2,2),(123,21),(33,21),(105,120),(13,133)]})
        self.assertEqual(tht.get_length(), 2)
        tht.print()
        self.assertEqual(tht.variables, f'2- [(8, 5), (2, 3), (1, 2), (7, 7), (12, 0)]\n\n5- [(2, 2), (123, 21), (33, 21), (105, 120), (13, 133)]\n\n')
        tht.sort()
        self.assertEqual(tht.ht, {5:[(2,2),(123,21),(33,21),(105,120),(13,133)],2:[(8,5),(2,3),(1,2),(7,7),(12,0)]})
    def test_Sorter(self):
        self.tl = [3,12,54,10,9,87,-132,45,86,0,33]
        Sorter.insertion_sort(self.tl)
        self.assertEqual(self.tl,[87,86,54,45,33,12,10,9,3,0,-132])

if __name__ == '__main__':
    unittest.main()
