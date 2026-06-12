import random
# Game Title and Introduction
def display_title():
    print("=" * 50)
    print("    MURDER MYSTERY: THE LOST DIAMOND")
    print("=" * 50)
    print()
# Create suspects using dictionaries
def create_suspects():
    suspects = [
        {
            "name": "Dr. James Wilson",
            "profession": "Museum Director",
            "motive": "He wanted to sell the diamond secretly",
            "alibi": "I was in my office reviewing documents",
            "interrogation": [
                "Q: Where were you during the theft?",
                "A: I was working late in my office, going over some paperwork.",
                "Q: Do you know anyone who would steal the diamond?",
                "A: Many people know about the diamond's value... *nervous laugh*"
            ]
        },
        {
            "name": "Emma Rodriguez",
            "profession": "Museum Security Guard",
            "motive": "She needed money for her sick daughter",
            "alibi": "I was patrolling the east wing",
            "interrogation": [
                "Q: Were you watching the diamond vault?",
                "A: Yes, I patrol that area every hour.",
                "Q: Did you see anyone suspicious?",
                "A: No... well, Dr. Wilson was acting strange earlier that evening."
            ]
        },
        {
            "name": "Marcus Chen",
            "profession": "Art Appraiser",
            "motive": "He has connections to diamond smugglers",
            "alibi": "I was cataloging artifacts in the storage room",
            "interrogation": [
                "Q: What were you doing in the storage room?",
                "A: Cataloging recently acquired artifacts, like always.",
                "Q: Do you have any ties to the black market?",
                "A: That's ridiculous! I'm a legitimate professional."
            ]
        }
    ]
    return suspects
# Display all suspects
def display_suspects(suspects):
    print("\n--- SUSPECTS ---")
    for index, suspect in enumerate(suspects, 1):
        print(f"{index}. {suspect['name']} - {suspect['profession']}")
    print()
# Interrogate a suspect
def interrogate_suspect(suspects, suspect_number):
    if suspect_number < 1 or suspect_number > len(suspects):
        print("Invalid suspect number!")
        return
   
    suspect = suspects[suspect_number - 1]
    print(f"\n--- INTERROGATING {suspect['name'].upper()} ---")
    print(f"Profession: {suspect['profession']}")
    print(f"Alibi: {suspect['alibi']}\n")
   
    # Display interrogation responses
    for line in suspect['interrogation']:
        print(line)
    print()
# Make an accusation
def make_accusation(suspects, accused_number, murderer_index):
    if accused_number < 1 or accused_number > len(suspects):
        print("Invalid suspect number!")
        return False
   
    accused = suspects[accused_number - 1]
    murderer = suspects[murderer_index]
   
    if accused_number - 1 == murderer_index:
        print(f"\n*** CORRECT! ***")
        print(f"{accused['name']} was the murderer!")
        print(f"Motive: {accused['motive']}")
        return True
    else:
        print(f"\n*** WRONG! ***")
        print(f"{accused['name']} is not the murderer.")
        print("Keep investigating...")
        return False
# Main game function
def play_game():
    display_title()
   
    # Game setup
    print("A priceless diamond has been stolen from the museum!")
    print("Three suspects are under investigation.")
    print("Interrogate them and find out who the murderer is!\n")
   
    # Create suspects and randomly choose murderer
    suspects = create_suspects()
    murderer_index = random.randint(0, 2)  # Random number 0, 1, or 2
   
    display_suspects(suspects)
   
    # Game loop
    game_won = False
    interrogations_done = 0
    max_interrogations = 5
   
    while not game_won and interrogations_done < max_interrogations:
        print("\n--- WHAT DO YOU WANT TO DO? ---")
        print("1. Interrogate a suspect")
        print("2. Make an accusation")
        print("3. Quit game")
       
        choice = input("\nEnter your choice (1-3): ").strip()
       
        if choice == "1":
            display_suspects(suspects)
            try:
                suspect_num = int(input("Enter suspect number to interrogate: "))
                interrogate_suspect(suspects, suspect_num)
                interrogations_done += 1
            except ValueError:
                print("Please enter a valid number!")
       
        elif choice == "2":
            display_suspects(suspects)
            try:
                accused_num = int(input("Enter suspect number to accuse: "))
                game_won = make_accusation(suspects, accused_num, murderer_index)
            except ValueError:
                print("Please enter a valid number!")
       
        elif choice == "3":
            print("\nThanks for playing!")
            return
       
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")
   
    if not game_won:
        print(f"\n*** GAME OVER ***")
        print(f"The murderer was: {suspects[murderer_index]['name']}")
        print(f"Motive: {suspects[murderer_index]['motive']}")
