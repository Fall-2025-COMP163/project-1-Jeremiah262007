import os
"""
COMP 163 - Project 1: Character Creator & Saving/Loading
Name: Jeremiah Cooper
Date: 10/23/2025

AI Usage: I consulted ChatGPT for guidance on stat-scaling formulas, file I/O structure, and debugging issues. 
The AI helped brainstorm class stat formulas, suggested safe file read/write patterns without try/except, 
and identified logic bugs (like indentation and return-order errors) in calculate_stats(). 
It also recommended adding directory checks in save_character() and refining load_character() parsing 
to match the required format. 
I designed and finalized all stat formulas, implemented and tested all functions myself, 
and ensured the final code met all project specifications.
"""

def starting_equiment(character_class):
    """
    Returns a list of starting weapon equipment that the character has based on their class.
    
    """

    # Normalize capitalization to ensure consistency
    character_class = character_class.strip().capitalize()

    # Use simple formulas for each class type and assign weapon equipment
    if character_class == "Warrior":
        return["Sword", "Shield", "Axe"]
    if character_class == "Mage":
        return["Invisible Cloak", "Wand", "Spell Book"]
    if character_class == "Rogue":
        return["Dagger", "Bow & Arrow", "Cloak"]
    if character_class == "Cleric":
        return["Godkiller", "Mace", "Holy Incantations"]
    if character_class == "Prisoner":
        return["Shank", "Jumpsuit", "Chained Whips"]
    if character_class == "Devil":
        return["Shapeshifting", "Crossbow", "Mind Control"]
    if character_class == "Angel":
        return["Flight", "Reality Warping", "Regeneration"]
    else:
        # Default for unrecognized classes
        return["Katana", "Gun", "Dog"]

def create_character(name, character_class):
    """
    Creates a new character dictionary with calculated stats.
    Returns: dictionary with keys: name, class, level, strength, magic, health, gold
    
    Example:
    char = create_character("Aria", "Mage")
    # Should return: {"name": "Aria", "class": "Mage", "level": 1, "strength": 5, "magic": 15, "health": 80, "gold": 100}
    """
    level = 1  # All new characters start at level 1
    
    # Use helper function to calculate stats based on class and level
    strength, magic, health, dexterity, stealth = calculate_stats(character_class, level)
    
    # Store all character data in a dictionary
    character = {
        "name": name,
        "class": character_class,  # Keep capitalization as entered
        "level": level,
        "strength": strength,
        "dexterity": dexterity,
        "stealth": stealth,
        "magic": magic,
        "health": health,
        "gold": 100,
        "equipment": starting_equiment(character_class)  # All new characters start with 100 gold
    }
    return character


def calculate_stats(character_class, level):
    """
    Calculates base stats based on class and level.
    Returns: tuple of (strength, magic, health, dexterity, stealth)
    Returns None if class is invalid.

    Example formulas (customizable):
    - Warrior: High strength, high health, low magic
    - Mage: High magic, low health and strength
    - Rogue: Balanced stats
    - Cleric: Good magic and health, medium strength
    - Prisoner: Rough minded indivduals who grinds with strength and health but has the opportunity to learn 
    - Devil: Embodiment of Evil
    - Angel: Embodiment of Good
    """
    # Normalize capitalization to ensure consistency
    character_class = character_class.strip().capitalize()
    
    # Use simple formulas for each class type
    if character_class == "Warrior":
        return (20 + level*4, 1 + level*1, 120 + level*10, 15 + level*2, 5 + level*1)
    elif character_class == "Mage":
        return (5 + level*1, 20 + level*4, 60 + level*6, 6 + level*2, 12 + level*3)
    elif character_class == "Rogue":
        return (12 + level*3, 5 + level*2, 80 + level*5, 15 + level*3, 20 + level*4)
    elif character_class == "Cleric":
        return (10 + level*2, 10 + level*3, 90 + level*8, 10 + level*2, 10 + level*3)
    elif character_class == "Prisoner":
        return (15 + level*3, 2 + level*4, 100 + level*5, 8 + level*4, 15 + level*3)
    elif character_class == "Devil":
        return (25 + level*5, 15 + level*4, 150 + level*4, 18 + level*3, 8 + level*2)
    elif character_class == "Angel":
        return (35 + level*6, 18 + level*4, 180 + level*4, 20 + level*3, 12 + level*2)
    else:
        # Default for unrecognized classes
        return (5 + level, 5 + level, 80 + level*8, 5 + level, 5 + level)
    

