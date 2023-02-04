from art import *


print(text2art("Welcome"))

options = ['yes', 'no', 'or']
directions = ['forward', 'left', 'right', 'backward']

player = input("What's your name traveler?\n")

choice = ""
while choice not in options:
    choice = input("Your eyes begin to open. There is a path in front of you. Do you wish to take the path?\nyes or no\n")
    choice = choice.lower()
    if choice == 'yes':
        print("You take the path. In the distance you hear the soft, muddled bustle of a township. Behind you there is a droning silence with the occasional movement of brush.\n")
    elif choice == "no":
        print(f'Perhaps you aren\'t quite ready for the adventure. Farewell, {player}.')
        quit()
    elif choice == "or":
        print('Or we can think of another adventure? Let\'s see the options.\n')
    else:
        print('I don\'t understand that...')


# direction_choice = ""
# while direction_choice not in directions:
#     print("You reach a three-way split in the path.") 
#     print("The middle path that leads forward is consumed in the dark forest ahead.")
#     print("The left path has a long curve that looks like it avoids the dark forest.")
#     print("The right path is illuminated by the sunlight that peaks around the dark clouds tha cover the dark forest.\n")
#     direction_choice = print("Do you wish to press on forward, take the left path, or take the right path?\nforward or left or right\n")
#     direction_choice = direction_choice.lower()
#     if direction_choice == 'forward':
#         print(f'What a brave warrior you are {player}! As you take a few steps forward you hear the screeching of ravens deep within the forest. The fog only grows thicker with each step you take. For a moment, you feel like there are eyes watching your every move.\n')


"""
The next question will include an option to pick up one of three items presented to the player:
1. An old sword that is mostly covered in moss
2. A tinderbox that can be used to start a fire
3. A walking stick

The player will then have an option to engage in combat with a creature depending on which path they chose to take
1. If they chose to go into the forest, the creature will be an Orc
2. If they chose to go left, the creature will be a Bear
3. If they chose to go right, the creature will be a Goblin

If the player chose to pick up the tinderbox, they will find that once they strike it, they are imbued with magical
energy that allows them to command fire with only their hands

If the player chose to pick up the sword, they will find that once they swing the sword, the first strike unleashes
the true power of the sword, causing it to glow with an enchanted aura

If the player chose to pick up the walking stick, they will find that the sword can shapeshift into a bow, with
a magically unlimited number of arrows

After fighting the creature in combat, the player will then be prompted that they have made it to a township

The player will then have an option to either stop in the township or continue on the path that leads westward

If the player chooses to stop in the town, they will be prompted with either sleeping or partying. Either option will result
in them receiving much needed rest and finding that they never wakeup.

If the player chooses to continue on the trail westward, the prompt will display an achievement and an end credit message will
play. The final sentence will be a cliff hanger into the next adventure
"""