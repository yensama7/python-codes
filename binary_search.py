import random
from math import log2
import sys
#***********************************opening*************************************************
def intro():
    the_list = list()
    for x in range (100):
        the_list.append(x)
    print("")
    print("think of a number from 1 - 100")
    print("")
    print("python has 7 tries")
    think_number= input("\nAre you done?\nEnter y for yes: ")
    if think_number != "y":
        print("\n please Enter y")
        return intro()
#*******************************************************************************************

    def binary_selection(list):

        game_count = 0
        low = 0
        high = len(the_list) - 1

        
        def the_game(list):
            nonlocal low
            nonlocal high
            nonlocal game_count

            def conclusion():
                if game_count == round(log2(100)):
                    print("python failed to guess the number you are thinking of🐍😢")
                    sys.exit()
                else:
                    print("python guessed the number correctly🐍🥳")
                    sys.exit()

#Binary selection block*******************************************************************************************
            while low <= high :
                mid = round((low + high)/2)
                guess = list[mid]
                question = input(f"\nis it, {guess}?\nEnter:\n1 : too high\n2 : too low\n3 : correct\n")
                try:
                    answer = int(question)
                except:
                    return the_game(the_list)

                if answer not in (1,2,3):
                    return the_game(the_list)
                elif answer == 1:
                    high = mid - 1
                elif answer == 2:
                    low = mid + 1
                else :
                    return conclusion()
                game_count += 1
                
                log = round(log2(100))
                if game_count == log :
                    return conclusion()
                return the_game(the_list)
#*********************************************************************************************************************
        the_game(the_list)

    binary_selection(the_list)
intro()