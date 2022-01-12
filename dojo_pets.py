class Ninja:
    def __init__(self, first_name, last_name ,treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    # walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        self.pet.play()

        return


    # feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        self.pet.eat()

        return


    # bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        self.pet.noise()

        return





class Pet:
    def __init__(self, name , pet_type , tricks, sound):
        self.name = name
        self.type = pet_type
        self.tricks = tricks
        self.energy = 10
        self.health = 10
        self.sound = sound


    # sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(self.energy)

        return 

    # eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.name+"'s health rose to "+str(self.health)+" and energy rose to "+str(self.energy)+"!")

        return

    # play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(self.name+"'s health rose to " + str(self.health) + "!")

        return

    # noise() - prints out the pet's sound
    def noise(self):
        print(self.sound)

        return


# end of classes


# instances

rover = Pet("Rover", "Dog", ["Fetch", "Roll over"], "Woof!")
seven = Ninja("Seven", "Six", "cookies", "dry food", rover)

seven.feed()
seven.bathe()
seven.walk()