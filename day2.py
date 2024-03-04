##print(len('yash'))>>4
##print(len(12345))>>type error

#string data type

a="hello" 
print(a) #hello
print(type(a)) #<class 'str'>
print("HELLO"[0]) #H
print(a[4]) #o
print(type("123")) #<class 'str'>
print("1234"+"567") #1234567
b=str(123)
print(type(b)) #<class 'str'>

#Integer

print(123+345) #468
print(123_234_567) #123234567
c=123.67
print(int(c)) #123
print(type(10)) #<class 'int'>

#Float
print(456.678) # 456.678
print(type(34.78)) # <class 'float'>
a=124 
print(float(a)) # 124.0
b="456" 
print(float(b)) # 456.0
c=567.7 
print(type(c)) # <class 'float'>

#Boolean
print(True) #True
print(False) #False
a=True
print(type(a)) #<class 'bool'>
print(bool(0)) # False
print(bool(145))
print(bool('true'))
print(bool('false'))
print(bool({}))

##Mathematical manipulation
'''
5+3 
8
5-3
2
3-5
-2
3/5
0.6
5/3
1.6666666666666667
6/2
3.0
6**2
36
6*2
12
6%6
0
6%3
6%4
2
'''
'''
>>> 4//5
0
>>> 8//3
2
>>> 4//2
2
>>> round(8/3)
3
>>> 8/3
2.6666666666666665
>>> round(8/3,3)
2.667
>>> round(8/3,2)
2.67
>>> round(8/3,1)
2.7
'''
##Compound operators
result=4/2
result/=2 #2/2=1.0
print(result)

score=0
score=score+1 #1
score+=1 #2
score-=1  #1
score*=1 #1
score/=1 #1.0
print(score)

##f-string
score=10
height=1.8
isWinning=True
print(f"your score is {score} , your height is {height} and you are winning is {isWinning}.")
#your score is 10 , your height is 1.8 and you are winning is True.
##project - tip calculator
print("Welcome to the tip calculator.")
g=input("What was the total bill?")
h=g[1:]
a=float(h)
b=int(input("What percentage tip would you like to give? 10,12 or 15?"))
c=int(input("How many people to split the bill?"))
d=(a*b)/100
e=a+d
f=e/c
print(f)
i=round(f,2)
print(f"Each person should pay : ${i}")
      

