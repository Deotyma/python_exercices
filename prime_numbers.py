def isPrimeNumber(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                print(f"{i} times {number//i} is {number}")
                print(f"{number} is not a prime number")
                break

            else:
                print(f"{number} is a prime number")
                break

isPrimeNumber(7)
isPrimeNumber(56)
isPrimeNumber(6883)
isPrimeNumber(6882)