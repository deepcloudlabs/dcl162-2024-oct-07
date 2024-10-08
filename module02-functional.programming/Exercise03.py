def fun(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens


def gun(numbers):
    cubed = []
    for number in numbers:
        cubed.append(number ** 3)
    return cubed


lost = [4, 8, 15, 16, 23, 42]
total = sum(gun(fun(lost)))
print(f"total is {total}") # 78760