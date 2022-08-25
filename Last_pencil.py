import random

players = ['John', 'Jack']
possible_moves = ['1', '2', '3']

print('How many pencils would you like to use:')

while True:

    pencils = input()
    if pencils.isnumeric() is False or int(pencils) < 0:
        print('The number of pencils should be numeric')
        continue
    elif int(pencils) == 0:
        print('The number of pencils should be positive')
        continue
    else:
        pencils = int(pencils)
        player = str(input('Who will be the first (John, Jack):\n'))

        if player not in players:
            player = str(input(f"Choose between '{players[0]}' and '{players[1]}'\n"))
            while player not in players:
                player = str(input(f"Choose between '{players[0]}' and '{players[1]}'\n"))

        while pencils > 0:

            lines = '|' * pencils
            print(lines)

            if player == players[0]:
                print(f"{player}'s turn!")
                move = input()
                while move not in possible_moves:
                    move = input("Possible values: '1', '2' or '3'\n")
                while pencils - int(move) < 0:
                    move = input('Too many pencils were taken\n')

            elif player == players[1]:
                if pencils % 4 == 0:
                    move = '3'
                elif pencils % 4 == 3:
                    move = '2'
                elif pencils % 4 == 2:
                    move = '1'
                elif pencils % 4 == 1:
                    move = '1'
                else:
                    current_move = random.randint(1, 3)
                print(f"{player}'s turn:")
                print(move)

            pencils -= int(move)
            player = players[players.index(player) - 1]

    print(f'{player} won!')
    break
