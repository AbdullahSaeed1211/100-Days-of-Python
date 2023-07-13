# tuple methods ()
#  convert a tuple to list then list to tuple to change 
countries =("spain","Italy","India","England")
temp = list(countries)
temp.append("Russia") #add item
temp.pop(3) #remove item
temp[2]="finland" #change item
countries=tuple(temp)
print(countries)

# OR
country =("spain","Italy","India","England")
country2 =("Russia","finland","Belgium")
coontry= country + country2
print(coontry)

num=(1,2,3,3,43,34,5)
num.count(3)