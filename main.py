'''
1 for snake
-1 for water
0 for gun

'''
computer = 0
youstr = input("Enter your choice: ")
youDict = {"s" : 1 , "w" : -1, "g" : 0}
reverseDict = {1 : "snake", -1 : "water", 0 : "gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if (computer == you):
    print("it is draw")                             
else:                                         #Nesting
    if(computer == -1 and you == 1):
        print("You win!")
        
    elif(computer == -1 and you == 0):
        print("You Lose!")
    
    elif(computer == 1 and you == -1):
        print("You Lose!")
    
    elif(computer == 1 and you == 0):
        print("You win!")
        
    elif(computer == 0 and you == -1):
        print("You win!")
    
    elif(computer == 0 and you == 1):
        print("You Lose!")
        
    else:
     print("somthing wantes wrong")
        
        