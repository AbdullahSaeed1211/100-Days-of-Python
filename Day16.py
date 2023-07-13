# import os
# print("hello World")
# os.system("python --version")  // checks version L

#match case {very similar to switch case}

x=10
match x:
    case 0:
        print("x is zero")
    case 6:
        print("x is six")
    case 3:
        print("x is thwee")
    case 10:
        print("x is ten ")
    case _ if x!=90: #default
        print(x, "isn't 90")
    case _ if x!=20: #default
        print(x, "isn't 90")
    case _: #default
        print(x)


#no break used here unlike cpp ,