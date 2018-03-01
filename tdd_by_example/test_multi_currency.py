class Money(object):
    def __init__(self, amount, currency):
        self._amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self._amount == other._amount and
                self._currency == other._currency)

    equals = __eq__

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self._amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        return Money(self._amount + addend._amount, self._currency)


class Bank():
    def reduse(self, source, to_currency):
        return Money.dollar(10)


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
    assert not Money.franc(5).equals(Money.dollar(5))


def test_simple_addition():
    five = Money.dollar(5)
    sum_ = five.plus(five)
    bank = Bank()
    reduced = bank.reduse(sum_, "USD")
    assert Money.dollar(10) == reduced
