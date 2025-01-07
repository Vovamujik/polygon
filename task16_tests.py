import numpy as np
import unittest

def trace1(matrix):
    return np.trace(matrix)

def trace2(matrix):
    return np.sum(np.diag(matrix))

class TestMatrixTrace(unittest.TestCase):
    def test_square(self):
        matrix = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])
        expected = 15  # 1 + 5 + 9
        self.assertEqual(trace1(matrix), expected)
        self.assertEqual(trace2(matrix), expected)

    def test_ne_squar(self):
        matrix = np.array([[1, 2, 3],
                           [4, 5, 6]])
        expected = 6  # 1 + 5
        self.assertEqual(trace1(matrix), expected)
        self.assertEqual(trace2(matrix), expected)

    def test_one_element(self):
        matrix = np.array([[42]])
        expected = 42  
        self.assertEqual(trace1(matrix), expected)
        self.assertEqual(trace2(matrix), expected)

    def test_empty(self):
        matrix = np.array([[]])
        expected = 0 
        self.assertEqual(trace1(matrix), expected)
        self.assertEqual(trace2(matrix), expected)

if __name__ == "__main__":
    unittest.main()