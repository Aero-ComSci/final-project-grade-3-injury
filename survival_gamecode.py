import random

inventory = []
stamina = 10
health = 10
days_survived = 0
hunger = 10
thirst = 10
shelter_built = False

resources = ["coconut", "fish", "wood", "fresh water", "berries", "fresh water", "banana", "rubber", "wood", "rubber"]

events = [
    "A wild boar appears glaring at you.",
    "A tropical storm is rolling in. You need to find shelter quickly!",
    "You see a distant boat. Do you signal or wait for a better chance?",
    "A mysterious figure lurks near the beach. You think it's a boar but your instinct tells you otherwise.",
    "You accidentally stumbled near a spider's nest and the queen looks angry.",
    "You are shrouded in your own thoughts, fighting your internal voice to quit.",
    "Your reflection in the lake does not match your movements. It stares back, unblinking.",
    "A wild boar appears, eyeing you cautiously. Warning: It may charge if provoked.",
    "A snake slithers near your foot. It hesitates deciding whether you are a threat."
]

def find_resource():
    global stamina
    global hunger
    global thirst
    global health
    choices = [
        "You rummage through dense jungle and find something useful.",
        "You dig in the sand near the shore, hoping for hidden treasures.",
        "You climb a tree, scanning for food or tools in the branches."
    ]
    print(random.choice(choices))
    
    found = random.choice(resources)
    inventory.append(found)
    print(f"Success! You found {found}.")
    print("You lost 1 stamina, 1 hunger, and 1 thirst though.")
    
    stamina -= 1
    hunger -= 1
    thirst -= 1

def build_shelter():
    global stamina
    global shelter_built 
    if "wood" in inventory:
        print("Using scattered driftwood, you craft a rough shelter against the elements. You lose 2 stamina points though.")
        inventory.remove("wood")
        shelter_built = True
    elif shelter_built:
        print("You have already built a shelter.")
    else:
        print("You have no materials to build with. You lose 2 stamina.")
    stamina -= 2

def check_status():
    global days_survived
    global stamina
    global hunger
    global thirst
    global inventory

    print(f"\nDay {days_survived} on the Island")
    print(f"Stamina: {stamina}")
    print(f"Hunger: {hunger}")
    print(f"Thirst: {thirst}")
    print(f"Health: {health}")
    print(f"Inventory: {inventory}")


def drink_water():
    global thirst
    global stamina
    global health
    if "fresh water" in inventory:
        print("You drink slowly, savoring every drop. You gained 3 thirst points. You gained 2 stamina. You gained 2 health.")
        thirst += 3
        stamina += 2
        health += 2
        inventory.remove("fresh water")
    else:
        print("Your throat is dry. No water in sight.")

def eat_food():
    global hunger
    global stamina
    global health
    for food in ["coconut", "fish", "berries", "banana"]:
        if food in inventory:
            print(f"You eat {food}, feeling stronger. You gained 3 hunger points, 3 stamina points, and 3 health points.")
            hunger += 3
            stamina += 3
            health += 3
            inventory.remove(food)
            return
    print("Your stomach growls... no food left.")

def face_danger():
    global days_survived
    global stamina
    global health

    event = random.choice(events)  
    print("\nDangerous Situation!!!")
    print(event)

    if event in ["A wild boar appears, eyeing you cautiously. Warning: It may charge if provoked.", 
                 "A snake slithers near your foot. It hesitates deciding whether you are a threat."]:
        response = input("What do you do? (stay still/back away/climb a tree/fight/run) ")
        
        if event == "A wild boar appears, eyeing you cautiously. Warning: It may charge if provoked.":
            if response == "stay still":
                deciding_factor = random.randint(1,2)
                if deciding_factor == 1:
                    print("You hold your ground. The boar snorts and eventually loses interest. No harm done.")
                else:
                    print("The boar charges towards you anyway and rips your head off. What a cruel world!")
                    print(f"You have survived {days_survived} days.")
                    quit()
            elif response == "back away":
                print("You slowly retreat, keeping your eyes on the boar. It watches you before returning to the jungle. You lose 1 stamina.")
                stamina -= 1
            elif response == "climb a tree":
                print("You scramble up a tree, but forget that boars can climb. The boar knocks you down and mauls you to death.")
                print(f"You have survived {days_survived} days.")
                quit()
            elif response == "fight":
                print("You attempt to fend off the boar, but its strength overwhelms you. What a cruel world!")
                print(f"You have survived {days_survived} days.")
            elif response == "run":
                print("You sprint away in panic, exhausting yourself. You lose 3 stamina.")
                stamina -= 3
            else:
                print("You hesitate, making unpredictable movements! The boar headbutts you. You lose 6 health and 4 stamina.")
                health -= 6
                stamina -= 4
        
        elif event == "A snake slithers near your foot. It hesitates deciding whether you are a threat.":
            if response == "stay still":
                print("You stay perfectly still. The snake flicks its tongue and moves on. No harm done.")
            elif response == "back away":
                print("You carefully step back without disturbing the snake while sweating profusely. It watches but does not strike. You lose 1 stamina.")
                stamina -= 1
            elif response == "climb a tree":
                print("You climb a tree, escaping the snake. However, you scrape your arm in the process. You lose 1 health.")
                health -= 1
            elif response == "fight":
                print("You attempt to strike the snake, but it bites your hand! Venom courses through your veins and you realize it was too late.")
                print(f"You have survived {days_survived} days")
            elif response == "run":
                print("You jump back and sprint away, losing 2 stamina in the process.")
                stamina -= 2
            else:
                print("You hesitate, making an unpredictable move! The snake bites. Fortunately, you can still heal. You lose 6 health.")
                health -= 6
        
    elif event == "A tropical storm is rolling in. You need to find shelter quickly!":
        if shelter_built:
            print("You take refuge in your shelter and wait out the storm safely.")
        else:
            print("You have no shelter! The storm batters you, reducing your health and stamina. You lose 5 health and 3 stamina.")
            health -= 5
            stamina -= 3

    else:
        response = input("What do you do? (run/fight/search/wait) ")
        if response == "run":
            print("You barely escape trouble, but you're exhausted. You lose 2 stamina.")
            stamina -= 2
        elif response == "fight":
            print("You have fought long and hard, but was it the right choice? You lose 3 stamina and 2 health.")
            stamina -= 3
            health -= 2
        elif response == "search":
            print("You look for something useful. You find a small resource but lose 2 stamina in the process.")
            stamina -= 2
            found = random.choice(resources)
            inventory.append(found)
            print(f"You found {found}.")
        elif response == "wait":
            print("You remain motionless and observe. The danger passes without incident.")
        else:
            print("You hesitate, making a risky decision. You lose 4 stamina and 10 health.")
            stamina -= 4
            health -= 10


