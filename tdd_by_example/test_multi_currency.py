class Money(object):
    pass


class Dollar(Money):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, other):
        return self.amount == other.amount


class Franc(object):
    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount

    def times(self, multiplier):
        return Franc(self.amount * multiplier)

    def equals(self, other):
        return self.amount == other.amount


def test_multiplication():
    five = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_equality():
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(5).equals(Dollar(6))


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