# Run the game
if __name__ == "__main__":
    play_game()
   
    # Ask if player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes" or play_again == "y":
        play_game()
    else:
        print("Goodbye!")
import random
# Game Title and Introduction
def display_title():
    print("=" * 50)
    print("    MURDER MYSTERY: THE LOST DIAMOND")
    print("=" * 50)
    print()
# Display the crime scene
def display_crime_scene():
    print("\n" + "=" * 50)
    print("         CRIME SCENE REPORT")
    print("=" * 50)
    print("""
Location: City Museum - Diamond Vault Room
Time of Theft: 9:30 PM, Friday Night
Victim: The "Hope Diamond" - a priceless gem worth $5 million
CRIME SCENE DETAILS:
- The vault was locked with a security code
- Only 4 people had access to the code: the three suspects and the director
- A security camera malfunction occurred at 9:20 PM
- A muddy footprint was found near the vault
- A coffee cup was left behind (fresh, still warm at time of discovery)
YOUR TASK: Find clues and interrogate the suspects to identify the thief!
""")
    print("=" * 50 + "\n")
# Create suspects using dictionaries
def create_suspects():
    suspects = [
        {
            "name": "Dr. James Wilson",
            "profession": "Museum Director",
            "motive": "He wanted to sell the diamond secretly",
            "alibi": "I was in my office reviewing documents",
            "clues": [
                "Clue: His shoes have fresh mud on them",
                "Clue: He knew the security code was about to change",
                "Clue: He has debts from gambling"
            ],
            "interrogation": [
                "Q: Where were you during the theft?",
                "A: I was working late in my office, going over some paperwork.",
                "Q: Do you know anyone who would steal the diamond?",
                "A: Many people know about the diamond's value... *nervous laugh*"
            ]
        },
        {
            "name": "Emma Rodriguez",
            "profession": "Museum Security Guard",
            "motive": "She needed money for her sick daughter",
            "alibi": "I was patrolling the east wing",
            "clues": [
                "Clue: She called in sick three times this month",
                "Clue: Her security badge was used to access the vault",
                "Clue: Witness saw her near the vault around 9:15 PM"
            ],
            "interrogation": [
                "Q: Were you watching the diamond vault?",
                "A: Yes, I patrol that area every hour.",
                "Q: Did you see anyone suspicious?",
                "A: No... well, Dr. Wilson was acting strange earlier that evening."
            ]
        },
        {
            "name": "Marcus Chen",
            "profession": "Art Appraiser",
            "motive": "He has connections to diamond smugglers",
            "alibi": "I was cataloging artifacts in the storage room",
            "clues": [
                "Clue: The coffee cup left at the scene matches his brand",
                "Clue: He received a mysterious phone call at 9:25 PM",
                "Clue: He has contacts with known smugglers overseas"
            ],
            "interrogation": [
                "Q: What were you doing in the storage room?",
                "A: Cataloging recently acquired artifacts, like always.",
                "Q: Do you have any ties to the black market?",
                "A: That's ridiculous! I'm a legitimate professional."
            ]
        }
    ]
    return suspects
# Display all suspects
def display_suspects(suspects):
    print("\n--- SUSPECTS ---")
    for index, suspect in enumerate(suspects, 1):
        print(f"{index}. {suspect['name']} - {suspect['profession']}")
    print()
# Display collected clues
def display_clues(clues_found):
    print("\n--- CLUES COLLECTED ---")
    if len(clues_found) == 0:
        print("No clues collected yet. Interrogate suspects to find clues!")
    else:
        for index, clue in enumerate(clues_found, 1):
            print(f"{index}. {clue}")
    print()
# Interrogate a suspect
def interrogate_suspect(suspects, suspect_number, clues_found):
    if suspect_number < 1 or suspect_number > len(suspects):
        print("Invalid suspect number!")
        return
   
    suspect = suspects[suspect_number - 1]
    print(f"\n--- INTERROGATING {suspect['name'].upper()} ---")
    print(f"Profession: {suspect['profession']}")
    print(f"Alibi: {suspect['alibi']}\n")
   
    # Display interrogation responses
    for line in suspect['interrogation']:
        print(line)
   
    # Add this suspect's clues to the clues found
    print("\n[New clues discovered during interrogation!]")
    for clue in suspect['clues']:
        if clue not in clues_found:  # Only add if not already collected
            clues_found.append(clue)
            print(f"  + {clue}")
    print()
