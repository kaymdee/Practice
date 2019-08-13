name = raw_input("What is your name? ")
print("Listen ")
print(name)

/* word = raw_input(Enter: )
for letter in word:
    print(word)
print("\n")
print((word + " ") + len(word))
*/

////////////

thing = raw_input("Type anything ")
print("The thing is of type: " + str(type(thing)))

///////////////
thing = raw_input("Enter: ")
thing2 = type(float(thing))
print("THE IS OF TYPE: ""+ str(float(thing))
///////////
age = raw_input("How old are you? ")

print("You were born in the year: ")
print(2019 - int(age))

/////////////

num = raw_input("Enter an Number: ")
num2 = raw_input("Enter another Number: ")

print "The sum is: " + str((int(num)+int(num2)))
//////////////////

num = raw_input("Enter an Number: ")
if not isinstance(num, (int,long));
    print "ERROR you did not enter an integer: " + num1
    return
    exit()
------------
num = raw_input("Enter an Number: ")
if not num1.isdigit()
    print "ERROR you did not enter an integer: " + num1
    return
    exit()
    ///////////////////////////

noun1 = raw_input("Enter a noun: ")
noun2 = raw_input("Enter another noun: ")
verb = raw_input("Enter a verb: ")
adj = raw_input("Enter a adjective: ")

print("The " + noun1 + "j umped over a "
+ adj + " " + noun1 + " Then the " + noun2
+ " decided to stop being so " + adj
+ " and take up a hobby: "+ verb)
//////////

num = raw_input("Enter an Number: ")
if not num1.isdigit()
    print "ERROR you did not enter an integer: " + num1
    return
    exit()

num2 = raw_input("Enter another Number: ")
if not num2.is

print"The sum is: " + str((int(num)+int(num2)))
/////////////////////

//eXCERSISE 2
s = raw_input("Enter a string: ")
def reverse_string(s):
    return s[::-1]
print(reverse_string(s))

//////////////////// eXCERSISE 3
def sum_to_n(num):
    total = num
    //creating another varible so that total keeps track
    //of the number, while num is stopping point
    for i in range(num, 0, -1):
        total = total + i
    return total

print sum_to_n(4)
//////////////////////
#append to be added to the end, insert for  specific location
students = ["Alex", "Bob", "Charlie"]

print(students[0] + ", " + students[2] + " and " +
    "are characters in security stories.")

students.append("David")
print(students)
#Note diffent List outputs
students.insert(3, "Chuck")
print(students)

students.remove("Chuck")
print(students)

/////////////////////
 #append to be added to the end, insert for  specific location
 students = ["Alex", "Bob", "Charlie"]

 print(students[0] + ", " + students[2] + " and " +
     "are characters in security stories.")

 students.append("David")
 print(students)

 students.insert(3, "Chuck")
 print(students)

 students.remove("Chuck")
 print(students)

 def story_message(students):
     message = "" #set variable equal to 'empty string' (empty string = "")
     for index in range(0,len(students) - 1):
         message = message + students[inde] + ", "
     message = (message + " and " + students[-1] +
     " are characters in security stories")
     print message

 story_message(students)
//////////////////////////
states = {
    "NY": "New York",
    "CA": "California",
    "TX": "Texas",
    "GA": "Georgia",
    "TN": "Tennesse",
    "IL": "Illinois"
}
#Dictionary has no use for slicing as dictionaries are unorderd
states.pop("CA")
for state in states:
    print(state + " is " + states[state])

#abbreviation = raw_input("Enter state abbreviation")
#abbrev_upper = abbreviation.upper()
#if abbrev_upper in states:
#@else:
#    print(abbreviation + " not a state I know about")


#print(states["NY"])

#states["NY"] = "Amsterdam"

#print(states["NY"])

////////////////////////


#Dictionaries can go in list
pets = [
    {
        "name": "Ein",
        "Animal": "dog",
        "speies": "Corgi",
        "age": 5,
        "toys": ["ball", "frisby"]
    },
    {
        "name": "Marine",
        "Animal": "cat",
        "speies": "Calico",
        "age": 11
    }
]
pets.add()

print ("Adding 1 to " pets u7[""]]
print((pets[0]["age"])]''
////////////////////////////////
## FIXME:
class Pet(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __init__(self, name, age):
        self.name = name
        self.age = age

my_pet = Pet("Fido", 3)
other_pet = my_pet

pet_2 = Pet("Spanky", 8)
pet_3 = Pet("Bella", 1)

print("My pet's name is " + my_pet.name + " and age is " +
        str(my_pet.age))
print(my_pet)
print(other_pet)

//////////
