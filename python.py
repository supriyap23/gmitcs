#calculate a^m with two input using function

def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: ")) 
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))



#using function calculate twin prime number between 1 to 100 in python

def find_prime_pairs(n):

    sieve = [True] * n

    if n > 0:
        sieve[0] = False
        if n > 1:
            sieve[1] = False

    for number in range(2, int(n ** 0.5) + 1):
        if sieve[number]:
            for index in range(number * number, n, number):
                sieve[index] = False

    return [(a, b) for b, a in enumerate(range(0, n - 2), start=2) if sieve[a] and sieve[b]]

print(*find_prime_pairs(100), sep='\n')





# using python caculate a number prime or not


def factorial(n) : 

    fact = 1

    while (n != 0) : 

        fact = fact * n 

        n = n - 1

    return fact 

def isKrishnamurthy(n) : 

    sum = 0

    temp = n 

    while (temp != 0) : 

  
        rem = temp%10

        sum = sum + factorial(rem) 

        temp = temp // 10

          

    return (sum == n) 

  


n = int(input("Enter any number"))

if (isKrishnamurthy(n)) : 

    print("YES") 

else : 

    print("NO")





# palindrome or not


import math 

def rev(num): 

    return int(num != 0) and ((num % 10) *

             (10**int(math.log(num, 10))) +

                          rev(num // 10)) 

test_number = 9669669
print("The original number is: " + str(test_number)) 

res = test_number == rev(test_number) 

print("Is the number palindrome?:" + str(res))





#Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 10

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))





