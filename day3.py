##conditional statement
#if-else-elif-nested IF- multiple if
print("welcome to the rollercoaster !")
height=int(input("what is your height in cm ?"))
bill=0
if height>=120:
    print("You can ride the rollercoaster !")
    age=int(input("what is your age"))
    if age<=12:
        bill=5
        print("child pays $5.")
        
    elif age<=18:
        
        bill=7
        print("youth pays $7.")
    elif age>=45 and age<=55:
        print("Everything is going to be ok. Enjoy the free ride")  
    else:
        bill=12
        print("adult pays $12.")
      
    ans=input("do you want a photo taken? Y or N")
    if ans=='Y':
        bill+=5
        print(f"Your bill is {bill} ")
    else:
        print(f"Your bill is {bill} ")
else:
    print("Sorry , you have to grow taller before you can ride.")
      

      
##leap yaer

if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasur Island")
print("Your mission is to find the treasure")
crossroad=input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"')
if crossroad=="left":
    island=input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')
    if island=="wait":
        door=input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if door=='red':
            print("It's a room full of fire. Game Over.")
        elif door=='blue':
            print("You enter a room of beasts. Game Over.")
        elif door=='yellow':
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You get attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")


