#jacob
#oct.25, 2024
#bomb game

print("loading.", end= '\r')

#Note: to run this program, you must install colorama to python. this is installed by default on thonny. to install, use cmd c:\users\user>'py -m pip install colorama" on windows.

#this question generator is fully customizable for any time
#to use call the function with your choices in the brackets with a '#' inbetween each answer
#make sure the charicters are all lower case and there is no extra spaces after the answers
#example: genchoice('type:','a#b#c') --> output to shell: type: a, b or c:
#after the user answers, the function will return the index for that answer (0, 1, 2...)  
def question_gen(prompt, ans):
    anslist = ans.split('#')#splitting the single string into a list
    choices = make_prompt(anslist)#promt generator function
    while 1:
        userans=input(f"{prompt} {choices}: ").lower().strip()#user unput (non case sensitive)
        try:
            ansindex = anslist.index(userans)#find the index of the users answer
            return ansindex
        except:
            print("Try again")#if the user does not enter one of the options
            continue

def make_prompt(ans):
    choices = ans[0]#first choice
    y=0 #y var to count the loops
    for _ in ans:
        y+=1
        if y+1 == len(ans):
            choices= choices + " or " + ans[y] #adding "or" to the prompt string
            break
        choices = choices + ", " + ans[y] #adding commas to the prompt string
    return choices

#Start of the game
def game_start():
    #start text:
    print("welcome to the game, player. You wake up in a dark room with no recolection of how you got there. \nIn front of you is a table with a strange beeping box. \nAfter closer inspection, you recognize the box as a bomb!")
    input("\nPress enter to continue... ")
    #first question:
    question=question_gen("\n\nDo you want to pick up the bomb, search the rest of the room or give up?\nType:","bomb#search#give up")
    if question == 0:
        bomb()#pick up the bomb
    elif question == 1:
        search()#search the room
    elif question == 2:
        giveup()#quit the game

#↓↓###################first 3 options####################↓↓
def bomb():
    if data_list[8] is True:#check if the user has seen the bomb desc before.
        print("\nThe bomb on the table is a box with Four sides.\nOne has a timer, one has a blue button that says 'HOLD'\none has a keypad and the last side has two wires.")
        data_list[8] = False#mark the bomb description as false so it wont print again
    print("\ndo you want to defuse the bomb, look closer at the bomb, or set it down and look for clues?")
    question = question_gen("Type:","defuse#look closer#go back")#choose what to do after picking up the bomb
    if question == 0:
        defuse()#pick a module
    elif question == 1:
        look_closer()#look at bomb id   
    elif question == 2:
        search()#set the bomb down

def search():
    if data_list[9] is True:#check if the user has read the room description
        print("\nThe room you are in is made of dark brick. there are pipes and wires high up in the celing. The table in front of you has a bomb and a pair of wirecutters\nbehind you is a dark metal door, and a industrial light obove the door. There appears to be somthing under your desk as well.")
        data_list[9] = False#mark the room description as false so it wont print again
    question = question_gen("\nWhat do you want to do?\nType:","look under desk#look at door#bomb")
    if question == 0:
        trashcan()#look under the desk
    elif question == 1:
        door()#look at the door
    elif question == 2:
        bomb()#pick up the bomb
        
def giveup():#quitting the game
    print("You give up on doing anything and let the bomb's timer run out. after an agonizingly long time, The bomb blows up and you die")
    game_end()#loose the game
#↑↑###############first 3 choices####################↑↑

#↓↓############after choice 'bomb'################↓↓
def defuse():#choosing what part of the bomb you want to defuse
    print("\n\nWhat module do you want to defuse?, or do you want to go back in the room?")
    question=question_gen("Type:","wires#keypad#button#go back")
    if question == 0:
        wires()#wires module
    elif question == 1:
        keypad()#keypad module
    elif question == 2:
        button()#button module
    else:
        bomb()

def look_closer():#the bomb's id will be printed
    print("\nyou find the id '" + Fore.LIGHTCYAN_EX + f"{data_list[1]}" + Fore.RESET + "' written on the side of the bomb.")
    sleep(1)#delay
    bomb()#back to the bomb
