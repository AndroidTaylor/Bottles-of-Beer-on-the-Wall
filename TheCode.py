#Written by Andrew Taylor April 25, 2019
#This program takes any number bottles of beer on a wall, and counts down. As the song 
#continues, the text gets more incoherent, simulating the speaking drinking the beer

#These are some important modules that I used to make the program
from time import sleep
import random
import sys

#Asking for INPUT
while 1 == 1:
    try:
        bottles = int(input("How many bottles start on the wall: "))
        break
    
#Exception Handling, for if the user inputs a non valid value, such as a character
    except ValueError:
        print("Please enter a valid number.")

#Defining variable to use later
drunkness = -1

#This Function is used to write the text into the terminal, with the included the 
#effects of alcohol
def passingbottle(sentence):
    #This repeats the following for every character in the sentence.
    for char in sentence:
            if drunkness >= 2:
                
                #Adds semi-random slowing to the typing
                sleep(0.01*(random.choice(drunklist)))
                
                #Adds random upper cased characters that get more frequent as the song continues
                case = random.random()*100
                if case*drunkness >= 290:
                    sys.stdout.write(char.upper())
                    sys.stdout.flush()
                
                #Randomly replaces characters with '*hic*'
                elif random.randint(0,50) == 50:
                    print("*hic*", end='')
                
                #Randomly Replaces characters with a space
                elif random.randint(0,50) == 50:
                    sys.stdout.write(" ")
                    sys.stdout.flush()
                
                #Just normally writes the character
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                        
            #If the program has not taken 3 bottles of beer, all characters and typing speeds are normal.
            else:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            
            #If the computer has take 5 or more beers, there is a 25% chance of repeating a character
            if drunkness >= 4:
                if random.random()*100 >= 75:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                else:
                    pass
            else:
                pass

#Starting song loop, looping until there are zero bottles left
while (bottles >= 1):
    drunkness = drunkness + 1
    
    #This Vairable determines the random typing speed, getting potentially worse as time goes on
    drunklist = [5, drunkness, 6, 9, 10, 20, 15]
    
    #This case is for when all mentions of bottles are plural
    if bottles >= 3:
        bottlesminusone = bottles - 1
        bottles_str = str(bottles)
        bottles2_str = str(bottlesminusone)
        sentence = (bottles_str + " bottles of beer on the wall, \n" + bottles_str + " bottles of beer. \n" + "Take one down, pass it around, \n" + bottles2_str + " bottles of beer on the wall.\n\n")
        passingbottle(sentence)
        bottles = bottles - 1
    
    #This case is for when the first two mentions of bottles is plural, but the last is singular
    elif bottles == 2:
        bottlesminusone = bottles - 1
        bottles_str = str(bottles)
        bottles2_str = str(bottlesminusone)
        sentence = (bottles_str + " bottles of beer on the wall, \n" + bottles_str + " bottles of beer. \n" + "Take one down, pass it around, \n" + bottles2_str + " bottle of beer on the wall.\n\n")
        passingbottle(sentence)
        bottles = bottles - 1
    
    #This case is for if the first two mention of bottles is singular, and I choose to make zero bottles be plural
    else:
        bottlesminusone = bottles - 1
        bottles_str = str(bottles)
        bottles2_str = str(bottlesminusone)
        sentence = (bottles_str + " bottle of beer on the wall, \n" + bottles_str + " bottle of beer. \n" + "Take one down, pass it around, \n" + bottles2_str + " bottles of beer on the wall.\n \nWhew, that was a mouth full!")
        passingbottle(sentence)
        bottles = bottles - 1
        print("\n")
        
#TEST (keep in mind, all runs have a differnt outcome, due to the random nature of the program, so the test is basically running from 5 bottles and it not crashing)
#My test: (When asked for input, input 5)
'''
How many bottles start on the wall: 5
5 bottles of beer on the wall, 
5 bottles of beer. 
Take one down, pass it around, 
4 bottles of beer on the wall.

4 bottles of beer on the wall, 
4 bottles of beer. 
Take one down, pass it around, 
3 bottles of beer on the wall.

3  ottles of beer on the wall, 
3*hic*bottl*hic*s of beer  
Take *hic*ne down, pass i  around, 
2 bottl*hic*s of beer on the wal .

2 bott  s of beer on the wal*hic*, 
2 bottles of beeR. 
T*hic*ke one down, pass it*hic*around, 
1 botTl*hic* of beeR on tHe wall.

11 BboTt*hic*tle of  *hic*bE r On the ww*hic*Lll, 

1 boTttlee  oF  beEr..*hic*
TTaK  O Ee dooWwNn, pAsss iiT  aroUndd, 
0  ooTtttlles  of beer on  thhe wwaLl*hic*.
  
Wheeww  ThAt wwaS aa Mouuth*hic* fUllL!
'''
