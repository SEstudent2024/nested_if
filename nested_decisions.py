# Nested Decisions: The Adventure Game 🏰
# Objective: To practice the use of nested if statements.

# Task 1: Code Correction You are provided with a Python script that is supposed to guide a user through an 
# adventure game, but it has some errors. Identify and fix them.

# Buggy Code:

place = input("Choose a place: forest or cave? ").strip().lower()

if place == "forest":
    action = input("Do you want to climb a tree or cross a river?").strip().lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("you found a boat!")
    else:
        print("Invalid choice. Please choose a valid action.")

# Task 2: Setting the Scene
# Based on your corrected code from Task 1, expand the game. If the user chooses "cave", 
# ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

elif place == "cave":
    action = input("Do you want to light a torch or proceed in the dark?").strip().lower()
    if action == "light a torch":
        print("The cave will have some light to help you find the hidden treasure!")
    elif action == "proceed in the dark":
        print("You will find it it difficult to find your way inside the cave in the dark.")
    else:
        print("Invalid choice. Please choose a valid action.")
else:
    print("Invalid choice. Please choose either forest or cave.")

    
# Task 3: Default Path
# If the user makes an invalid choice at any point, incorporate a pass statement to handle it. 
# HINT: How can an else statement be of use here?

if place not in ["forest", "cave"]:
    pass

