class Dog:

    def __init__(self, name, breed):
        self.name_of_dog = name 
        self.breed__of_dog = breed 


    def bark(self):
        print("woof woof")

dog1 = Dog("bruse","german")
dog1.bark()
print(dog1.name_of_dog)
print(dog1.breed__of_dog)

dog2 = Dog("allly","scotich")
dog2.bark()
print(dog2.name_of_dog)
print(dog2.breed__of_dog)
