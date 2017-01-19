import unittest
from main.prime_checker import is_prime

class PrimeChecker(unittest.TestCase):
	def test_number_is_int(self):
		self.assertTrue(is_prime('6'), str)


if __name__ == '__main__':
	unittest.main()