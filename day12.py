import random
print("Welcome to the Number Guessing Game !")
print("I am thinking of a number between 1 and 100")

def attempt_type():
  '''
  choosing whether
  to chose easy or hard
  level
  '''
  level=input("Chose a attempt. Type 'easy' or 'hard' :")
  if level=='easy':
    attempt=10
  else:
    attempt=5
  return attempt

def random_number():
  a=random.randint(1,100)
  return a

def game_main():
  number=random_number()
  attempt=attempt_type()
  i=0
  while i<attempt:
    a=attempt-i
    print ("You have {0} remaining to guess the number".format(a))
    guess=int(input("Make a guess"))
    if guess==number:
      print("You made a guess correct ! ")
      break
    elif guess> number:
      print("Too high")
    else:
      print("Too low")
    i+=1
  else:
    print("You have run out of attempts. The number was {}.".format(number))
 
game_main()



      
