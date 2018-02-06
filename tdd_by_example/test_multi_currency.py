class Money(object):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount

    def equals(self, other):
        return self._amount == other._amount


class Dollar(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def times(self, multiplier):
        return Franc(self._amount * multiplier)


def test_multiplication():
    five = Dollar(5)
    assert Dollar(10) == five.times(2)
    assert Dollar(15) == five.times(3)


def test_equality():
    assert Dollar(5).equals(Dollar(5))
    assert not Dollar(5).equals(Dollar(6))
    assert Franc(5).equals(Franc(5))
    assert not Franc(5).equals(Franc(6))


def test_franc_multiplication():
    five = Franc(5)
    assert Franc(10) == five.times(2)
    assert Franc(15) == five.times(3)
