# Finally clause for clean-ups
def func1():
    try:
        l=[1,5,6,7]
        l= int(input("Enter the Index"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("Always Executed") #will happen regardless even if the function is returned 
x=func1()
print(x)
