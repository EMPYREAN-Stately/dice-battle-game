from game_logic import play_game

print("Welcome Players in the Dice Battle Game!")
print("First to achieve 5 points will win the Game.\n")

player1_name = input("Enter Player 1 name: ")
player2_name = input("Enter Player 2 name: ")
print()

if __name__ == "__main__":
    play_game(player1_name, player2_name)
