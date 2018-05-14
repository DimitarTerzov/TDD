class Money(object):
    def __init__(self, amount, currency):
        self.amount = amount
        self._currency = currency

    def __eq__(self, other):
        return (self.amount == other.amount and
                self._currency == other._currency)

    equals = __eq__

    @staticmethod
    def dollar(amount):
        return Money(amount, "USD")

    @staticmethod
    def franc(amount):
        return Money(amount, "CHF")

    def times(self, multiplier):
        return Money(self.amount * multiplier, self._currency)

    def currency(self):
        return self._currency

    def plus(self, addend):
        return Sum(self, addend)

    def reduce(self, bank, to_currency):
        rate = bank.rate(self._currency, to_currency)
        return Money(self.amount / rate, to_currency)

class Bank(object):
    def __init__(self):
        self.rates = {}

    def reduce(self, source, to_currency):
        return source.reduce(self, to_currency)

    def rate(self, from_currency, to_currency):
        if from_currency == to_currency:
            return 1
        return self.rates.get(Pair(from_currency, to_currency))

    def add_rate(self, from_currency, to_currency, rate):
        self.rates[Pair(from_currency, to_currency)] = rate

class Sum(object):
    def __init__(self, augend, addend):
        self.augend = augend
        self.addend = addend

    def reduce(self, bank, to_currency):
        amount = self.augend.reduce(bank, to_currency).amount \
            + self.addend.reduce(bank, to_currency).amount
        return Money(amount, to_currency)

class Pair(object):
    def __init__(self, from_currency, to_currency):
        self.from_currency = from_currency
        self.to_currency = to_currency

    def __eq__(self, another):
        pair = another
        return self.from_currency == pair.from_currency and \
               self.to_currency == pair.to_currency

    def __hash__(self):
        return 0

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
    sum = five.plus(five)
    bank = Bank()
    reduced = bank.reduce(sum, "USD")
    assert Money.dollar(10) == reduced

def test_plus_returns_sum():
    five = Money.dollar(5)
    sum = five.plus(five)
    assert five == sum.augend
    assert five == sum.addend

def test_reduce_sum():
    sum = Sum(Money.dollar(3), Money.dollar(4))
    bank = Bank()
    result = bank.reduce(sum, "USD")
    assert Money.dollar(7) == result

def test_reduce_money():
    bank = Bank()
    result = bank.reduce(Money.dollar(1), "USD")
    assert Money.dollar(1).equals(result)

def test_reduce_money_different_currency():
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(Money.franc(2), "USD")
    assert Money.dollar(1) == result

def test_identity_rate():
    assert Bank().rate("USD", "USD") == 1

def test_mixed_addition():
    five_bucks = Money.dollar(5)
    ten_franks = Money.franc(10)
    bank = Bank()
    bank.add_rate("CHF", "USD", 2)
    result = bank.reduce(five_bucks.plus(ten_franks), "USD")
    assert Money.dollar(10) == result
