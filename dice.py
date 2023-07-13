from random import shuffle
dieone=[1,2,3,4,5,6]
dietwo=[1,2,3,4,5,6]
def shuffled(dieone,dietwo):
    shuffle(dieone)
    shuffle(dietwo)
    print(dieone[0])
    print(dietwo[0])
(shuffled(dieone,dietwo))