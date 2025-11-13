import random

def play_game():
    item_list = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        comp_choice = random.choice(item_list)

        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {comp_choice}")

        if user_choice not in item_list:
            print("Invalid choice! Please choose rock, paper, or scissors.\n")
            continue

        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            print("🎉 You win!")
        else:
            print("😢 You lose!")

        again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing! 👋")
            break


# Main start point
start = input("Do you want to start the Rock, Paper, Scissors game? (yes/no): ").strip().lower()
if start == 'yes':
    play_game()
else:
    print("Okay, maybe next time! 👋")
