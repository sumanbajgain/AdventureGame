# This version of the game works, but is not compliant with the pyCodeStyle recommended
# syntax style. adventure_game_Refactored.py is the same version of this game, but
# is pyCodeStyle compliant.


import random
import time


def printPause(string):
    time.sleep(2)
    print(string)


creatures = ["dragon", "troll", "vampire", "killer bot", "hungry orc",
             "man-eating Minotaur"]


weakWeapons = ["rusty old knife", "walking stick", "wooden club",
               "rubber mallet", "rusty sword"]


strongWeapons = ["Valerian sword", "Magical Wand", "Ring of Infinite Power",
                 "Never-missing Crossbow", "Viking axe"]


def askChoice(choice1, choice2):
    validChoices = [str(choice1), str(choice2)]
    choice = input(f"Please enter '{choice1}' or '{choice2}'. \n")
    if str(choice) in validChoices:
        return int(choice)
    else:
        printPause(f"Invalid input. Please enter '{choice1}' "
                   f"or '{choice2}'. \n")
        return askChoice(choice1, choice2)


def askPlayAgain():
    printPause("Would you like to play again?")
    printPause("'1' for Yes, '2' for No.")
    choose = askChoice(1, 2)
    if choose == 1:
        printPause("Restarting the game. Good luck on your adventure.")
        startGame()
    else:
        printPause("Thank you for playing Adventure Game.")
        printPause("Hope to see you soon.")


def retreat():
    printPause(f"You retreat from the {villain}'s castle.")
    printPause(f"To your relief, the {villain} is not following you.")


def backToField():
    printPause("You are back on the field.")
    printPause("In front of you is a dilapidated castle.")
    printPause("To your right is a dark cave.")
    if 'beenToCave' in items:
        printPause(f"In your hand you hold your new and "
                   f"powerful {strongWeapon}.")
    else:
        printPause(f"In your hand you hold your trusty (but not very"
                   f" effective) {weakWeapon}.")
    printPause("Enter 1 to knock on the castle door.")
    printPause("Enter 2 to peer into the cave.")
    printPause("What would you like to do?")
    choices = askChoice(1, 2)
    if choices == 1:
        enterCastle()
    else:
        enterCave()


def enterCastle():
    printPause("You approach the castle door.")
    printPause(f"You are about to knock when the door"
               f" opens and out steps a {villain}.")
    printPause(f"This is the {villain}'s house. \n"
               f"The {villain} angrily runs toward you to attack!")
    if 'beenToCave' in items:
        printPause(f"You feel a rush of excitement as you tighten "
                   f"your grip on the {strongWeapon}!")
    else:
        printPause(f"You feel a bit under-prepared for this, what with"
                   f" only having a {weakWeapon}!")
    printPause("Would you like to fight (option 1) or run away (option 2)?")
    decision = askChoice(1, 2)
    if decision == 1:
        if 'beenToCave' in items:
            victory()
            askPlayAgain()
        else:
            youLose()
            askPlayAgain()
    if decision == 2:
        retreat()
        backToField()


def enterCave():
    if 'beenToCave' in items:
        printPause(f"You have already been to this cave "
                   f"and collected the {strongWeapon}.")
        printPause("There is nothing else to see here, so "
                   f"you return to the field.")
        backToField()
    else:
        printPause("You peer cautiously into the cave.")
        printPause("The cave appears to be small and uninhabitated.")
        printPause("You walk around the cave and catch a glimpse "
                   f"of something shiny!")
        printPause(f"It's a {strongWeapon}!")
        printPause(f"You grab the {strongWeapon} but vow to return "
                   f"it once your quest is over.")
        printPause(f"You leave your {weakWeapon} in the cave.")
        printPause(f"With a new found confidence, you leave the "
                   f"cave and head back to the field.")
        items.append('beenToCave')
        backToField()


def victory():
    printPause(f"The {villain} angrily runs toward you to attack!")
    printPause(f"This time, you have the newly acquired {strongWeapon} "
               f"and a sense of confidence, \n"
               f"so you brace yourself for the {villain}'s attack.")
    printPause(f"The {villain} instantly notices the {strongWeapon} "
               "and stops short in its tracks. \n"
               f"You seize the moment and use the {strongWeapon} to "
               "attack your opponent. ")
    printPause(f"The {villain} is instantly killed.")
    printPause(f"You are victorious!!! You have rid the world "
               f"of the evil {villain}.")
    printPause(f"Be sure to keep your promise and return the "
               f"{strongWeapon} to the cave.")


def youLose():
    printPause(f"You fight the {villain} with all your strength. ")
    printPause(f"However, the {villain} is just too strong and your "
               f"{weakWeapon} is no match for his wicked powers.")
    printPause("You have been defeated!")


