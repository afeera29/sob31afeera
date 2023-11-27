import random
#code
def compare_numbers(number, user_guess):
    l=[]
    n=[]
    for d in number:
        n.append(int(d))
    cowcount=0
    bullcount=0
    for i in user_guess:
        l.append(int(i))
    for j in l:
        if str(j) in str(number):
            cowcount+=1
    for b in range(0,4):
        if l[b]==n[b]:
            bullcount+=1
    cowbull=[str(cowcount),str(bullcount)]
    return cowbull

playing = True #gotta play the game
number = str(random.randint(1000,9999)) #random 4 digit number, changed 0 to 1000
guesses=0
#print number(commented) 
print("Let's play a game of Cowbull!") #explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every number that exists in the sequence but is in wrong place, you get a cow. For every one in the right place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type exit at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess!")
    if len(user_guess)==4:# ensuring a four digit number is entered
        if user_guess == "exit":
            break
        cowbullcount = compare_numbers(number,user_guess)
        print(cowbullcount)
        guesses+=1
        print("You have ",str(cowbullcount[0]) , " cows, and " , str(cowbullcount[1]) ," bulls.")
        if cowbullcount[1]=='4':
            print("You have won the game after " ,str(guesses) , " guesses! The number was ",str(number))
            playing = False
            break #redundant exit
        else:
            print("Your guess isn't quite right, try again.")
            
    else:
        print("please enter a four digit number")#if four digit number is not entered


       