def build_a_raft():
    if "wood" in inventory and "fresh water" in inventory and ("fish" in inventory or "banana" in inventory or "berries" in inventory or "coconut" in inventory) and "rubber" in inventory and health >= 7 and stamina >= 7 and thirst >= 7 and hunger >= 7:
        print("You use your rubber to tie the wood together in order to construct a raft and row yourself to the nearest island to get help. You snack on some food and drink some water as you embark on your two-day journey. You are rescued!")
        exit()
    elif health < 7:
        print("You are not healthy enough to leave the island!")
    elif stamina < 7:
        print("You do not have enough stamina to leave")
    elif thirst < 7:
        print("You are too thirsty to leave")
    elif hunger < 7:
        print("You are too hungry to leave")
    else:
        print("You don't have enough resources to leave! Think about what you need.")

def build_signal_fire():
    global stamina
    global inventory
    wood_needed = 5

    if inventory.count("wood") >= wood_needed:
        print(f"You gather {wood_needed} pieces of wood and carefully arrange them to build a large signal fire.")
        print("The flames rise high, increasing your chances of being spotted. You lose 2 stamina.")
        for i in range(wood_needed):
            inventory.remove("wood")
        stamina -= 2

        if random.random() < 0.5:
            print("A distant boat sees the smoke and approaches the island. You are finally rescued!")
            exit() 
        else:
            print("Hours pass, but no sign of help. You remain stranded.")
    else:
        missing_wood = wood_needed - inventory.count("wood")
        print(f"You need {wood_needed} pieces of wood, but you only have {inventory.count('wood')}.")
        print(f"Don't give up! Keep searching! You still need {missing_wood} more wood.")


print("You wake up on the shore, stranded. You have lost all memory that happened before the plane crashed onto the island. The sun is high, use this opportunity to survive. Eat food to gain stamina and hunger points. Drink water to gain stamina and thirst points. Forage the island for supplies to potentially help you escape the island. Good luck, face every situation with a logical approach, and don't die.")

while stamina > 0 and hunger > 0 and thirst > 0 and health > 0:
    days_survived += 1
    print(f"\nDay {days_survived} Begins")
    print(f"Stamina: {stamina}")
    print(f"Thirst: {thirst}")
    print(f"Hunger: {hunger}")
    print(f"Health: {health}")

    if random.random() < 0.5: 
        face_danger()
    else:
        print("What a peaceful day!")

    print("\nChoose an action:")
    print("1. Search for supplies")
    print("2. Build a shelter")
    print("3. Drink water")
    print("4. Eat food")
    print("5. Check status")
    print("6. Try to escape")
    print("7. Give up")

    choice = input("Enter a number: ")

    if choice == "1":
        find_resource()
    elif choice == "2":
        build_shelter()
    elif choice == "3":
        drink_water()
    elif choice == "4":
        eat_food()
    elif choice == "5":
        check_status()
    elif choice == "6":
        escape_options = input("How would you like to escape? Type 1 for a raft or 2 for a signal fire.")
        if escape_options == "1":
            build_a_raft()
        elif escape_options == "2":
            build_signal_fire()
    elif choice == "7":
        print(f"This was all too much for you. The island claims its first victim. You survived {days_survived} days.")
        break
    else:
        print("You have entered the wrong input!")
        choice = input("Enter a number: ")