def startGame():
    global items
    items = []
    global villain
    villain = random.choice(creatures)
    global weakWeapon
    weakWeapon = random.choice(weakWeapons)
    global strongWeapon
    strongWeapon = random.choice(strongWeapons)
    printPause("You find yourself standing in an open field, filled"
               " with grass and yellow wildflowers.")
    printPause(f"Rumor has it that a {villain} is somewhere around here,"
               " and has been terrifying the nearby village.")
    printPause("In front of you is a dilapidated castle.")
    printPause("To your right is a dark cave.")
    printPause(f"In your hand you hold your trusty (but not very"
               f" effective) {weakWeapon}.")
    printPause("Enter 1 to knock on the castle door.")
    printPause("Enter 2 to peer into the cave.")
    printPause("What would you like to do?")
    choices = askChoice(1, 2)
    if choices == 1:
        enterCastle()
    if choices == 2:
        enterCave()


startGame()

#Below is the version of Adventure Game that was first submitted for review.

# import random
# import time


# def printPause(string):
#     time.sleep(0.2)
#     print(string)


# creatures = ["dragon", "troll", "vampire", "killer bot", "hungry orc",
#              "man-eating Minotaur"]
# villain = random.choice(creatures)

# weakWeapons = ["rusty old knife", "walking stick", "wooden club",
#                "rubber mallet", "rusty sword"]
# weakWeapon = random.choice(weakWeapons)

# strongWeapons = ["Valerian sword", "Magical Wand", "Ring of Infinite Power",
#                  "Never-missing Crowssbow", "Viking axe"]
# strongWeapon = random.choice(strongWeapons)

# items = []


# def askChoice(choice1, choice2):
#     validChoices = [str(choice1), str(choice2)]
#     choice = input(f"Please enter '{choice1}' or '{choice2}'. \n")
#     if str(choice) in validChoices:
#         return int(choice)
#     else:
#         printPause(f"Invalid input. Please enter '{choice1}' "
#                    f"or '{choice2}'. \n")
        
        

# def askPlayAgain():
#     printPause("Would you like to play again?")
#     printPause("'1' for Yes, '2' for No.")
#     choose = askChoice(1, 2)
#     if choose == 1:
#         printPause("Restarting the game. Good luck on your adventure.")
#         startGame()
#     else:
#         printPause("Thank you for playing Adventure Game.")
#         printPause("Hope to see you soon.")


# def retreat():
#     printPause(f"You retreat from the {villain}'s castle.")
#     printPause(f"To your relief, the {villain} is not following you.")


# def backToField():
#     printPause("You are back on the field.")
#     printPause("In front of you is a dilapidated castle.")
#     printPause("To your right is a dark cave.")
#     if 'beenToCave' in items:
#         printPause(f"In your hand you hold your new and "
#                    f"powerful {strongWeapon}.")
#     else:
#         printPause(f"In your hand you hold your trusty (but not very"
#                    f" effective) {weakWeapon}.")
#     printPause("Enter 1 to knock on the castle door.")
#     printPause("Enter 2 to peer into the cave.")
#     printPause("What would you like to do?")
#     choices = askChoice(1, 2)
#     if choices == 1:
#         enterCastle()
#     else:
#         enterCave()


# def enterCastle():
#     printPause("You approach the castle door")
#     printPause(f"You are about to knock when the door"
#                f" opens and out steps a {villain}.")
#     printPause(f"This is the {villain}'s house. \n"
#                f"The {villain} angrily runs toward you to attack!")
#     if 'beenToCave' in items:
#         printPause(f"You feel a rush of excitement as you tighten "
#                    f"your grip on the {strongWeapon}!")
#     else:
#         printPause(f"You feel a bit under-prepared for this, what with"
#                    f" only having a {weakWeapon}!")
#     printPause("Would you like to fight (option 1) or run away (option 2)?")
#     decision = askChoice(1, 2)
#     if decision == 1:
#         if 'beenToCave' in items:
#             victory()
#             askPlayAgain()
#         else:
#             youLose()
#             askPlayAgain()
#     if decision == 2:
#         retreat()
#         backToField()


# def enterCave():
#     if 'beenToCave' in items:
#         printPause(f"You have already been to this cave "
#                    f"and collected the {strongWeapon}.")
#         printPause("There is nothing else to see here, so "
#                    f"you return to the field.")
#         backToField()
#     else:
#         printPause("You peer cautiously into the cave.")
#         printPause("The cave appears to be small and uninhabitated.")
#         printPause("You walk around the cave and catch a glimpse "
#                    f"of something shiny!")
#         printPause(f"It's a {strongWeapon}!")
#         printPause(f"You grab the {strongWeapon} but vow to return "
#                    f"it once your quest is over.")
#         printPause(f"You leave your {weakWeapon} in the cave.")
#         printPause(f"With a new found confidence, you leave the "
#                    f"cave and head back to the field.")
#         items.append('beenToCave')
#         backToField()


