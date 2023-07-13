# recursions
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
        
print(factorial(5))

# Fibonacci
def fib(x):
    if(x==0):
        return 0
    elif(x==1 or x==2):
        return 1
    else:
       return fib(x-1)+fib(x-2)
z=int(input("Enter number of terms "))
for i in range(z):
    print(fib(i))