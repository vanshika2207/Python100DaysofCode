import random
a=random.randint(1,10)
print(a)
b=random.random()
print(b)
c=b*5
print(c)
d=b*5+1
print(d)

states_of_india=indian_states_by_formation_order = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh",
    "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka",
    "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram",
    "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana",
    "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"
]

print(states_of_india)
print(states_of_india[0])
print(states_of_india[-1])
a=states_of_india[-2]
states_of_india.append(['Jammu and Kashmir'])

fruits=['apple', 'banana','grapes']
vegetables=['tomato','potato']
shop=[fruits,vegetables]
print(shop)
import random
a=int(input("what do you chose ? Type 0 for rock , 1 for paper or 2 for scissors"))
rock = '''
r
'''

paper = '''
 p
'''

scissors = '''
    s
'''            

game=[rock,paper,scissors]
print(game[a])
print("computer chooses")
b=random.randint(0,2)
c=game[b]
print(c)
if b==a:
    print("draw")
elif a>=3 or a<0:
    print("invalid choice")
elif a==0 and b==1:
    print("you loose")
elif a==1 and b==0:
    print("you won")
elif a==0 and b==2:
    print("you won")
elif b==0 and a==2:
    print("you loose")
elif a==1 and b==2:
    print("you loose")
else:
    print("you won")
            

