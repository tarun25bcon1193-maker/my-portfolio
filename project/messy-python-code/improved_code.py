def calculate_even_sum(start, end):
    total = 0

    for number in range(start, end + 1):
        if number % 2 == 0:
            total += number

    return total


print(calculate_even_sum(1, 10))