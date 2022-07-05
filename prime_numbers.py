def isPrimeNumber(number):
    if number > 1:
        for i in range(2,number):
            if number % i == 0:
                #print(f"{i} times {number//i} is {number}")
                #print(f"{number} is not a prime number")
                return False    
        return True
    else:
        return False    

print("7 is prime", isPrimeNumber(7))
print("9 is prime", isPrimeNumber(9))
#isPrimeNumber(56)
#isPrimeNumber(6883)
#isPrimeNumber(6882)

def allPrimeNumbers(num):
    for i in range(num):
        if isPrimeNumber(i):
            print(i, end = ", ")


print("prime numbers to 100")
allPrimeNumbers(100)
