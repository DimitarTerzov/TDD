
class Dollar(object):
    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier


def test_multiplication():
    five = Dollar(5)
    five.times(2)
    assert five.amount == 10
