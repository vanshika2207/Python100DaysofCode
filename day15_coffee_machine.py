#COFFEE MACHINE

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
print('☕')
def total_money():
    print("Please insert coins")
    quarters = int(input("How many quarters? :"))
    dimes = int(input("How many dimes? :"))
    nickles = int(input("How many nickles? :"))
    pennies = int(input("How many pennies? :"))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total




# TODO :1.Prompt from user


money=0
coffee_machine='on'
while coffee_machine=='on':
    input_user = input("What would you like? (espresso/latte/cappuccino):")
    if input_user=='off':
        coffee_machine='off'

    elif input_user=='report':
        print(f'''
        Water : {resources["water"]}
        Milk  : {resources["milk"]}
        Coffee: {resources["coffee"]}
        Money : {money}
        ''')

    elif input_user=='espresso':
        if resources["water"]<=MENU["espresso"]["ingredients"]["water"] :
            print("Sorry not enough water")
        elif resources["coffee"]<=MENU["espresso"]["ingredients"]["coffee"]:
            print("sorry not enough coffee")
        else:
          a=total_money()
          if a<1.5:
              print("Sorry that's not enough money. Money refunded.")
          else:
              if a>1.5:
                  money+=1.5
                  remaining_money=a-1.5
                  print(f"Here is ${round(remaining_money, 2)} in change")
              else:
                  money+=1.5
              resources['water']=resources['water']-50
              resources['coffee']=resources['coffee']-18
              print("Here is your espresso.Enjoy ! ")
    elif input_user=='latte':
        if resources["water"]<=200 :
            print("Sorry not enough water")
        elif  resources["coffee"]<=24:
            print("sorry not enough coffee")
        elif resources["milk"] <=150:
            print("sorry not enough milk")
        else:
            a=total_money()
            if a < 2.5:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if a > 2.5:
                    money += 2.5
                    remaining_money = a - 2.5
                    print(f"Here is ${round(remaining_money, 2)} in change")
                else:
                    money += 2.5
                resources['water'] = resources['water'] -200
                resources['coffee'] = resources['coffee'] - 24
                resources['milk']=resources['milk']-150
                print("Here is your latte.Enjoy ! ")
    elif input_user=='cappuccino':
        if resources["water"]<=250 :
            print("Sorry not enough water")
        elif  resources["coffee"]<=24:
            print("sorry not enough coffee")
        elif resources["milk"] <=100:
            print("sorry not enough milk")
        else:
            a=total_money()
            if a < 3.0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if a > 3.0:
                    money += 3.0
                    remaining_money = a - 3.0
                    print(f"Here is ${round(remaining_money,2)} in change")
                else:
                    money += 3.0
                resources['water'] = resources['water'] - 250
                resources['coffee'] = resources['coffee'] - 24
                resources['milk'] = resources['milk'] - 100
                print("Here is your cappuccino.Enjoy ! ")