# Make an accusation
def make_accusation(suspects, accused_number, murderer_index):
    if accused_number < 1 or accused_number > len(suspects):
        print("Invalid suspect number!")
        return False
   
    accused = suspects[accused_number - 1]
    murderer = suspects[murderer_index]
   
    if accused_number - 1 == murderer_index:
        print(f"\n*** CORRECT! ***")
        print(f"{accused['name']} was the murderer!")
        print(f"Motive: {accused['motive']}")
        return True
    else:
        print(f"\n*** WRONG! ***")
        print(f"{accused['name']} is not the murderer.")
        print("Keep investigating...")
        return False
# Main game function
def play_game():
    display_title()
   
    # Display crime scene
    display_crime_scene()
   
    # Game setup
    print("A priceless diamond has been stolen from the museum!")
    print("Three suspects are under investigation.")
    print("Interrogate them and find out who the murderer is!\n")
   
    # Create suspects and randomly choose murderer
    suspects = create_suspects()
    murderer_index = random.randint(0, 2)  # Random number 0, 1, or 2
    clues_found = []  # List to store collected clues
   
    display_suspects(suspects)
   
    # Game loop
    game_won = False
    interrogations_done = 0
    max_interrogations = 5
   
    while not game_won and interrogations_done < max_interrogations:
        print("\n--- WHAT DO YOU WANT TO DO? ---")
        print("1. Interrogate a suspect")
        print("2. View clues")
        print("3. Make an accusation")
        print("4. Quit game")
       
        choice = input("\nEnter your choice (1-4): ").strip()
       
        if choice == "1":
            display_suspects(suspects)
            try:
                suspect_num = int(input("Enter suspect number to interrogate: "))
                interrogate_suspect(suspects, suspect_num, clues_found)
                interrogations_done += 1
            except ValueError:
                print("Please enter a valid number!")
       
        elif choice == "2":
            display_clues(clues_found)
       
        elif choice == "3":
            display_suspects(suspects)
            try:
                accused_num = int(input("Enter suspect number to accuse: "))
                game_won = make_accusation(suspects, accused_num, murderer_index)
            except ValueError:
                print("Please enter a valid number!")
       
        elif choice == "4":
            print("\nThanks for playing!")
            return
       
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
   
    if not game_won:
        print(f"\n*** GAME OVER ***")
        print(f"The murderer was: {suspects[murderer_index]['name']}")
        print(f"Motive: {suspects[murderer_index]['motive']}")
# Run the game
if __name__ == "__main__":
    play_game()
   
    # Ask if player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes" or play_again == "y":
        play_game()
    else:
        print("Goodbye!")
import random
# Game Title and Introduction
def display_title():
    print("=" * 50)
    print("    MURDER MYSTERY: THE LOST DIAMOND")
    print("=" * 50)
    print()
# Display the crime scene
def display_crime_scene():
    print("\n" + "=" * 50)
    print("         CRIME SCENE REPORT")
    print("=" * 50)
    print("""
Location: City Museum - Diamond Vault Room
Time of Theft: 9:30 PM, Friday Night
Victim: The "Hope Diamond" - a priceless gem worth $5 million
CRIME SCENE DETAILS:
- The vault was locked with a security code
- Only 4 people had access to the code: the three suspects and the director
- A security camera malfunction occurred at 9:20 PM
- A muddy footprint was found near the vault
- A coffee cup was left behind (fresh, still warm at time of discovery)
YOUR TASK: Find clues and interrogate the suspects to identify the thief!
""")
    print("=" * 50 + "\n")
# Create suspects using dictionaries
def create_suspects():
    suspects = [
        {
            "name": "Dr. James Wilson",
            "profession": "Museum Director",
            "motive": "He wanted to sell the diamond secretly",
            "alibi": "I was in my office reviewing documents",
            "clues": [
                "Clue: His shoes have fresh mud on them",
                "Clue: He knew the security code was about to change",
                "Clue: He has debts from gambling"
            ],
            "interrogation": [
                "Q: Where were you during the theft?",
                "A: I was working late in my office, going over some paperwork.",
                "Q: Do you know anyone who would steal the diamond?",
                "A: Many people know about the diamond's value... *nervous laugh*"
            ]
        },
        {
            "name": "Emma Rodriguez",
            "profession": "Museum Security Guard",
            "motive": "She needed money for her sick daughter",
            "alibi": "I was patrolling the east wing",
            "clues": [
                "Clue: She called in sick three times this month",
                "Clue: Her security badge was used to access the vault",
                "Clue: Witness saw her near the vault around 9:15 PM"
            ],
            "interrogation": [
                "Q: Were you watching the diamond vault?",
                "A: Yes, I patrol that area every hour.",
                "Q: Did you see anyone suspicious?",
                "A: No... well, Dr. Wilson was acting strange earlier that evening."
            ]
        },
        {
            "name": "Marcus Chen",
            "profession": "Art Appraiser",
            "motive": "He has connections to diamond smugglers",
            "alibi": "I was cataloging artifacts in the storage room",
            "clues": [
                "Clue: The coffee cup left at the scene matches his brand",
                "Clue: He received a mysterious phone call at 9:25 PM",
                "Clue: He has contacts with known smugglers overseas"
            ],
            "interrogation": [
                "Q: What were you doing in the storage room?",
                "A: Cataloging recently acquired artifacts, like always.",
                "Q: Do you have any ties to the black market?",
                "A: That's ridiculous! I'm a legitimate professional."
            ]
        }
    ]
    return suspects
