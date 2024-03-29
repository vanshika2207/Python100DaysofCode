class User:
    def __init__(self,user_id,username):
        print("welcome")
        self.id=user_id
        self.username=username
        self.follower=0
        self.following=0
    def follow(self,user):
        user.follower+=1
        user.following+=1


user_1=User('001','vanshika')
user_2=User('002','teesha')
print(user_1.follower)
user_2.follow(user_1)
print(user_1.follower)
print(user_1.following)

