n = int(input("How many Fibonacci numbers? "))

a, b = 0, 1

if n <= 0:
    print("Enter a positive number.")
else:
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()