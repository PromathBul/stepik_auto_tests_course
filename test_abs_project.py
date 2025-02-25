import unittest

class TestAbs(unittest.TestCase):
    def test_abs_1(self):
        self.assertEqual(abs(-42), 42, "Ожидается абсолютное значение числа")

    def test_abs_2(self):
        self.assertEqual(abs(-42), -42, "Ожидается абсолютное значение числа")

if __name__ == '__main__':
    unittest.main()