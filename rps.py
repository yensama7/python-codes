#Play a game of Rock, Paper and scissors with Python
def game():
    import random
    game_count = 0
    your_wins = 0
    your_loss = 0

    while True:
        print("")
        print("....................")
        print("Enter done to end game")
        print("....................")
        inp = input(
        "Enter ... \n1 for Rock, \n2 for Paper, \n3 for Scissors \n"
         )
        if inp.lower() == "done" :
            print("....................")
            print("Game count: ", game_count , "\n Your wins: ", your_wins, "\n your loss: ", your_loss)
            print("....................")
            break
        try:
            player = int(inp)
        except:
            print("Enter 1, 2 or 3 😒")
            continue
            quit()

        if player < 1 or player > 3 :
            print("enter 1, 2 or 3😒")
            continue

        compchoice = random.choice('123')
        comp= int(compchoice)

        def rps(inp):
            if inp == 1:
                return "Rock"
            elif inp == 2:
                return "Paper"
            elif inp == 3:
                return "Scissors"

        print("you chose ", rps(player) )
        print("python  chose ", rps(comp) )


        if player == 1 and comp == 3:
            your_wins += 1
            print("you win 🎉🥳")


        elif player == 2 and comp == 1:
            your_wins += 1
            print("you win 🎉🥳")


        elif player == 3 and comp == 2:
            your_wins += 1
            print("you win 🎉🥳")

        elif player == comp :
            print("Tie Game😮")

        else:
            your_loss += 1
            print("Python wins 🐍")

        game_count += 1

play = game()
play()
