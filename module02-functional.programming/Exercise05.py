def fun(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"fun yields {number}")
            yield number



def gun(numbers):
    for number in numbers:
        print(f"gun yields {number ** 3}")
        yield number ** 3


lost = [4, 8, 15, 16, 23, 42]
result = gun(fun(lost)) # lazy evaluation
total = sum(result)
print(f"total: {total}")