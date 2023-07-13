# set methods
s1={1,2,5,6}
s2={3,9,8,5,6,7}
print(s1.union(s2))
s1.update(s2) # bring values of s2 not present in s1 into s1 and update s1
print(s1,s2)
s1.intersection_update(s1)
print(s1)
s3=s1.difference(s2)
print(s3)
# isdisjoint() checks if items of given set are presnt in another set
# issuperset()
# issubset()
# add() adds a singles item to set
# update() adds more than one item
# remove()/discard() remove raises error if item not present discard doesn't
# pop() removes last element but since sets are unordered it pops random value which will be accessible much like stacks
# del - keyword not a methods deletes an entire set 
# clear() clears all elements 