# Display all suspects
def display_suspects(suspects):
    print("\n--- SUSPECTS ---")
    for index, suspect in enumerate(suspects, 1):
        print(f"{index}. {suspect['name']} - {suspect['profession']}")
    print()
# Display collected clues
def display_clues(clues_found):
    print("\n--- CLUES COLLECTED ---")
    if len(clues_found) == 0:
        print("No clues collected yet. Interrogate suspects to find clues!")
    else:
        for index, clue in enumerate(clues_found, 1):
            print(f"{index}. {clue}")
    print()
# Interrogate a suspect
def interrogate_suspect(suspects, suspect_number, clues_found):
    if suspect_number < 1 or suspect_number > len(suspects):
        print("Invalid suspect number!")
        return
   
    suspect = suspects[suspect_number - 1]
    print(f"\n--- INTERROGATING {suspect['name'].upper()} ---")
    print(f"Profession: {suspect['profession']}")
    print(f"Alibi: {suspect['alibi']}\n")
   
    # Display interrogation responses
    for line in suspect['interrogation']:
        print(line)
   
    # Add this suspect's clues to the clues found
    print("\n[New clues discovered during interrogation!]")
    for clue in suspect['clues']:
        if clue not in clues_found:  # Only add if not already collected
            clues_found.append(clue)
            print(f"  + {clue}")
    print()
# Make an accusation
def make_accusation(suspects, accused_number, murderer_index):
    if accused_number < 1 or accused_number > len(suspects):
        print("Invalid suspect number!")
        return False
   
    accused = suspects[accused_number - 1]
    murderer = suspects[murderer_index]
   
    if accused_number - 1 == murderer_index:
        print(f"\n*** CORRECT! ***")
        print(f"{accused['name']} was the murderer!")
        print(f"Motive: {accused['motive']}")
        return True
    else:
        print(f"\n*** WRONG! ***")
        print(f"{accused['name']} is not the murderer.")
        print("Keep investigating...")
        return False
# Main game function
def play_game():
    display_title()
   
    # Display crime scene
    display_crime_scene()
   
    # Game setup
    print("A priceless diamond has been stolen from the museum!")
    print("Three suspects are under investigation.")
    print("Interrogate them and find out who the murderer is!\n")
   
    # Create suspects and randomly choose murderer
    suspects = create_suspects()
    murderer_index = random.randint(0, 2)  # Random number 0, 1, or 2
    clues_found = []  # List to store collected clues
   
    display_suspects(suspects)
   
    # Game loop
    game_won = False
    interrogations_done = 0
    max_interrogations = 5
   
    while not game_won and interrogations_done < max_interrogations:
        print("\n--- WHAT DO YOU WANT TO DO? ---")
        print("1. Interrogate a suspect")
        print("2. View clues")
        print("3. Make an accusation")
        print("4. Quit game")
       
        choice = input("\nEnter your choice (1-4): ").strip()
       
        if choice == "1":
            display_suspects(suspects)
            try:
                suspect_num = int(input("Enter suspect number to interrogate: "))
                interrogate_suspect(suspects, suspect_num, clues_found)
                interrogations_done += 1
            except ValueError:
                print("Please enter a valid number!")
       
        elif choice == "2":
            display_clues(clues_found)
       
        elif choice == "3":
            display_suspects(suspects)
            try:
                accused_num = int(input("Enter suspect number to accuse: "))
                game_won = make_accusation(suspects, accused_num, murderer_index)
            except ValueError:
                print("Please enter a valid number!")
       
        elif choice == "4":
            print("\nThanks for playing!")
            return
       
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
   
    if not game_won:
        print(f"\n*** GAME OVER ***")
        print(f"The murderer was: {suspects[murderer_index]['name']}")
        print(f"Motive: {suspects[murderer_index]['motive']}")
# Run the game
if __name__ == "__main__":
    play_game()
   
    # Ask if player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes" or play_again == "y":
        play_game()
    else:
        print("Goodbye!")