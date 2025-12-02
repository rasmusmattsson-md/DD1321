
import random

# Dictionary with win rules
win_rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

# List of options
options_list = ['rock', 'scissors', 'paper']

# Store points
player_points = 0
computer_points = 0

# Game loop. Continue until either gets 2 points
while player_points < 2 and computer_points < 2:
    # User chooses
    print("\nChoose: rock, scissors, or paper")
    user_choice = input("Your choice: ")
    
    # Computer chooses (randomly)
    random_index = random.randint(0, 2)
    computer_choice = options_list[random_index]
    print(f"Computer chose: {computer_choice}")
    
    # Determine winner
    if user_choice == computer_choice:
        print("Draw!")
    elif win_rules[computer_choice] == user_choice:
        computer_points += 1
        print("Computer wins this round!")
    else:
        player_points += 1
        print("You win this round!")
    
    # Print score
    print(f"Score - You: {player_points}, Computer: {computer_points}")

# Game winner
print("\n--- GAME OVER ---")
if player_points > computer_points:
    print("You won the game!")
else:
    print("The computer won the game.")
