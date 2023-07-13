# Break and continue
for i in range(12):
    if(i==10):
        break
    print( " 5 *",i+1 ,"= ",5*(i+1))
# Emulate do while
i = 0
while True:
    print(i)
    i+=100
    if(i%100==0):
     break