def add(*args):
    print(args)
    print(type(args))
    sum=0
    for n in args:
        sum+=n
    print(sum)

#add(1,2,3,4,5)

def calculate(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n=2
    n+=kwargs["add"]
    n*=kwargs["multiply"]
    b=kwargs.get("subtract")
    print(n,b)

calculate(add=3,multiply=5)

class Car:
    def __init__(self,**kwargs):
        self.make=kwargs.get("make")
        self.model=kwargs.get("model")

my_car=Car(make="Nissan")
print(my_car.model)