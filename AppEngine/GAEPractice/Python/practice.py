class Pet(object):
    def __init__(self, name, age, animal, mood):
        self.name = name
        self.age = age
        self.animal = animal
        self.is_hungry = False
        self.mood = mood

    def __str__(self):
        hungry_statement = "not hungry"
        if self.is_hungry:
            hungry_state = "hungry"
        description = "%s is a %s %s, and is %s" % (self.name, self.mood, self.animal, hungry_state)

        return description

    def eat(self):
        print("> %s is eating..." % self.name)
        if self.is_hungry:
            self.is_hungry = False
        else:
            print("> %s  may have eaten too much" % self.name)
            self.mood = "lethargic"



my_pet = Pet("Fido", 3, "lion", "ight")
pet_2 = Pet("Spanky", 8, "dog", "happy")
print(my_pet)

#other_pet = my_pet

#pet_2 = Pet("Spanky", 8)
#pet_3 = Pet("Bella", 1)
#print("%s is a %s %" % (my_pet.name, my_pet.mood, my_pet.animal))

#print("My animal's name is " + my_pet.name + " and age is " +
#        str(my_pet.age) + "he is a " + my_pet.animal + " ")
#print(my_pet)
#print(other_pet)




#abbreviation = raw_input("Enter state abbreviation")
#abbrev_upper = abbreviation.upper()
#if abbrev_upper in states:
#@else:
#    print(abbreviation + " not a state I know about")


#print(states["NY"])

#states["NY"] = "Amsterdam"

#print(states["NY"])
