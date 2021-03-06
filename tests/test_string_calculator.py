import pytest
import exceptions


def add(string_numbers):
    numbers = string_numbers.split(',')
    if len(numbers) > 2:
        raise RuntimeError("Up to 2 numbers separated by comma (,) are allowed")
    else:
        for number in numbers:
            if not number.isdigit():
                raise RuntimeError


def test_more_than_two_numbers_added():
    expected = exceptions.RuntimeError
    assert expected == add("1,2,3")