#↑↑############after choice 'bomb'#################↑↑

#↓↓############after choice 'search'###############↓↓
def trashcan():#the instructions on how to defuse the bomb (with colored text)
    print("\nUnder the desk is a metal wire trash can. You dig around in the trash can and find some gum wrappers and a crumpled up page. \nUncrumpling the page reveals some numbers written on it:\n")
    print(Back.LIGHTWHITE_EX+Fore.LIGHTBLACK_EX+"'The bomb's keypad code is:"+Fore.CYAN+f'{data_list[2]}')
    if data_list[3] == 1:
        print(Back.LIGHTWHITE_EX+Fore.LIGHTBLACK_EX+"The wire you must cut is: "+Fore.RED+'RED   ')
    else:
        print(Back.LIGHTWHITE_EX+Fore.LIGHTBLACK_EX+"The wire you must cut is: "+Fore.BLUE+"BLUE' ")
    search()#return to the room

def door():#the description of the door
    print("\nIt is a solid metal door with a large metal handle. you push and pull on the door but it is locked tight.\nAbove the door is a large red light casting the room in its ereie glow. \nA paper is sticking out of the handle. after putting it out it reads:\n\n"+Back.LIGHTWHITE_EX+Fore.LIGHTBLACK_EX+"'Remember: quickly press the HOLD button                            ","\n"+Back.LIGHTWHITE_EX+Fore.LIGHTBLACK_EX+"You will need the bomb id as well, which is on the side of the bomb'")
    sleep(6)#delay
    search()#return to the room
#↑↑############after choice 'search'###############↑↑

#↓↓############after choice 'defuse'###############↓↓
def wires():#the wires module of the bomb
    if data_list[5] is False:#see if the user has defused this part of the bomb before
        question = question_gen("\nWhich wire do you want to cut?\nType:","red#blue#go back")
        if question == 0:
            red_wire()#cut the red wire
        elif question == 1:
            blue_wire()#cut the blue wire
        else:
            defuse()#go back
    else:
        print("\nyou already finished the wires, do another one")#if the user has done this module before
        sleep(2)#delay
        defuse()#go back

def keypad():
    if data_list[6] is False:#see if the user has defused this part of the bomb before
        
        keyin = input("The keypad has 5 digits it accepts, as well as letters just like a flipphone.\nDo you have a number?\nEnter number or go back: ").strip()
        if keyin == str(data_list[2]):#check if the number was correct
            win_condition('keypad')
        elif keyin == "go back":
            defuse()
        else:
            strike()#incorrect number
            defuse()
    else:
        print("\nyou already finished the keypad, do another one")#if the user has done this module before
        sleep(2)
        defuse()

def button():      
    if data_list[7] is False:#see if the user has defused this part of the bomb before
        print("There is a blue button that says 'HOLD'",Fore.LIGHTBLUE_EX+"""
            *  *
         *        *
        *   HOLD   *
        *          *
         *        *
            *  *""")
        question = question_gen("Do you hold the button down, or press it and relese it?\nType:","press#press and hold")
        if question == 1:
            print(Fore.LIGHTRED_EX+"\nIncorrect!","You were fell for the button's text and held the button")#if the user holds the button
            strike()
            defuse()
        else:
            keyin = input("Text pops up above the button to enter the device ID.\nEnter bomb ID or go back: ").strip().lower()
            if keyin == str(data_list[1]).lower():
                    win_condition('button')
            elif keyin ==  "go back":
                defuse()#go back
            else:#incorrect guess
                print(Fore.LIGHTRED_EX+"\nIncorrect!","The ID you entered was incorrect")
                strike()       
    else:#if the user has finished this module
        print("\nyou already finished the button, do another one")
        sleep(2)#delay
        defuse()#go back
#↑↑############after choice 'defuse'###############↑↑

