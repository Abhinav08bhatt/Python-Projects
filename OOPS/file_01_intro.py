class Dog:

    def __init__(self, name, breed, owner):
        self.name_of_dog = name
        self.breed_of_dog = breed
        self.owner_of_dog = owner

    def bark(self):
        print("woof woof")


class Owner:
    def __init__(self, name, address, mobile_num):
        self.name = name
        self.address = address
        self.mobile_num = mobile_num


owner1 = Owner("richard", "123 street", "2435632")

dog1 = Dog("bruse", "german", owner1)
dog1.bark()
print(dog1.name_of_dog)
print(dog1.breed_of_dog)
print(dog1.owner_of_dog.name)

owner2 = Owner("sally", "123 street", "2435632")

dog2 = Dog("allly", "scotich", owner2)
dog2.bark()
print(dog2.name_of_dog)
print(dog2.breed_of_dog)
