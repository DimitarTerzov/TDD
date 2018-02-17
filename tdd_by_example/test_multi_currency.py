class Money(object):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return self._amount == other._amount

    def equals(self, other):
        return (self._amount == other._amount and
                self._currency == other._currency)

    @staticmethod
    def dollar(amount):
        return Dollar(amount, "USD")

    @staticmethod
    def franc(amount):
        return Franc(amount, "CHF")

    def times(self, multiplier):
        return Money(self._amount*multiplier, self._currency)

    def currency(self):
        raise NotImplementedError


class Dollar(Money):
    def __init__(self, amount, currency):
        Money.__init__(self, amount, currency)

    def currency(self):
        return self._currency


class Franc(Money):
    def __init__(self, amount, currency):
        Money.__init__(self, amount, currency)

    def currency(self):
        return self._currency


def test_currency():
    assert "USD" == Money.dollar(1).currency()
    assert "CHF" == Money.franc(1).currency()


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


def test_different_class_equality():
    assert Money(10, "CHF").equals(Franc(10, "CHF"))
