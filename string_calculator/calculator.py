def add(string_numbers):
    numbers = string_numbers.split(',')
    if len(numbers) > 2:
        raise RuntimeError("Up to 2 numbers separated by comma (,) are allowed")
    else:
        for number in numbers:
            if not number.isdigit():
                raise RuntimeError
