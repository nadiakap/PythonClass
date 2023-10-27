def fibonacci():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y
        
# Accept input from the user
n = int(input("Enter the number of Fibonacci numbers you want to generate "))

print("Number of first ",n,"Fibonacci numbers:")
fib = fibonacci()
for _ in range(n):
    print(next(fib),end=" ")