# function args
# def sum(a,b):
#     print('sum is ', a+b)
# sum(89,11)


# default args
def sum(a=12,b=23):
    print('sum is ', a+b)
sum(89,11)
sum()
sum(1)
# keyword arb args
def average(*numbers):
    for i in numbers:
        sum=sum + i
    print("Avg is",sum/len(numbers))

# 