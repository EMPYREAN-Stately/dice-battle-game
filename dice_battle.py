import random

print("Welcome Players in the Dice Battle Game!")
print("First to achieve 5 points will win the Game.\n")

player1_name = input("Enter Player 1 name: ")
player2_name = input("Enter Player 2 name: ")
print()


def roll_dice():
    return random.randint(1, 6)


def play_game():
    player1 = 0
    player2 = 0
    rounds = 1

    while player1 < 5 and player2 < 5:
        input(f"Round {rounds} - Press Enter to roll the dice...")

        player1_roll = roll_dice()
        player2_roll = roll_dice()

        print(f"{player1_name} rolled: {player1_roll}")
        print(f"{player2_name} rolled: {player2_roll}")

        if player1_roll > player2_roll:
            player1 += 1
            print(f"{player1_name} wins this round!\n")
        elif player2_roll > player1_roll:
            player2 += 1
            print(f"{player2_name} wins this round.\n")
        else:
            print("It's a tie!\n")

        print(
            f"Score => {player1_name}: {player1} | {player2_name}: {player2}\n")
        rounds += 1

    if player1 > player2:
        print(f"Hurray {player1_name} won the game!")
    else:
        print(f"Hurray {player2_name} won the game!")


if __name__ == "__main__":
    play_game()
