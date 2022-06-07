import namer_module

#variables

first_name = "James"
address = "308 w main"

print (address)



#data types
#strings
#numbers
#lists
#tuples
#dictionaries


#list [], you can also place numbers & variables in a list, len will figure out how many items are in the list
first_name = ["john", "bob", "tina"]
print(first_name[2])

del first_name[1]

print(len(first_name))

#tuple () tuples are faster than lists, big projects tuples are faster
first_name = ("john", "bob", "tina")
print (first_name[2])


tuple_1 = ('john', 'bob', 'mary')
tuple_2 = ('tine',)

tuple_3 = tuple_1 + tuple_2
print (tuple_3)
print(tuple_1[0:2])

#dictionaries
fav_pizza = {
    "jon": "pep",
    "bob": "cheese",
    "tina": "supreme"
}
print(fav_pizza["tina"])

del fav_pizza["jon"]

fav_pizza.update({'Tim': 'green peppers'})   #this adds to the dictionary

#strings    \ and \n\ creates a new line
talking = 'my mom yelled "CLEAN YOUR ROOM"'

talking_2 = "my mom yelled \n\"CLEAN YOUR room\""

print(talking)
print(talking_2)

#string manipulation .upper capitalizes everything, .title captilizes first letter, .lower, len is also another way to get functionality
my_string = "my name is james goff"
print(my_string.title())
print(my_string[3:len(my_string)])
print(my_string.split (' ')[2])
print(my_string.split (' ')[2].upper())


#math
print (2 + 3)
print (2 - 3)
print (2 * 3)
print(2 ** 8) #to the power of
print(9 % 3) #prints the remainder
print((3 + 1) **4)

num_1 = 3
num_2 = 4

print(num_1 * num_2)

#numbers     integer or ints is a whole number, floats are decimal numbers
num_1 = 10
num_2 = 3

print(num_1/num_2)

print(round(num_1/num_2), 4)



#assignment operator +-*/%
num = 41
num *= 3

print (num)



#comparison operator   ==  !=  <  >  <=  >=

first_name = "jon"

print(10 == 10)
print(9 >= 10)


#conditional statements

num = 20
if(num < 10):
    print ("your number is greather than 10")

elif (num ==3):
    print("your number is pretty cool")

else:
    print ("your number is garbage")  



#multiple conditional statements (and, or)


num = 20
if(num > 10) or (num > 100):
    print ("your number is greather than 10")





#while loops

counter = 20
while (counter > 10):
    print ("the count is: %s" % counter)
    counter -= 2


#for loops

name = ["bob", "jon", "tina"]

for x in name:
    print(x)


fav_pizza = {
    "jon": "pep",
    "bob": "cheese",
    "tina": "sup"
}

#dictionaries deal with keys and values

for key, value in fav_pizza.items():
    print(value)

for key, value in fav_pizza.items():
    print(key)





#fizzbuzz program

#while loop:::
count = 0
while (count < 101):
    count += 1
    if (count % 3 == 0) and (count % 5 == 0):
        print("%s - FIZZBUZZ!" % count)
#if numbers in list of 0 -101 are divisible by 3 and 5, print FIZZBUZZ!
    elif (count % 3 == 0):
        print("%s - Fizz!" % count)
#if numbers in list of 0-101 are ONLY divisible by 3, print fizz!
    elif (count % 5 == 0):
        print ("%s - buzz!" % count)
#if numbers in list of 0-100 are ONLY divisible by 5, print buzz!
    else:
        print(count)
#otherwise print the other numbers in the list from 0-101


#for loop:::
count = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)

for x in count:
    if (x % 3 == 0) and (x % 5 == 0):
        print("%s - FIZZBUZZ!" % x)
#if numbers in list of 0 -20 are divisible by 3 and 5, print FIZZBUZZ!
    elif (x % 3 == 0):
        print("%s - Fizz!" % x)
#if numbers in list of 0-20 are ONLY divisible by 3, print fizz!
    elif (x % 5 == 0):
        print ("%s - buzz!" % x)
#if numbers in list of 0-20 are ONLY divisible by 5, print buzz!
    else:
        print(x)
#otherwise print the other numbers in the list from 0-101



#functions
print("hello") #this is a function

def namer(name):
    print("hello %s" % name)

namer("jon")

def namer(first_name, last_name):
    print("hello %s" % first_name)
    print("hello %s" % last_name)

namer("jon", "smith")



def mather(num1, num2):
    print (num1 + num2)

mather(4, 5)



#functions part 2

def namer(name):
    return ("Hello %s" % name)


my_namer = namer("john")

print(my_namer.upper())

print(namer("John garbage"))


for letter in my_namer:
    print(letter)



#modules, importing modules (namer_module.py)
print(namer_module.namer("john"))



#classes
first_name = "jon"

print(first_name.upper())


#classes part 1 & 2 methods within classes, calling methods in classes

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

    def perimeter(self):
        return self.side_length * 4        

    def report(self):
        print ("side length: %s" % self.side_length)
        print ("area: %s" % self.area())
        print ("perimeter: %s" % self.perimeter())


    



my_square = Square(10)
my_square.report()



