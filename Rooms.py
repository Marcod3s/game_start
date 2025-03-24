import random
import character as ch
import math

random_num = random.randint(1, 10)
cbfive_num = math.ceil((random_num ** 3) * 5)


def room1(character):
    r1_sol = False
    print(f"welcome to the first room {character.name}")
    print(f"There's  screen displaying a number\n the number is {cbfive_num}")
    print("5 extremities of the human body,\n cubes make up the world")
    while not r1_sol and character.health > 0:
        r1_answr = int(input("What is the number you enter"))
        if r1_answr == math.ceil((cbfive_num / 5) ** (1 / 3)):
            print("Wow! You have passed the first room")
            r1_sol = True
        else:
            print("incorrect, try again")
            character.health -= 2
            print(f"You Have :{character.health} health")


pass


def room2(character):
    r2_items = ["1. 5 glass panes",
                "2. 9 branches",
                "3. 7 idols",
                "4. 3 knives"]
    print(f"welcome to second room {character.name}")
    print("You see 5 glass panes, 9 branches, 7 idols and 3 knives.\n there's a keypad right next to you")
    r2 = False
    while not r2 and character.health > 0:

        r2ans = int(input("what numbers do you put into the keypad?"))

        if r2ans == 5973:
            print("you got it right")
            r2 = True
            item_pickup = int(input("Pickup an Item? 1 for yes, 2 for no:"))

            if item_pickup == 1:
                item_chose = False

                while item_chose is False:

                    if len(r2_items) > 0:
                        item_choice = int(input(r2_items))
                        if item_choice == 1:
                            character.inventory.append("1. 5 glass panes")
                            print(f"Your bag has:{character.inventory}")
                            r2_items.remove("1. 5 glass panes")
                            # item_chose = True
                        elif item_choice == 2:
                            character.inventory.append("2. 9 branches")
                            print(f"Your bag has:{character.inventory}")
                            r2_items.remove("2. 9 branches")
                            # item_chose = True
                        elif item_choice == 3:
                            character.inventory.append("3. 7 idols")
                            print(f"Your bag has:{character.inventory}")
                            r2_items.remove("3. 7 idols")
                        # item_chose = True
                        elif item_choice == 4:
                            character.inventory.append("4. 3 knives")
                            print(f"Your bag has:{character.inventory}")
                            r2_items.remove("4. 3 knives")
                            # item_chose = True
                        elif item_choice == 5:
                            print("You are done!")
                            item_chose = True
                        else:
                            print("You didn't choose an item")
                        item_choice2 = int(input("Pickup another Item? 1 for yes, 2 for no:"))
                        if item_choice2 == 1:
                            item_chose = False
                        elif item_choice2 == 2:
                            item_choice = True
                    else:
                        print("You are done!")
                        break
        else:
            print("Incorrect, you've been punched in the face, try again and lost 2 health")
            character.health -= 2
            print(f"your health is now {character.health}")
            # if character.health == 0 :
            # print ("YOU DIED\n There's no way you couldn't get that easy answer -_-")
            # exit()


def room3(character):
    beast = ch.character("beast", health=40)
    print(f"You've moved on to the final room {character.name}")
    print(f"welcome to third room {character.name}")
    print("There's a beast in the room, you need to fight it")
    while beast.health > 0 and character.health > 0:
        print(character.health)
        print("What do you do?")
        fight_choice = int(input("1. run away\n2. fight it\n 3. use an item\n 4. do nothing?"))
        if fight_choice == 1:
            print("You ran away but there's only one direction to go, you must go back and fight the beast")
        elif fight_choice == 2:
            print("You punched the beast for 5 damage, but you lost 2 health")
            character.health -= 2
            beast.health -= 5
        elif fight_choice == 3:
            print(f"available items are: {character.inventory}")
            item_use = int(input("Which Item do you use?"))
            if item_use == 1:
                print("Used 5 glass panes")
                character.inventory.remove("1. 5 glass panes")
                beast.health -= 5
                print(character.inventory)
            elif item_use == 2:
                print("Used 9 branches")
                character.invetory.remove("2. 9 branches")
                beast.health -= 9
                print(character.inventory)
            elif item_use == 3:
                print("Used 7 idols")
                character.inventory.remove("3. 7 idols")
                beast.health -= 7
            elif item_use == 4:
                print("Used 3 knives")
                character.inventory.remove("4. 3 knives")
                beast.health -= 3
                print(character.inventory)
            else:
                print("not available")

        elif fight_choice == 4:
            character.health -= 7
            print("You did nothing, the beast attacked you for 7 damage (that was lowkey really dumb)")
            print(f"your health is now {character.health}")
    print("OH MY GOODNESS!!!!!!!!!\n YOU'VE SLAIN THE BEAST AND WON\n AMAZING JOB")
    print("YOU HAVE ACQUIRED THE SWORD OF THE BEAST")
    character.inventory.append("Sword of the beast")