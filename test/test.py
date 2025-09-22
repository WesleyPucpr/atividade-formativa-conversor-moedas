import unittest
from currency_converter import convert_currency, get_available_currencies

class TestCurrencyConverter(unittest.TestCase):
    def test_convert_currency_valid(self):
        result = convert_currency(100, "USD", "EUR")
        self.assertTrue(isinstance(result, str))
        self.assertTrue(result.startswith("100 USD ="))

    def test_convert_currency_invalid_to_currency(self):
        result = convert_currency(100, "USD", "XYZ")
        self.assertEqual(result, "Currency XYZ not found")

    def test_convert_currency_api_error(self):
        result = convert_currency(100, "XXX", "EUR")
        self.assertTrue(result.startswith("Error fetching exchange rates"))

    def test_get_available_currencies(self):
        currencies = get_available_currencies()
        self.assertTrue(isinstance(currencies, list))
        self.assertGreater(len(currencies), 0)
        self.assertIn("USD", currencies)

if __name__ == '__main__':
    unittest.main()