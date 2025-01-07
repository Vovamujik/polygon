import unittest
import numpy as np


def elements_above_mean(array):
    mean_value = np.mean(array)
    return np.sum(array > mean_value)

class TestCountAboveMean(unittest.TestCase):
    def test1(self):
        array = np.array([1, 1, 2, 3, 1, 5])
        expected = 2  # Среднее = 2.16(6), больше среднего: 3, 5
        self.assertEqual(elements_above_mean(array), expected)

    def test_all_equal(self):
        array = np.array([2, 2, 2, 2])
        expected = 0  # Среднее = 2, никто не больше
        self.assertEqual(elements_above_mean(array), expected)

    def test2(self):
        array = np.array([10, 20, 30, 40])
        expected = 2  # Среднее = 25, больше среднего: 30, 40
        self.assertEqual(elements_above_mean(array), expected)

    def test_large_array(self):
        array = np.arange(1, 10001)  # Массив от 1 до 10 000
        expected = 5000  # Среднее = 5000.5, больше среднего: от 5001 до 10000
        self.assertEqual(elements_above_mean(array), expected)

    def test_empty_array(self):
        array = np.array([])  # Пустой массив
        expected = 0  # Нет элементов, нет больше среднего)
        self.assertEqual(elements_above_mean(array), expected)

    def test_single_element(self):
        array = np.array([42])
        expected = 0  # Среднее = 42, никто не больше
        self.assertEqual(elements_above_mean(array), expected)

if __name__ == "__main__":
    unittest.main()
