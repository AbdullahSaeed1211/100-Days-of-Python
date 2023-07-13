# tuples IMMUTABLE use ()

tup=(1,2,3,4,5,"green",True)
print(type(tup),tup)
# if only 1 elements then tup =(1,) else python reads it as int
print(len(tup))
print(tup[1])
print(tup[3])
# negative indexing same as list

if 32 in tup:
    print('yes')
    
# you can slice but another tuple is returned
tup2=tup[1:4]
print(tup2)
