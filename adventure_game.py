
import time
import random
tscore=0
environments=["polar area","forest","desert"]
arms=["axe","saw","pickaxe"]
def my_game():#the function of the game
        
    print("you are lost in somewhere")
    time.sleep(2) #delays the execution for 2 seconds
    print("it seems like a")
    print(random.choice(environments))#allow randomness in the game in the environments
    time.sleep(2)#delays the execution for 2 seconds
    print("you have")
    print(random.choice(arms))#allow randomness in the game in the arms
    time.sleep(2)#delays the execution for 2 seconds
    print("the weather is cold")
    time.sleep(2)#delays the execution for 2 seconds
    print("Enter 1 to continue walking")
    print("Enter 2 to light a fire")
    x = (input("enter 1 or 2"))
    while x != "2" and x!="1": #when the input of the user !=1 or !=2 the game asks for correct input untill the user input 1 or 2 
        x= (input("enter 1 or 2"))     
    def bad(): #the function that is called when the user input incorrect one and asks him to play again
         print("this a bad choice")
         print("you lose")
         play_again=input("play again y/n")#the game asks the user for playing again when he lose
         while play_again !="y" and play_again!="n": #when the user input incorrect one the game asks the user to input y or n
            play_again=input("play again y/n")
         if play_again=="y": # when value of play_again= y the game starts again 
             my_game()
         elif play_again=="n": #when the value of play_again= n it quit from function
             print("thank you for playing")
             quit()
             
    def good(p):#function is used when the user input a correct one
         print("This a good choice")
         tscore =p
         print("score is")
         print(tscore)

    if x=="2":#when x=="2" it calls the function good(1) 
        good(1)
        
    elif x=="1":#when x=="1" it calls the function bad() 
        bad()

    time.sleep(2)#delays the execution for 2 seconds
    print("You hear the sound of wild animals")
    time.sleep(2)#delays the execution for 2 seconds
    print("Enter 1 to make a spear of trees")

    print("Enter 2 to wait someone")
    y=(input("Enter 1 or 2"))

    while y!="2" and y!="1":#when the input of the user !=1 or !=2 the game asks for correct input untill the user input 1 or 2 
        y=(input("Enter 1 or 2"))
    if y=="1":#when y=="1" it calls the function good(2) 
        good(2)
    elif y=="2":#when y=="2" it calls the function bad()
         bad()

    time.sleep(2)#delays the execution for 2 seconds
    print("you fells hungury")
    time.sleep(2)#delays the execution for 2 seconds
    print("Enter 1 to hunt a rabbit")
    print("Enter 2 to Wait for someone to save you")
    z=(input('Enter 1 or 2'))
    while z!="2" and z!="1":#when the input of the user !=1 or !=2 the game asks for corect input untill the user input 1 or 2 
        z=(input("Enter 1 or 2"))
    if z=="1":#when z=="1" it calls the function good(3) 
        good(3)
    elif z=="2":#when z=="2" it calls the function bad()
         bad()
    time.sleep(2)#delays the execution for 2 seconds
    print("you see a plane")
    time.sleep(2)
    print("Enter 1 to Wave it with your hands")
    print("Enter 2 to Light a torch and wave it")
    l=(input("Enter 1 or 2"))
    while l!="2" and l!="1":
        l=(input("Enter 1 or 2"))
    def good4(p):
        print("The plane saved you and you won")
        time.sleep(2)#delays the execution for 2 seconds
        tscore=p
        print( "score is")
        print(tscore)
        play_again=input("play again y/n")#the game asks the user for playing again when he lose
        while play_again !="y" and play_again!="n":#when the user input incorrect one the game asks the user to input y or n
            play_again=input("play again y/n")
        if play_again=="y":# when value of play_again= y the game starts again 
             my_game()
        elif play_again=="n":#when the value of play_again= n it quit from function
             print("thank you for playing")
             quit()

    if l=="1":#when l=="1" it calls the function bad()
        bad()
    elif l=="2":#when l=="2" it calls the function good(4) 
        good4(4)
my_game()#it calls the my_game() function







