from art import *


print(text2art("Welcome"))

options = ['yes', 'no', 'or']
directions = ['forward', 'left', 'right', 'backward']
items = ['sword', 'tinderbox', 'walking stick', 'gun']
combat_choice = ['yes', 'no']
end_path = ['forward', 'right']

player = input("What's your name traveler?\n")

print('\n')

choice = ""
while choice not in options:
    choice = input("Your eyes begin to open. There is a path in front of you. Do you wish to take the path?\nyes or no\n")
    print('\n')
    choice = choice.lower()
    if choice == 'yes':
        print("You take the path. In the distance you hear the soft, muddled bustle of a township. Behind you there is a droning silence with the occasional movement of brush.\n")
    elif choice == "no":
        print(f'Perhaps you aren\'t quite ready for the adventure. Farewell, {player}.')
        quit()
    elif (choice == "or") or (choice == "maybe"):
        print('Or we can think of another adventure? Let\'s see the options.\n')
    else:
        print('I don\'t understand that...')


direction_choice = ""
while direction_choice not in directions:
    print("You reach a three-way split in the path.") 
    print("The middle path that leads forward is consumed in the dark forest ahead.")
    print("The left path has a long curve that looks like it avoids the dark forest.")
    print("The right path is illuminated by the sunlight that peaks around the dark clouds that cover the dark forest.\n")
    direction_choice = input("Do you wish to press on forward, take the left path, or take the right path?\nforward or left or right\n")
    print('\n')
    direction_choice = direction_choice.lower()
    if direction_choice == 'forward':
        print(f'What a brave warrior you are {player}! As you take a few steps forward you hear the screeching of ravens deep within the forest. The fog only grows thicker with each step you take. For a moment, you feel like there are eyes watching your every move.\n')
    elif direction_choice == 'left':
        print(f'You resemble no more than a common coward {player}... I am disappointed. And so will you be... As you begin down the trail, you see bones in the ditch near the forest. The ditch on the left side of you is filled with a small pool of blood... Animal tracks cover the path before you...\n')
    elif  direction_choice == 'right':
        print(f'So you\'re an optimist {player}! Perhaps your optimism will help you in the journey to new adventures. As you continue on the trail, it seems that you re not the only traveler. You see a few carts on the path towards a city along with the average caravan of a few townspeople. You should delight in your optimism.\n')
    elif (direction_choice == 'backward') or (direction_choice == 'back') or (direction_choice == 'turn around'):
        print(f'Better quit while you can. Shameful you are {player}. Disgrace and dishonor be upon you.')
        quit()
    else:
        print('I don\'t understand that...')

item = ""
while item not in items:
    print(f'{player.upper()}! On your path, however dark or light it may or may not be for you. Using what sight you can muster... You see a chest that glows a purple aura. As you go to open the chest, it shatters and out falls three items!\n')
    print('There is an old sword that is covered in moss and dirt. Perhaps it will prove to be a worthy companion for you.')
    print('There is a tinderbox that can be used to start a fire. Although old, it appears to have never been used.')
    print('There is a walking stick. It doesn\'t look to be much, but it\'s an honest stick. One you could use to make your walk a bit easier.\n')
    item = input('Which of these three items do you wish to take with you on your journey forward?\nsword or tinderbox or walking stick?\n')
    print('\n')
    item = item.lower()
    if (item == 'sword') or (item == 'old sword'):
        item = 'sword'
        print('What a good choice! The true choice of a hopeful warrior! As you reach for the sword you think that you see it begin to shine. Once your hand touches the hilt, some of the dirt shakes off, but the moss is heavier than you thought it would be.\n')
    elif (item == 'tinderbox') or (item == 'tinder'):
        item = 'tinderbox'
        print('Ahhh! A resourceful adventurer! You think it will only get darker the further you travel? Maybe your wit hasn\'t escaped you just yet.\n')
    elif (item == 'walking stick') or (item == 'stick'):
        item = 'walking stick'
        print('Your back hurts too huh? I know mine does... Carrying this entire game on my back gets difficult sometimes. Isn\'t it weird that you have no idea how long it has been? I don\'t think there\'s any food or water in this game either. Woops!\n')
    elif item == 'gun':
        item = 'gun'
        print('How did that get there? Well it will be really weird when you kill a mythical creature with a modern weapon. They will have no idea what just punched a hole through their chest... WILD!\n')
    else:
        print('I don\'t understand that...')


