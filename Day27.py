# KBC 
# use list data type to store questions and correct ans
# display final amt the person is taking home after 

questions=["Who is the musician of the strawhats","Who is the helmsman of the strawhats","Who is the captain of the strawhats"]
answers=["Brook","Jimbei","Zoro","Luffy"]
key=["A","B","C","D"]
for i in range(3):
    print(questions[i])
    for k in range(4):
        print(answers[k])
        k=k+1
    guess=input("Enter Answer key ")
    for j in range(3):
        if(guess==key[j]):
            print("You have won ", j+1 ," crore rupees ")
        else:
            print("You have lost")
            break
    i=i+1
            
