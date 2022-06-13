# print even numbers
# method1
def evenNumbers():
    n=0
    while n < 100:
        n += 1
        if n % 2 == 0:
            print(n)
        else:
            print("*")

evenNumbers()

print("another solution")
def evenNumbers2():
    numbers = range(0,101)
    for n in numbers:
        if n % 2 == 1:
            continue
        print(n)


evenNumbers2()
