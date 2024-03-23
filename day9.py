
#the secret auction program

bid={}
name=input("What is your name")
price=int(input("What is the bid price"))
bid[name]=price

ans=input("If there are more users who want to bid 'Y' or 'N'").lower()
while ans=='y':
  
  name=input("What is your name")
  price=int(input("What is the bid price"))
  bid[name]=price
  
  ans=input("If there are more users who want to bid 'Y' or 'N'").lower()

max_bid=0  
for key in bid:
  if bid[key]>max_bid:
    max_bid=bid[key]
    winner=key
print("the winner is", winner , "with the bid of :",max_bid) 

  
          
