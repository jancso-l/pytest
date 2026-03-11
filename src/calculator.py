
class Calculator:
    """
    Basic Calculator class.
    """
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def calc_add(self):
        return self.num1 + self.num2

    def calc_diff(self):
        return self.num1 - self.num2

    def calc_prod(self):
        return self.num1 * self.num2

    def calc_division(self):
        return self.num1 / self.num2