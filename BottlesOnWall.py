#Written by Andrew Taylor April 25, 2019
#This program takes any number bottles of beer on a wall, and counts down. As the son 
#continues, the text gets more incoherent, simulating the speaker drinking the beer


#These are some important modules that I used to make the program
from time import sleep
import random
import sys



#Header
print("*******************************************************")
print("***   Bottles of Beer on the Wall (Drunk edition)   ***")
print("*******************************************************")


#Asking for INPUT
while 1 == 1:
    try:
        bottles = int(input("How many bottles start on the wall: "))
        #Making sure the user does not input a number less than 1, because nothing would even happen
        if bottles <= 0:
            print("Please input a valid number.")
            continue
        else:
            pass
        
        #If everything checks out, the program will carry on
        print("\n")
        break
    
#Exception Handling, for if the user inputs a non valid value, such as a character
    except ValueError:
        print("Please enter a valid number.")

#Defining variable to use later
drunkness = -1
HicCounter = 1
SpaceCounter = 1
UpperCaseCounter = 0
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '\n']
#This Function is used to write the text into the terminal, with the included the 
#effects of alcohol
def passingbottle(sentence, HicCounter, SpaceCounter, UpperCaseCounter):
    #This repeats the following for every character in the sentence.
    for char in sentence:
            if drunkness >= 2:
                
                #Adds semi-random slowing to the typing
                sleep(0.01*(random.choice(drunklist)))
                
                #Adds random upper cased characters that get more frequent as the song continues
                case = random.random()*100
                
                #Preventing more than 4 caps in a row, otherwise it just looks like I put caps lock on for no reason.
                if case*drunkness >= 200:
                    
                    if UpperCaseCounter < 4:
                        sys.stdout.write(char.upper())
                        sys.stdout.flush()
                        UpperCaseCounter += 1
                    else:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        UpperCaseCounter = 0
                elif UpperCaseCounter >= 4:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    UpperCaseCounter = 0
     
    
    
                #Randomly replaces characters with '*hic*'
                elif drunkness*random.randint(0,100) == 80:
                    HicCounter -= 1
                    
                    #This prevents the program form spamming out "*Hic*'s"
                    if HicCounter == 0:
                        print("*hic*", end='')
                        HicCounter = random.randint(0,5)
                        
                    #Randomly Replaces characters with a space
                    elif drunkness*random.randint(0,100) == 80:
                    
                        #Prevents the spamming of spaces
                        if SpaceCounter == 0:
                            sys.stdout.write(" ")
                            sys.stdout.flush()
                            SpaceCounter = random.randint(0,3)
                        else:
                            pass
                
                #Just normally writes the character
                else:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                        
                #If the program has not taken 3 bottles of beer, all characters and typing speeds are normal.
            else:
                sleep(0.05)
                sys.stdout.write(char)
                sys.stdout.flush()
            
            #If the computer has take 5 or more beers, there is a 25% chance of repeating a character, but will not if the character is a number, because that looks ugly.
            if char in numbers:
                pass
            else:
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
        passingbottle(sentence, HicCounter, SpaceCounter, UpperCaseCounter)
        bottles = bottles - 1
    
    #This case is for when the first two mentions of bottles is plural, but the last is singular
    elif bottles == 2:
        bottlesminusone = bottles - 1
        bottles_str = str(bottles)
        bottles2_str = str(bottlesminusone)
        sentence = (bottles_str + " bottles of beer on the wall, \n" + bottles_str + " bottles of beer. \n" + "Take one down, pass it around, \n" + bottles2_str + " bottle of beer on the wall.\n\n")
        passingbottle(sentence, HicCounter, SpaceCounter, UpperCaseCounter)
        bottles = bottles - 1
    
    #This case is for if the first two mention of bottles is singular, and I choose to make zero bottles be plural
    else:
        bottlesminusone = bottles - 1
        bottles_str = str(bottles)
        bottles2_str = str(bottlesminusone)
        sentence = (bottles_str + " bottle of beer on the wall, \n" + bottles_str + " bottle of beer. \n" + "Take one down, pass it around, \n" + bottles2_str + " bottles of beer on the wall.\n \nWhew, that was a mouth full!")
        passingbottle(sentence, HicCounter, SpaceCounter, UpperCaseCounter)
        bottles = bottles - 1
        print("\n")
        
#TEST (Keep in mind that the nature of this program is random, so your actuall output may vary, but to test that it works, you have to run it with 5 bottles, because it will defitely hit all cases in the distortions)

'''
input = 5

output:
5 bottles of beer on the wall, 
5 bottles of beer. 
Take one down, pass it around, 
4 bottles of beer on the wall.

4 bottles of beer on the wall, 
4 bottles of beer. 
Take one down, pass it around, 
3 bottles of beer on the wall.

3 bottles of beer on the wall, 
3 bottles of beer. 
Take one down, pass it around,*hic*
2 bottles of beer on the wall.

2 bOTTlEs of bEer on THe walL, 
2 boTTleS Of beEr. 
TaKe oNe dOwn, paSs It arounD, 
1 boTTle Of Beer On The waLl.

1 BooTTtlE OF beeR On The Wall, 
1 BOoTTlE OF  bEeR. 
TTaakkee oone dOWN, *hic*Ass Iit AaRoounnD, 
0 bOottles OF BeeEr  On tthhe WaLl.
 
Wheew, Thatt  WaaSs a mmOUTh  fULl!
'''