# def victory():
#     printPause(f"The {villain} angrily runs toward you to attack!")
#     printPause(f"This time, you have the newly acquired {strongWeapon} "
#                f"and a sense of confidence, \n"
#                f"so you brace yourself for the {villain}'s attack.")
#     printPause(f"The {villain} instantly notices the {strongWeapon} "
#                "and stops short in its tracks. \n"
#                f"You seize the moment and use the {strongWeapon} to "
#                "attack your opponent. ")
#     printPause(f"The {villain} is instantly killed.")
#     printPause(f"You are victorious!!! You have rid the world "
#                f"of the evil {villain}.")
#     printPause(f"Be sure to keep your promise and return the "
#                f"{strongWeapon} to the cave.")


# def youLose():
#     printPause(f"You fight the {villain} with all your strength. ")
#     printPause(f"However, the {villain} is just too strong and your "
#                f"{weakWeapon} is no match for his wicked powers.")
#     printPause("You have been defeated!")


# def startGame():
#     printPause("You find yourself standing in an open field, filled"
#                " with grass and yellow wildflowers.")
#     printPause(f"Rumor has it that a {villain} is somewhere around here,"
#                " and has been terrifying the nearby village.")
#     printPause("In front of you is a dilapidated castle.")
#     printPause("To your right is a dark cave.")
#     printPause(f"In your hand you hold your trusty (but not very"
#                f" effective) {weakWeapon}.")
#     printPause("Enter 1 to knock on the castle door.")
#     printPause("Enter 2 to peer into the cave.")
#     printPause("What would you like to do?")
#     choices = askChoice(1, 2)
#     if choices == 1:
#         enterCastle()
#     if choices == 2:
#         enterCave()


# startGame()


# Below is my incomplete program without the refactoring:

# def choices(choice):
#     choice = numericResponse()
#     return choice

# while True:
#     while True:
#         startGame()
#         # choice1
#         #numericResponse()
#         if response1 == "1":
#             printPause("You approach the castle door")
#             printPause(f"You are about to knock when the door"
#                         f" opens and out steps a {villain}.")
#             printPause(f"This is the {villain}'s house. \n"
#                         f"The {villain} angrily runs toward you to attack!")
#             printPause("You feel a bit under-prepared for this, what with"
#                         f" only having a {weakWeapon}!")
#             printPause("Would you like to fight (option 1) or run away (option 2)?")
#             response2 = input("(Please enter 1 or 2.)\n")
#             if response2 == "1":
#                 if strongWeapon in items:
#                     victory()
#                     askPlayAgain()
#                 else:
#                     youLose()
#                     askPlayAgain()
#                     if response3 == "n":
#                         printPause("Thank you for playing Adventure Game.")
#                         break
#                     elif response3 == "y":
#                         printPause("Restarting the game. Good luck.")

#                     else:
#                         printPause("Invalid input. Please enter 'y' or 'n'.\n")
#             elif response2 == "2":
#                 printPause(f"You retreat from the {villain}'s house.")
#                 printPause(f"To your relief, the {villain} is not following you.")
#             else:
#                 printPause("Invalid input. Please enter '1' or '2'. \n")
                



#         elif response1 == "2":
#             printPause("You peer cautiously into the cave.")
#             printPause("The cave appears to be small and uninhabitated.")
#             printPause("You walk around the cave and catch a glimpse of something shiny!")
#             printPause(f"It's a {strongWeapon}")
#             printPause(f"You grab the {strongWeapon} but vow to return it once your"
#                         f" quest is over. You leave your {weakWeapon} in the cave.")
#             printPause(f"With new found confidence, you leave the cave and head"
#                         " back to the field.")
#             printPause("Enter 1 to knock on the castle door.")
#             printPause("Enter 2 to peer into the cave.")
#             printPause("What would you like to do?")
#             response3 = input("(Please enter 1 or 2.\n)")
#             if response3 == "1":
#                 printPause(f"You head towards the mansion.")
#                 printPause(f"The {villain} angrily runs toward you to attack!")
#                 printPause(f"However, you are now confident and have {strongWeapon} to fight with, "
#                             f"so you brace yourself for the {villain}'s attack.")
#                 printPause(f"The {villain} instantly notices the {strongWeapon} and stops short "
#                             "in its tracks. \n"
#                             f"You seize the moment and use the {strongWeapon} to attack your opponent. ")
#                 printPause(f"The villain is instantly killed.")
#                 printPause("You are victorious!!!")
#                 printPause("Would you like to play again?")
#                 printPause("Please enter 'y' or 'n'.")
#                 # continue here.

#         else:
#             print("Invalid input. Please enter '1' or '2'. \n")