combat = ""
while combat not in combat_choice:
    if direction_choice == 'forward':
        print(f'As you continue walking, holding your trust {item}, you can\'t tell if you are getting closer to the small light that looks like an exit in the distance or if you are only getting more tired. Just as you realize that you\'ve been day dreaming about making it out of the forest, you hear large snap of a branch!! BOOM! An Orc falls from the tree above! He blocks the path before you!\n')
        combat = input(f'Do you wish to fight the Orc with your {item}?\nyes or no?\n')
        print('\n')
        combat = combat.lower()
        if (combat == 'yes') and (item == 'sword'):
            print(f'You can feel your hand shaking, your eyes are dry, your stomach groans because I forgot to code in an option for food or water, now you are even more confused about what\'s going on, but you reach for your {item}. As a true warrior you barge toward the Orc! You swing the sword and just as you strike the Orc, the sword bursts with a flash of energy, it begins to glow with the purple haze of the chest it fell out of! The Orc catches fire and turns to dust instantly!! Your trust {item} will continue with you for many days!\n')
        elif (combat == 'yes') and (item == 'tinderbox'):
            print(f'The ringing in your ears from intense dehydration only get\'s louder with each step. Your eyes begin to burn into your skull. But, you have your {item}. Just as you open your eyes from the longest blink you have ever took, you see the large Orc standing only a few feet in front of you. You pull it out from the backpack that you forgot you were carrying and you run towards the Orc with no idea of how you are going to get out of this fight alive. You are brave. You are fire. Just as you get within feet of the Orc you strike the tinderbox and light it! As you do so, the fire from the box illuminates your body, you raise your hands and drop the {item}! As your hands raise, there emits a beam of fire that strikes the Orc and cooks him to a crisp! Finally, now you have food, even though you have no water!\n')
        elif (combat == 'yes') and (item == 'walking stick'):
            print(f'Look at you. Just you and your {item}. Doing the things that {player}s and {item}s do. Walking through a pitch black forest. Taking our dandy time. The Orc is ANGRY! He begins to charge you, so you raise your {item}. It transforms into a bow and you pull the string back to see 3 arrows ready to fly at your enemy! You release, and the arrows striek the Orc. They explode as they touch his green, slimy skin! WOAH!!! You have mighty power! There is nothing left of the Orc and now there is a 7 ft deep crater in the path. The township department of highways and transporation is not going to be happy with what you\'ve done with the place.\n')
        elif (combat == 'yes') and (item == 'gun'):
            print(f'You are walking, in the forest, with a {item} in your hand. Living the dream. Doing {player} things. The average life. It\'s exciting and your happy to be alive. The Orc is not a happy camper! You raise your gun laughing and just as you do you wake up in Chem-101 screaming and everyone looks at you confused. What a weird dream...')
            quit()
        elif combat == 'no':
            print('You leave and run back down where you came from in terror. Pitiful.')
            quit()
        else:
            print('I don\'t understand that...')

    elif direction_choice == 'left':
        print(f'You continue walking. The small creek of blood to your left is now a river that has spilled onto the path that has coated everything before you. The piles of bones to your right have yet to get smaller in size and quantity. It\'s dark now. As you raise your eyes forward a large behemoth of a bear stands in the path. Uh oh...\n')
        combat = input(f'Do you wish to fight the bear with your {item}?\nyes or no?\n')
        print('\n')
        combat = combat.lower()
        if (combat == 'yes') and (item == 'sword'):
            print(f'Without hesitation you charge at the bear with your {item}! You raise it and moss falls to your feet. You let out a loud cry, like the true warrior you are {player}! Just as the blade of the sword hits the bear, there is a bright flash of energy and the sword begins to glow with the same purple haze that surrounded the chest you found it in! The bear catches flames and the turns to ash instantly! What a great companion your {item} will make...\n')
        elif (combat == 'yes') and (item == 'tinderbox'):
            print(f'As you stare at the bear you wonder how good he would taste cooked. You charge him! THE TURN TABLES! As you begin to get close you strike the {item} and just as the flame appears it moves through your hands and into your very being. You begin to feel warm! Scared, you drop the {item} and you begin to raise your hands. Just as you do so beams of fire shoot out and hit the bear! Within seconds he turns into what looks like a perfectly cooked steak! WOW! You feel amazing and you avoid the trikinosis poisoning of raw bear meat! Win-win!\n')
        elif (combat == 'yes') and (item == 'walking stick'):
            print(f'{player} you are tired. You\'ve been walking for too long. There\'s no water and it only gets colder and colder. What a wild ride it has been. The bear begins to charge you! You raise your {item} and as you do it turns into a large bow! You see 3 arrows properly quivered and ready to fly towards the enemy! You pull back and release! They hit the bear and explode!!! There is nothing but a giant crater where the four legged beast was. What a great choice the {item} was!\n')
        elif (combat == 'yes') and (item == 'gun'):
            print(f'{player}, you really thought you could bring a gun to a knife fight? Think again. The bear flys towards you! Just as it gets close, it turns into a teddy bear! Huh? As you shoot the {item} your eyes open and you wake up in Stats 150. Everyone is laughing at you. Weird...')
            quit()
        elif combat == 'no':
            print('You run away frightened. Bear was super effective.')
            quit()
        else:
            print('I don\'t understand that...')

    elif direction_choice == 'right':
        print(f'It\'s just you and your {item} walking down the busy road. What a life it is. Simple even. BOOM! A goblin appears in the path before you and he is not happy! You hear combat music begin. You know what must be done.\n')
        combat = input(f'Do you want to fight the goblin with your {item}?\nyes or no?\n')
        print('\n')
        combat = combat.lower()
        if (combat == 'yes') and (item == 'sword'):
            print(f'Without hesitation you charge the goblin! You scream and raise your {item}! Just as the blade hits the goblin it bursts with a flash of light and a purple haze appears! Astonishing! The goblin bursts into flames and turns to ash immediately! The {item} proved to be a trust sidekick to you!\n')
        elif (combat == 'yes') and (item == 'tinderbox'):
            print(f'You remember your late uncle use to love eating goblin. You run at it! With bravery you strike the {item} and just as the flame appears it rushes towards you and hit you in the stomach. You feel warm and powerful. As you let go of the tinder box and raise your hands, a beam of fire shoots the goblin and cooks it immediately. The smell is repulsive and you choose to remain hungry... But hey, you can shoot fire from your hands now.\n')
        elif (combat == 'yes') and (item == 'walking stick'):
            print(f'Well {player}, it\'s just you and your {item}. Without thought the goblin runs towards you! You lift your {item} and it turns into a bow! An arrow is already properly quivered. You raise the bow and release the arrow. It punches a giant hole through the goblin! WOW! What a great choice the {item} was!\n')
        elif (combat == 'yes') and (item == 'gun'):
            print(f'Ya, nice try {player}. You wake up. It was a dream. Go back to your life. You can\'t bring that {item} to a goblin fight...')
            quit()
        elif combat == 'no':
            print('Well, then I guess that\'s the end of the game. Bye!')
            quit()
        else:
            print('I don\'t understand that...')

