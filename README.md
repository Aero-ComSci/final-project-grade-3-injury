# final-project-grade-3-injury
final-project-grade-3-injury created by GitHub Classroom


# Stuff we did:
 - Figure out Final Project Idea?
 - Add Additional Features
 - Debug Testing
 - Added Custom Functions
 - Had to add some tweaks to the code to make the game have more features.
 - Made custom dialogues for certain deaths and occasions.
# Project Description
- This program is essentially made for anyone who has a passion in games not just video games but all sorts of games, specifically survival games. However, we say essentially as this game is not catered to any ONE audience and instead peaks and reveals itself to a plethora of people who have any interest in what this game provides as it forces people to learn through challenges that involve critical thinking and push the human brain to the edge due to the infinite amount of possibilities for how the survival on the island could turn out.

- What this program does it automate and create an environement where the user is forced to make decisions based on their own choices, and due to this will either end up avoiding death on the island. But, on the other hand the user could also make terrible decisions leading to their ultimate demise. So, what this code is essentially automating is an infinite loop where there is a day counter counting down every single day the user is trying to surivive on the island. Also, it adds the possibility of there being a 50% chance of something terrible happening daily and there is always the possibility that the person could die anyday. To end off, what this program does is use functions specifically in our code we used the function (def eat_food) and what this does it allow the user a selection and the ability to eat food which increases things like stamina, and health so that the user can survive longer on the island avoiding death.

  
# Using a Loop
```
while stamina > 0 and hunger > 0 and thirst > 0 and health > 0:
    days_survived += 1
    print(f"\nDay {days_survived} Begins")
    print(f"Stamina: {stamina}")
    print(f"Thirst: {thirst}")
    print(f"Hunger: {hunger}")
    print(f"Health: {health}")
```
# Using a Collection like a List
```
inventory = []
stamina = 10
health = 10
days_survived = 0
hunger = 10
thirst = 10
shelter_built = False

resources = ["coconut", "fish", "wood", "fresh water", "berries", "fresh water", "banana", "rubber", "wood", "rubber"]
```
# Using a Function
```
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
```

# Screenshots of Code
![Screenshot 2025-05-29 100044](https://github.com/user-attachments/assets/b1680bd2-7477-490b-91f7-48ff56e44d9b)
![Screenshot 2025-05-29 100059](https://github.com/user-attachments/assets/6747038d-5f34-4253-bf11-10f99b1a439b)
![Screenshot 2025-05-29 100115](https://github.com/user-attachments/assets/8f8f1021-ee3e-4276-ab0b-5205094e83ac)

# Video
https://github.com/user-attachments/assets/68e2b198-05ba-41f5-abac-82577f8ae885





