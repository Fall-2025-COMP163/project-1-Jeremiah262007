# COMP 163 – Project 1: Character Creator & Saving/Loading  
**Author:** Jeremiah Cooper  
**Date:** October 31, 2025  

---

## Game Concept  
This project simulates a **fantasy RPG character creator** where players can build, level up, save, and load their own custom characters.  
Each character belongs to one of four classes — **Warrior**, **Mage**, **Rogue**, or **Cleric** — each with unique stat growth formulas and gameplay identities.  

Players begin at **Level 1** with **100 gold**, and as they level up, their stats automatically increase based on their class formula.  
Characters can be **saved to** and **loaded from** text files, allowing progress to persist between sessions.

---

## Design Choices  
I designed my stat formulas to reflect each class’s strengths and weaknesses while keeping the math simple and balanced.

| Class | Role & Design Intent | Strength Formula | Magic Formula | Health Formula |
|--------|----------------------|------------------|----------------|----------------|
| **Warrior** | Strong melee fighter with high Strength and Health but low Magic | `20 + level * 4` | `1 + level * 1` | `120 + level * 10` |
| **Mage** | Magic specialist with high Magic but low Strength and Health | `5 + level * 1` | `20 + level * 4` | `60 + level * 6` |
| **Rogue** | Balanced and agile with steady overall growth | `12 + level * 3` | `5 + level * 2` | `80 + level * 5` |
| **Cleric** | Support role with good Magic and Health | `10 + level * 2` | `10 + level * 3` | `90 + level * 8` |

A **default formula** is also included for unrecognized class names to prevent runtime errors.  
This design ensures each class feels unique and scales fairly across levels.

---

## Bonus Creative Features  
**Note:** All bonus feature code is included under the commit titled  
**"Add bonus creative features code"**  
*(commit details to be added later).*

---

## AI Usage  
I consulted **ChatGPT** for assistance in the following areas of development:  

- **Stat Formulas:** Brainstormed and refined scaling formulas for different classes.  
- **File I/O Structure:** Suggested clean and safe read/write patterns for saving and loading characters without using `try/except`.  
- **Debugging Help:** Identified indentation and logic-order issues in the `calculate_stats()` function.  
- **Code Refinement:** Recommended adding directory validation in `save_character()` and improving parsing logic in `load_character()`.  
- **Documentation Support:** Helped write professional docstrings, inline comments, and this README file.  

All code logic, stat formula design, function implementation, and testing were done **independently by me (Jeremiah Cooper)**.  
The AI was used only as a learning and polishing tool — this project is **my original work** and meets all COMP 163 requirements.

---

## How to Run  

### Run in Terminal  
Make sure you are in your project directory, then run:  
```bash
python3 project1_character_creator.py

Inside the if __name__ == "__main__": block, you can uncomment the test lines to verify your functions:
display_character(char)
save_character(char, "my_character.txt")
loaded = load_character("my_character.txt")
print(loaded)
level_up(char)

Example Output
=== CHARACTER CREATOR ===
{'name': 'TestHero', 'class': 'Warrior', 'level': 1, 'strength': 24, 'magic': 2, 'health': 130, 'gold': 100}

=== CHARACTER SHEET ===
Name: TestHero
Class: Warrior
Level: 1
Strength: 24
Magic: 2
Health: 130
Gold: 100
==========================
TestHero leveled up to Level 2!

