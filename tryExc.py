class nameError(Exception):
    pass
class ageError(Exception):
    def __init__(self):
        print("you are not eligible for voting")

try:
    name=input("enter your name = ")
    if(len(name)<=0):
        raise nameError
    age=int(input("enter your name = "))
    if(age<=21):
        raise ageError
except nameError :
    print("plz enter a valid name")
except ageError:
    pass
except Exception as e:
    print(e)
else:
    print("you are eligible for voting")