def save_character(character, filename):
    """
    Saves a character's information to a text file in a specific format.
    Returns: True if successful, False if error occurred.
    
    File format example:
    Character Name: Aria
    Class: Mage
    Level: 1
    Strength: 5
    Magic: 15
    Health: 80
    Gold: 100
    """

    # Check that the directory exists before writing
    dir_path = os.path.dirname(filename)
    if dir_path and not os.path.exists(dir_path):
        return False  # Invalid directory, cannot save
    
    # Attempt to write character data to the file
    with open(filename, 'w') as file:
        file.write(f"Character Name: {character['name']}\n")
        file.write(f"Class: {character['class']}\n")
        file.write(f"Level: {character['level']}\n")
        file.write(f"Strength: {character['strength']}\n")
        file.write(f"Dexterity: {character['dexterity']}\n")
        file.write(f"Stealth: {character['stealth']}\n")
        file.write(f"Magic: {character['magic']}\n")
        file.write(f"Health: {character['health']}\n")
        file.write(f"Gold: {character['gold']}\n")
        file.write(f"Equipment: {', '.join(character['equipment'])}\n") # AI assitance to help with formatting of weapons in a file

    return True  # Successfully saved


def load_character(filename):
    """
    Loads a character from a text file.
    Returns: character dictionary if successful, None if file does not exist.
    """
    # Return None if the file is missing
    if not os.path.exists(filename):
        print(f"Error: File {filename} not found")
        return None

    # Read the file and rebuild the character dictionary
    with open(filename, 'r') as file:
        character = {}
        for line in file:
            # Split line at the first ': ' to separate key and value
            key, value = line.strip().split(": ", 1)
            
            # Convert text keys into proper dictionary fields
            if key == "Character Name":
                character["name"] = value
            elif key == "Class":
                character["class"] = value
            elif key == "Level":
                character["level"] = int(value)
            elif key == "Strength":
                character["strength"] = int(value)
            elif key == "Dexterity":
                character["dexterity"] = int(value)
            elif key == "Stealth":
                character["stealth"] = int(value)
            elif key == "Magic":
                character["magic"] = int(value)
            elif key == "Health":
                character["health"] = int(value)
            elif key == "Gold":
                character["gold"] = int(value)
            elif key == "Equipment":
                character["equipment"] = [item.strip() for item in value.split(",")]
                    
    return character


def display_character(character):
    """
    Prints a formatted character sheet to the console.
    Returns: None
    """
    print("=== CHARACTER SHEET ===")
    print(f"Name: {character['name']}")
    print(f"Class: {character['class']}")
    print(f"Level: {character['level']}")
    print(f"Strength: {character['strength']}")
    print(f"Dexterity: {character['dexterity']}")
    print(f"Stealth: {character['stealth']}")
    print(f"Magic: {character['magic']}")
    print(f"Health: {character['health']}")
    print(f"Gold: {character['gold']}")
    print(f"Equipment: {', '.join(character['equipment'])}")
    print("==========================")


def level_up(character):
    """
    Increases character level by 1 and recalculates stats.
    Modifies the existing character dictionary directly.
    """
    # Increase the level by one
    character["level"] += 1

    # Recalculate stats based on new level
    strength, magic, health, dexterity, stealth = calculate_stats(character["class"], character["level"])

    # Update stats in dictionary
    character["strength"] = strength
    character["magic"] = magic
    character["health"] = health
    character["dexterity"] = dexterity
    character["stealth"] = stealth

    # Provide user feedback
    print(f"{character['name']} leveled up to Level {character['level']}!")


# === MAIN PROGRAM AREA ===
# Used for testing your functions directly
if __name__ == "__main__":
    print("=== CHARACTER CREATOR ===")
    print("Test your functions here!")

    # Create a test character
    char = create_character("TestHero", "Warrior")
    print(char) 
    # Display dictionary directly
    
    # Uncomment below for extended testing
    # display_character(char)
    # save_character(char, "my_character.txt")
    # loaded = load_character("my_character.txt")
    # print(loaded)
    # level_up(char)
 
