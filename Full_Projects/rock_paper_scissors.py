#modules
import simple_colors
from random import randint, seed
from time import sleep
seed()

#intro/gamestate
print("-----Rock, Paper, Scissors game.-----")
conf = str(input(f'press {simple_colors.green("<Enter>")} to play.'))

if conf == '':
    continue_game = True
else:
    continue_game = False
    print("Goodbye.")
    exit()

#commands
commands = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
print("--------------------------")
print("choose one of the options:")
print("\t1 = Rock")
print("\t2 = Paper")
print("\t3 = Scissors")
print(f'To quit the game press {simple_colors.green("<q>")}')
print("--------------------------")

#scoreboard
player, ai = 0, 0

#engine
while continue_game:

    #inputs
    selection = input("Your choice: ")
    bot = randint(1, 3)

    #input check
    if selection == 'q':
        print("--------------------------------------------")
        print(f'Player score: {player}\n....AI score: {ai}.')
        print("Thank you for playing!")
        exit()
    elif int(selection) in range(1, 4):
        selection = int(selection)
    else:
        print("The value you inputed was incorrect.")
        print("please try again.\n")

    #game itself
    if selection == bot:
        print(f'You chose {commands[int(selection)]}')
        print(f'Bot chose...')
        sleep(2)
        print(f'{commands[bot]}.')
        print(simple_colors.yellow("Draw."))
    elif (selection == 1 and bot == 2) or (selection == 2 and bot == 3) or (selection == 3 and bot == 1):
        print(f'You chose {commands[int(selection)]}.')
        sleep(2)
        print(f'Bot chose {commands[int(bot)]}.')
        print(simple_colors.red('You lost.'))
        ai += 1
    elif (selection == 1 and bot == 3) or (selection == 2 and bot == 1) or (selection == 3 and bot == 2):
        print(f'You chose {commands[int(selection)]}.')
        sleep(2)
        print(f'Bot chose {commands[int(bot)]}.')
        print(simple_colors.green("Player won."))
        player += 1
