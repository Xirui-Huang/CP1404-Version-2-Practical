import random

def main():
    """Main function to operate the score program."""
    print("Welcome to the Score Program.")
    user_score = get_valid_score()
    while True:
        print_menu()
        choice = input("Please enter your choice: ").upper()
        if choice == 'Q':
            break
        elif choice == 'G':
            user_score = get_valid_score()
        elif choice == 'V':
            print_score(user_score)
        elif choice == 'S':
            show_star(random_score())
        else:
            print("Invalid choice. Please choose again.")

def get_valid_score():
    """Prompt the user for a valid score between 0 and 100, inclusive."""
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a score between 0 and 100.")

def print_score(score):
    """Prints the qualitative score description based on the numeric score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    else:
        return "Bad"

def random_score():
    """Generate and return a random score."""
    return random.randint(0, 100)

def show_star(score):
    """Display asterisks equal to the score value."""
    print('*' * score)

def print_menu():
    """Prints the user options menu."""
    MENU_TEXT = """
    G - Get a new score
    V - View your score
    S - Show stars
    Q - Quit
    """
    print(MENU_TEXT)

if __name__ == "__main__":
    main()

