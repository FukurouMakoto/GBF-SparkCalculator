import unittest
import SparkCalculator

class TestSparkCalculator(unittest.TestCase):

    def test_totalDraws(self):
        self.assertEqual(SparkCalculator.totalDraws(90000, 0, 0), 300)
        self.assertEqual(SparkCalculator.totalDraws(0, 300, 0), 300)
        self.assertEqual(SparkCalculator.totalDraws(0, 0, 30), 300)
        self.assertEqual(SparkCalculator.totalDraws(39000, 100, 7), 300)
        self.assertEqual(SparkCalculator.totalDraws(-5040, 10, -4), -46.8)
        self.assertEqual(int(SparkCalculator.totalDraws(-5000, -10, 5)), 23)

    def test_how_many_rolls(self):
        self.assertEqual(SparkCalculator.how_many_rolls(450), "You can spark a character and have 150 draws leftover to draw for whomever you want!")
        self.assertEqual(SparkCalculator.how_many_rolls(300), "You can spark a character!")
        self.assertEqual(SparkCalculator.how_many_rolls(150), "Sorry, you need 150 draws until you can spark a character...")
        self.assertEqual(SparkCalculator.how_many_rolls(600), "You can spark a character and have 300 draws leftover to draw for whomever you want!")
        self.assertEqual(SparkCalculator.how_many_rolls(100), "Sorry, you need 200 draws until you can spark a character...")
        self.assertEqual(SparkCalculator.how_many_rolls(299), "Sorry, you need 1 draws until you can spark a character...")

    def test_test_for_negative(self):
        self.assertEqual(SparkCalculator.test_for_negative(50), False)
        self.assertEqual(SparkCalculator.test_for_negative(1), False)
        self.assertEqual(SparkCalculator.test_for_negative(0), False)
        self.assertEqual(SparkCalculator.test_for_negative(-45), True)
        self.assertEqual(SparkCalculator.test_for_negative(-25), True)
        self.assertEqual(SparkCalculator.test_for_negative(-100), True)

    def test_sparkCalculator(self):
        self.assertEqual(SparkCalculator.sparkCalculator(90000, 0, 0), "You can make a total of 300 draws.")
        self.assertEqual(SparkCalculator.sparkCalculator(0, 300, 0), "You can make a total of 300 draws.")
        self.assertEqual(SparkCalculator.sparkCalculator(0, 0, 30), "You can make a total of 300 draws.")
        self.assertEqual(SparkCalculator.sparkCalculator(39000, 100, 7), "You can make a total of 300 draws.")
        self.assertEqual(SparkCalculator.sparkCalculator(-5040, 10, -4), "You can make a total of -46 draws.")
        self.assertEqual(SparkCalculator.sparkCalculator(-5000, -10, 5), "You can make a total of 23 draws.")

if __name__ == '__main__':
    unittest.main()
