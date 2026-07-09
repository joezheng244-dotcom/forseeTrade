import unittest

from main import predict_next_price_with_ai


class TestAIPredictor(unittest.TestCase):
    def test_predict_next_price_with_ai_returns_float(self) -> None:
        prices = [100, 102, 101, 105, 107, 109, 108, 112, 115, 114]
        prediction = predict_next_price_with_ai(prices)
        self.assertIsInstance(prediction, float)
        self.assertGreater(prediction, 0)


if __name__ == "__main__":
    unittest.main()
