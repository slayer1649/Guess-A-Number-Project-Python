import random

comp_move = random.randint(1, 10)

while True:
    player_input = input("Guess the number (1-10): ")

    if not player_input.isdigit():
        print("Invalid input. Type a number!")
        continue

    player_number = int(player_input)

    if player_number == comp_move:
        print("You guess it!")
        break
    elif player_number > comp_move:
        print("Too High!")
    else:
        print("Too Low!")
