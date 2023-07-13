# Exception Handling
# we use try and except
a=input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i}={int(a)*i}")
except: #Exception as e:
    print("Invalid input")
    
 
try:
    num=int(input("Enter an Integer"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Entered number isn't an integer")
except IndexError:
    print("Index Error")

    
print("Some lines of code")
print("Some lines of code")
print("End of code ")