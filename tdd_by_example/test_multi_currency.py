class Money(object):
    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount

    def equals(self, other):
        return (self._amount == other._amount and
                self.__class__ == other.__class__)

    @staticmethod
    def dollar(amount):
        return Dollar(amount)

    @staticmethod
    def franc(amount):
        return Franc(amount)

    def times(self, multiplier):
        raise NotImplementedError


class Dollar(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def times(self, multiplier):
        return Money(self._amount * multiplier)


class Franc(Money):
    def __init__(self, amount):
        Money.__init__(self, amount)

    def times(self, multiplier):
        return Money(self._amount * multiplier)


def test_multiplication():
    five = Money.dollar(5)
    assert Money.dollar(10) == five.times(2)
    assert Money.dollar(15) == five.times(3)


def test_equality():
    assert Money.dollar(5).equals(Money.dollar(5))
    assert not Money.dollar(5).equals(Money.dollar(6))
    assert Money.franc(5).equals(Money.franc(5))
    assert not Money.franc(5).equals(Money.franc(6))
    assert not Money.franc(5).equals(Money.dollar(5))


def test_franc_multiplication():
    five = Money.franc(5)
    assert Money.franc(10) == five.times(2)
    assert Money.franc(15) == five.times(3)
