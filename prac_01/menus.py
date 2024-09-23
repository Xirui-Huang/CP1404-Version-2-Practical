# Get user's name
name = input("Enter name: ")

# Display menu initially
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")

# Get user's choice and convert to uppercase
choice = input(">>> ").upper()

# Loop until the user decides to quit
while choice != 'Q':
    if choice == 'H':
        print(f"Hello {name}")
    elif choice == 'G':
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    # Display menu again
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    # Get the next choice
    choice = input(">>> ").upper()

# Print finished message once the user quits
print("Finished.")