#↓↓############after choice 'wires'###############↓↓
def red_wire():#the user chose the red wire
    if data_list[3] == 2:#if the red wire is incorrect
        print(Fore.LIGHTRED_EX+"\nIncorrect!", "That was the wrong wire")
        strike() 
    else:#if the red wire is correct
        print("\nYou cut the red wire")
        win_condition('wires')#greenlight with which module was defused

def blue_wire():#the user chose the blue wire
    if data_list[3] == 1:#if the blue wire is incorrect
        print(Fore.LIGHTRED_EX+"\nIncorrect!", "That was the wrong wire")
        strike()
    else:#if the blue wire is correct
        print("You cut the blue wire")
        win_condition('wires')#greenlight with which module was defused
#↑↑############after choice 'wires'###############↑↑
 
#↓↓##############data and misc#################↓↓
def code_gen():#main data used across the game:
    strikes = 3#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .#[0]
    bombid = ''.join(random.choice(ascii_uppercase + digits) for _ in range(5))# #[1]
    keypass = random.randint(10000,99999)#. . . . . . . . . . . . . . . . . . . .#[2]
    wire = random.randint(1,2)#. . . . . . . . . . . . . . . . . . . . . . . . . #[3]
    green_light = 3#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .#[4]
    wire_light = False#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . #[5]
    keypad_light = False# . . . . . . . . . . . . . . . . . . . . . . . . . . . .#[6]
    button_light = False#. . . . . . . . . . . . . . . . . . . . . . . . . . . . #[7]
    bomb_desc = True# . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .#[8]
    room_desc = True#. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . #[9]
    return [strikes, bombid, keypass, wire, green_light, wire_light, keypad_light, button_light, bomb_desc, room_desc]#return the data into one string

def win_condition(module):#guessibg correctly
    print(Fore.LIGHTGREEN_EX+"\nCorrect!")
    if data_list[4] > 1:#check if you have more modules of the bomb to solve
        print(f"\nThe light obove the {module} has turned green, meaning you have compleated that part of the bomb.")
        data_list[4] -= 1#subtract one from the total amount of correct guesses to win
        if module == 'wires':
            data_list[5] = True #correct wire
        elif module == 'keypad':
            data_list[6] = True #correct keypad code
        else:
            data_list[7] = True #correct button ID code
        defuse()
    else:#win the game
        print("\nYou Defused the bomb! the red light above the door starts to flash and the door opens for you to leave!")
        game_end()

def strike():#guessing incorrectly results in a strike 
    data_list[0]-=1 #subtract one from the strikes counter
    if data_list[0] == 2: #prompt for the first strike
        print("The steady beeping noice has incresed, and a red", Fore.RED + "x" + Fore.RESET, "has appeared above the timer. \nNext to the red x is an uneluminated 'x' sign meaning there are two strikes untill the bomb explodes for good.  \nYou have", Fore.LIGHTBLUE_EX + f'{data_list[0]}' + Fore.RESET, "strikes remaining.\nWhy dont you try looking in the room for clues?")
        defuse()
    elif data_list[0] == 1:#prompt fpr the second strike
        print("The steady beeping noice has incresed again, and another red", Fore.RED + "x" + Fore.RESET, "has appeared above the timer. \nBoth x's have gone red meaning there is one strike untill the bomb explodes for good.  \nYou have", Fore.LIGHTBLUE_EX + f'{data_list[0]}' + Fore.RESET, "strike remaining.\nWhy dont you try looking in the room for clues?")
        defuse()
    else:#after 3 strikes
        print("After the last red 'x' appears the timer is going too fast for you to react. The bomb blows up and you die")
        game_end()
#↑↑##############data and misc#################↑↑

#↓↓##############end of the game###############↓↓
def game_end():#the end of the game
    question = question_gen("\nThanks for playing! Do you want to play again?","yes#no")
    if question == 0:#play again
        print("\n"*10)
        game_start()
#↑↑##############end of the game###############↑↑

#main code & imports
from time import sleep
import random
from string import ascii_uppercase, digits
from colorama import Fore, Back, init
init(autoreset=True)#some coloured text formatting
data_list = code_gen()#generate all the codes, strikes and other global variables in one list
game_start()