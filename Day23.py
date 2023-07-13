# list methods
l=[1,23,4]
l.append(7) #element appeneded to end of l
l.sort(reverse=True) #sorts descending
l.sort() # sorts list ascending order
l.reverse() #reverses the list
print(l.index(23)) #returns first occcurence 
print(l.count(1)) #counts occurrences

# m=l  this changes actual list
# m[0]=0
# print(l)

m = l.copy()
l.insert(1,899) #index of 899 is 1
# l.extend()
n=[900,100,1222]
l.extend(n)
print(l) #adds list m to end of list l
#or
k=l+n 
print(k)