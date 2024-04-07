import unittest
from is_prime import is_prime, half_number, divisible

class TestIsPrime(unittest.TestCase):
    def test_with_0(self):
        result = is_prime(0)
        self.assertFalse(result)

    def test_with_1(self):
        result = is_prime(1)
        self.assertTrue(result)
    
    def test_with_2(self):
        result = is_prime(2)
        self.assertTrue(result)
    
    def test_with_3(self):
        result = is_prime(3)
        self.assertTrue(result)
    
    def test_with_4(self):
        result = is_prime(4)
        self.assertFalse(result)
    
    def test_with_7(self):
        result = is_prime(7)
        self.assertTrue(result)
    
    def test_with_114(self):
        result = is_prime(114)
        self.assertFalse(result)
    
    def test_with_11(self):
        result = is_prime(11)
        self.assertTrue(result)
    
    def test_with_35(self):
        result = is_prime(35)
        self.assertFalse(result)
    
    def test_with_4906(self):
        result = is_prime(4906)
        self.assertFalse(result)
    
    def test_with_97(self):
        result = is_prime(97)
        self.assertTrue(result)
    
    def test_with_9777777(self):
        result = is_prime(9777777)
        self.assertFalse(result)

class TestHalf(unittest.TestCase):
    def test_with_half_1(self):
        result = half_number(1)
        self.assertEqual(result, 0)

    def test_with_half_2(self):
        result = half_number(2)
        self.assertEqual(result, 1)

    def test_with_half_3(self):
        result = half_number(3)
        self.assertEqual(result, 1)
    
    def test_with_half_4(self):
        result = half_number(4)
        self.assertEqual(result, None)
    
    def test_with_half_7(self):
        result = half_number(7)
        self.assertEqual(result, 3)
    
    def test_with_half_34(self):
        result = half_number(34)
        self.assertEqual(result, None)
    
    def test_with_half_127(self):
        result = half_number(127)
        self.assertEqual(result, 63)
    
    def test_with_half_4906(self):
        result = half_number(4906)
        self.assertEqual(result, None)
    
class TestDivisible(unittest.TestCase):
    def test_300(self):
        result = divisible(300)
        self.assertEqual(result, "Divisible")

    def test_303(self):
        result = divisible(303)
        self.assertEqual(result, "Divisible")
    
    def test_3000000004(self):
        result = divisible(3000000004)
        self.assertEqual(result, "Divisible")
    
    def test_15879(self):
        result = divisible(15879)
        self.assertEqual(result, "Divisible")
    
    def test_3(self):
        result = divisible(15879)
        self.assertEqual(result, "Divisible")   



unittest.main()