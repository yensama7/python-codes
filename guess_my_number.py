#customized game using the argparse module
#start game by typing py guess_my_number.py -n (gamer name) on the command line on windows using the directory it was saved
#start game by typing python3 guess_my_number.py -n (gamer name) on the command line on macbook using the directory it was saved
import random
import sys
import argparse

def guess_my_number(name):
    your_wins = 0
    game_count = 0
    your_loss = 0
    def the_game():
        nonlocal your_wins
        nonlocal your_loss
        nonlocal game_count
        player = input("Guess the number python is thinking of?\n1,2 or 3\n") 
        if player not in ["1", "2", "3"]:
            print("input 1, 2, 3")
            return the_game()
        comp = random.choice("123")
        print("")
        print(f"{name} chose ", player )
        print("python  chose ", comp) 
        print("")

        player_choice = int(player)
        computer_choice = int(comp) 

        def decide_winner(player_choice, computer_choice):
            nonlocal your_wins
            nonlocal your_loss
            nonlocal game_count 
            if player_choice == computer_choice :
                your_wins += 1
                return f"\n {name} wins 😁"
            else:
                your_loss += 1
                return "Python wins🐍"

#holds code for the score***********************************************
        def score():
            nonlocal game_count
            nonlocal your_loss
            nonlocal your_wins
            print("....................")
            print("Game count: ", game_count , "\n Yours wins: " , your_wins , "\n Your loss: ", your_loss)
            print("....................") 
            print("")
            def leave():
                xit = input("do you really want to leave?\ny or n\n ")
                xit = xit.lower()
                if xit not in ["y", "n"]:
                    return leave()
                elif xit == "n" :
                    return the_game()
                else:
                    ply_name = f"{name}"
                    print("Good bye", ply_name )
                    sys.exit()
            leave()
#*********************************************************************************



#play again?**********************************************************************     
        game_result = decide_winner(player_choice,computer_choice)
        print(game_result)
        
        game_count +=1

        print("would you like to play again?")
        def true():
            while True:
                play_again = input("y or n? \n")
                play = play_again.lower()
                if play not in ["y", "n"]:
                    return true()
                if play == "y" :
                    return the_game()
                else:
                    return score()
        true()
    return the_game
# ******************************************************************


#initiates the code*************************************************
if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="for a personalized gaming experience"
    )

    parser.add_argument(
        '-n', '--name', metavar='Name',
        required = True, help = 'for inputting name in code'
    )
    argu = parser.parse_args()


    guess_number = guess_my_number(argu.name)
    guess_number()
#******************************************************************