print('Well done traveler, you have made it past the enemy before you. You reach the end of the path and now there is only a township before you. Surely there must be people there! What a great joy comes over you! You are still curious about if water or food will be introduced in the game, but that hope leaves you instantly.\n')

the_end = ""
while the_end not in end_path:
    print(f'So so so {player}. Looks like you have a choice to make again. There is a township before you. You hear laughter from the pub, the bustle of trade and travel, and the happy talk of the towns folk. To your right there is a trail that has a long line of other travelers spread across what distance you can see. It looks like there is a mountain off in the distance and certainly more adventure.')
    the_end = input('Do you want to go forward into the township or to the right on the next trail?\nforward or right\n')
    print('\n')
    the_end = the_end.lower()
    if the_end == 'forward':
        print(f'{player}, you go into the township. You party and laugh and wind up falling asleep in the pub. But the dream you have never stops and you never wake up again. Good job! That brings you to the end of this adventure! Well done warrior! Your name shall be known throughout the land! {player} the Party Goer!')
        quit()
    elif the_end == 'right':
        print(f'{player} you take your {item} and continue on the new trail! You are excited for the adventure that lies ahead! Although you are curious about what the mountain has in store for you. Perhaps it is the adventure. As you continue down the path with the other travelers you over hear two talking about a certain \'King of the East Mountain\' and you become more and more curious about who he is and what he can do for you. The travelers talk about how the king has many armies and riches that he has culled together from ruling the East Mountain with an iron fist and great strength. But this only causes your flame to burn brighter. You raise your {item} towards the sky! You certainly are a brave warrior {player}! The journey continues....')
        quit()
    else:
        print('I don\'t understand that...')
