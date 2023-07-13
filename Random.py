def cube(num):
    return num*num*num
print(cube(3))

print("-------------------------------------------------------------------------\n\n")

num1 = input("Enter number to be cubed: ")
def cubic(num):
    return print(cube(int(num1)))
cubic(int(num1))

print("-------------------------------------------------------------------------\n\n")

def Sum(num,num2):
    return num+num2
result = Sum(17,23)
print(result)    

print("-------------------------------------------------------------------------\n\n")

def loop(num):
    for num in range(1,11):
        print(num)
    return num
loop(1)