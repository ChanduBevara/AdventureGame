import time

def print_slow(text, delay=0.03):
    """
    Prints text slowly to create a more dramatic effect.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def adventure_game():
    print_slow("Welcome to the Mysterious Island Adventure Game!")
    print_slow("You find yourself on a deserted island with no memory of how you got here.")
    print_slow("Your goal is to explore the island and uncover its secrets.")
    print_slow("Let the adventure begin!\n")

    while True:
        print_slow("\nChoose your next action:")
        print("1. Explore the jungle")
        print("2. Investigate the beach")
        print("3. Rest by the campfire")
        print("4. Quit the game")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            print_slow("\nYou venture into the dense jungle.")
            print_slow("Suddenly, you hear a rustling sound in the bushes.")
            jungle_choice = input("Do you investigate further? (yes/no): ")
            if jungle_choice.lower() == 'yes':
                print_slow("\nYou discover a hidden treasure chest!")
                print_slow("Congratulations! You win!")
                break
            else:
                print_slow("\nYou decide not to investigate and return to the beach.")
        elif choice == '2':
            print_slow("\nYou walk along the sandy beach.")
            print_slow("You find a message in a bottle washed ashore.")
            print_slow("The message is illegible, but it intrigues you.")
        elif choice == '3':
            print_slow("\nYou sit by the campfire and enjoy the warmth.")
            print_slow("The stars above twinkle mysteriously.")
        elif choice == '4':
            print_slow("\nThanks for playing! See you next time.")
            break
        else:
            print_slow("\nInvalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    adventure_game()
