import random

def get_choice():
    print("Choose Rock, Paper or Scissors:")
    user_choice = input().lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        user_choice = input().lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif user_choice == 'rock':
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 'scissors':
        return "You win!" if computer_choice == 'paper' else "Computer wins!"
    elif user_choice == 'paper':
        return "You win!" if computer_choice == 'rock' else "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    user_choice = get_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = decide_winner(user_choice, computer_choice)
    print(result)

play_game()
