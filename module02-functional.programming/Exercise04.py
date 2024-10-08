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
for num in gun(fun(lost)):
    print(f"for: num is {num}")