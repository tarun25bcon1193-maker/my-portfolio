def factorial(n):
    if n < 0:
        return "Negative numbers are not allowed"

    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


number = int(input("Enter a number: "))
print("Factorial:", factorial(number))