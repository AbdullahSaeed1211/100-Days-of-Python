from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess=input("Pick a number between 0,1 and 2: ")
    return int(guess)
def check_guess(mylist,guess):
    if mylist[guess]=='O':
        print("Correct!")
        print(mylist)
    else:
        print("Try Again!")
        print(mylist)
# Initial List
mylist=['','O','']

# Shuffle list
shuffled_list=shuffle_list(mylist)

# Player Guess
guess=player_guess()

#Check Guess
check_guess(shuffled_list,guess)