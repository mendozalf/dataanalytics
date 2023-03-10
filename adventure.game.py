#Game
from re import U
import time
user_name = input("What is your name? ")
print(f"You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT.")
time.sleep(3)
#If statements
user_thing = input(f"{user_name}, which one do you want to pick up? ")

#match

if user_thing.lower() == "match":
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated.\nYou see a large grizzly bear, and then the match burns out.")
    user_thing_2 = input("Do you want to RUN, or HIDE behind a tree? ")
    if user_thing_2.lower() == "run":
        print("As you run, the beard reached to you. You find a weapon and a fish.")
        user_thing_3 = input("Which one do you want to use? ")
        if user_thing_3.lower() == "weapon":
            print(f"Game Over {user_name}. The beard felt angry because you tried to hurt him, and\nthen he killed you.")
        elif user_thing_3.lower() == "fish":
            print(f"You have won {user_name}! The bear felt hangry because you showed him the fish,\nthen the beard ate the fish and it gave you time to escape.")
        else:
            print(f"{user_name}, you have chose a wrong option")
    elif user_thing_2.lower() == "hide":
        print("You have a HOUSE TREE and a CAVE.")
        user_thing_4 = input("In which one do you want to hide? ")
        if user_thing_4.lower == "house tree":
            print("You win! The beard got tired while wating for you, and then he got sleep.\nIt gave you time to escape.")
        elif user_thing_4.lower() == "cave":
            print("Game Over. Another beard was in that cave, and then he killed you.")
    else:
        print("Ups! You are wrong")

#flashlight

elif user_thing.lower() == "flashlight":
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you,\nbut you thought you also heard something off to the side.")
    user_thing_5 = input("Do you want to FOLLOW the path or LOOK in the trees for the thing that made the noise?")
    if user_thing_5.lower() == "follow":
        print(f"Great job {user_name}! As you follow the path you realized the noise come from a car. Using the car you escape from the fores.")
    elif user_thing_5.lower() == "look":
        print(f"{user_name} you loose. Because you wasted time looking in the trees, the beard got you and ate you")
    else:
     print("Ups! You are wrong")

elif user_thing.lower() != "flashlight" and user_thing.lower() != "match":
    print(f"Try again, you typed {user_thing}")
else:
    print("Try again")                 
            
    
