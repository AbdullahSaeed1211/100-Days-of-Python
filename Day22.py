# lists in python
l=[1,2,4,5]
print(l)
print(type(l))
# tuples are immutable
# list is mutable can store multiple types str , bool , int
print(l[1])
print(l[len(l)-3])

if 7 in l:
    print("yes")
else:
    print("no")
    
if 'arry' in 'Harry ':
    print("yes")

print(l[1:3])
print(l[1:3:2]) #jumps 2

# list comprehension
lst = [i*i for i in range(4)]
print(lst)
lst2 = [i for i in range(4)]
print(lst2)
lst = [i for i in range(10) if i%2==0]
print(lst)