# decimal_precision.py
class DecimalPrecision:
    def __init__(self, precision=2):
        self.precision = precision

    def set_precision(self, precision):
        self.precision = precision

    def format_result(self, result):
        return round(result, self.precision)
