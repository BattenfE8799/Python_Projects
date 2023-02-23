# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:47:54 2023

@author: Elizabeth

Notes for Working with Python
"""

"""
    PRINT
"""
print("\t\n\nPRINT\n\n")
#adds tab to printed words
print("\tTabbed Words")
#adds new line to printed words
print("\nNew line Words\n")


"""
    STRINGS
"""
print("\t\n\nSTRINGS\n\n")
message_string = "emily bolling"
# changes first letters into capital
print("Titled: ",message_string.title())
# changes all letters into upper
print("Upper case: ",message_string.upper())
# changes all letters into lower
print("Lower case: ",message_string.lower())
# magical f string
print(f"My name is {message_string}! F string is magical")

#strips whitespace at right and left
whitespace = " words with whitespaces "
print(whitespace.strip())
#strips whitespace at right
print("No whitespace at right: ", whitespace.rstrip())
#strips whitespace at left
print("No whitespace at left: ", whitespace.lstrip())

"""
    NUMBERS
"""
print("\t\n\nNUMBERS\n\n")
# INTIGERS
# add
print("integers")
print("2+2:", 2+2)
# subtract
print("2-2:", 2-2)
# multiply
print("2*2:", 2*2)
# divide
print("2/2:", 2/2)
# exponents
print("2**2:", 2**2)

# FLOATS
#do same thing as above just with . in it
#float with integers equals float number

# UNDERSCORES
#added to make it readable in code not in print
numbers_underscored = 4_333_999
print("Adding underscores to numbers in codes make it easier to read in code: ",numbers_underscored)

"""
    LISTS
"""
print("\t\n\nLISTS\n\n")
list1 =  ["one","two","three","four","five"]
#call first item in list
print("Call first item in list: ",list1[0])
print("Call first item in list and title it: ",list1[0].title())
#call last item in list
print("Call first item in list: ",list1[-1])

# MODIFYING LISTS

#exchange an item on list for another
list1[0] = "zero"
print("modify list:",list1)
#add to end of list
list1.append('six')
print("add to end of list:",list1)
#add specific point of list
list1.insert(5,'seven')
print("add to specific point of list:",list1)
#remove specific entry of list
del list1[0]
print("remove specific entry of list:",list1)
#create a new list from a removed item from a list
list2 = list1.pop()
print("Create a new list from a removed item from a list:", list2)
print(list1)
#remove item by key
list1.remove('two')
print("Remove item in list by key:", list1)
#exercise to remove key from list
print()
print("Exercise to remove key from list")
item1 = 'key'
list3 = ['sword','shield','key']
print(list3)
list3.remove(item1)
print("You used the key.")
print(list3)
#sorting a list
list1.sort()
print("Sort a list alphabetically: ", list1)
#sorting a list reversed
list1.sort(reverse=True)
print("Sort a list reverse alphabetically: ", list1)
# sorting a list temporaryily
print("Sorting a list temporarily:", sorted(list1))
# sorting a reverse list temporarily # not working right
print("Sorting a list temporarily:", sorted(list1,reverse=True))
#printing in reverse order
list1.reverse()
print("Reverse sorts the list permanently:", list1)
#finding a length of a list
print("Find the length of a list:",len(list1))
#count the amount of a specific element is in a list
print("Count the amount of a specific element is in a list:", list1.count('one)'))
#slicing a list
list3 = ['shield','sword','key','gem', 'rock']
print("Slicing the list: ",list3[0:3])
#omitting the first number starts it from the start of the list
#omitting the last number ends it at the end
#putting a negative as fist number will pull from end of list
print("Slicing the list: ",list3[-3:])
#copying a list, use a empty slicing to get all the list
list4 = list3[:]

#checking if value is in list
print("Do you have key?",'key' in list3)
print("Do you have key?",'key' in list2)

"""
    LOOPING LISTS
"""
print("\t\n\nLOOPING LIST\n\n")
#loops item in a list print each item in a new line
for item in list3:
    print(item)

#range function
for value in range(1,5):
    print(value)
    
#make a list of numbers using range
numbers = list(range(1,6))
print(numbers)
#make a list of even numbers using range
even_numbers = list(range(1,6,2))
print(even_numbers)
#squares list
squares = []
for value in range(1,11):
    squares.append(value**2)
squares = [value**2 for value in range(1,11)]  #consise version
print(squares)
#
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#looping through a sliced list
print("Here are the last three items in the invintory:")
for item in list3[-3:]:
    print(item.title())    

"""
    TUPLES
"""
print("\t\n\nTUPLES\n\n")
#TUPLES are lists that cannot be changed
tuple1 = ("Sword","Shield")
print(tuple1[0])
print(tuple1[1])
#tuples are defined by a comma, you can have only one item in it but include the comma
tuple2 = ("Key",)
print(tuple2)

#looping through a tuple
for item in tuple1:
    print(item)

#wtite over a tuple
tuple1 = ("Key", "Gem")
print("Modified tuple:")
for item in tuple1:
    print(item)
    
"""
    IF STATEMENTS
"""
print("\t\n\nIF STATEMENTS\n\n")
list4 = 'Key'
for item in list3:
    if item == "key":
        print("You have a key.")
    else:
        print("You don't have the key...")

# use .lower() to take away capital issues
for item in list4:
    if item.lower() == 'key':
        print("You have a key.")
    else:
        print("You don't have the key...")
        
#checking if two values are not equal
for item in list4:
    if item.lower() != "key":
        print("You have a key.")
    else:
        print("You don't have the key...")
        
#you can check it with  < > <= >= or ==
number = 22
if number < 30:
    print("Item is less than 30.")
else:
    print("item is not less than 30")
if number <= 30:
    print("Item is less than or equal to 30.")
else:
    print("Item is not less than or equal to 30.")
if number > 30:
    print("Item is greater than 30.")
else:
    print("Item is not greater than 30.")
if number >= 30:
    print("Item is greater than or equal to 30.")
else:
    print("Item is not greater than 30.")
#you can combine two checks in one
age = 30
if age >=18 and age >= 21:
    print("You are of age to vote and drink")
else:
    print("You are not the correct age.")

#improve readability
if (age >=18) and (age >= 21):
    print("You are of age to vote and drink")
else:
    print("You are not the correct age.")

#checking if value is in list
print("Do you have key?",'key' in list3)
print("Do you have key?",'key' in list2)

#checking to see item is not in list
if 'key' not in list2:
    print("You dont' have the key")

#if elif else statement
#if no else then it must be very specific on tests
if age > 18:
    print("You are less than 18 years old.")
elif age >= 18:
    print("You are 18 or older.")
else:
    print("What is your age again?")

#multiple if statements
if 'sword' in list3:
    print("You have a sword")
if "shield" in list3:
    print("You have a shield")
if "gold" in list3:
    print("You have gold")
if "gold" not in list3:
    print("You have no gold")
print("That is it.")

# checking for special items
for item in list3:
    print(f"You have a: {item}")
print("Thats all your items.")

for item in list3:
    if item == 'gem':
        print("Its sooo shiny, this gem")
    else:
        print(item)
print("This is all you items.")
#checking to see if list is not empty
invintory = []
if invintory:
    for item in invintory:
        print(item)
else:
    print("You have nothing in your invintory.")

#using multiple lists
ages = [22,23,24,16]
userage = [22,16,13]
for age in userage:
    if age in ages:
        print("This is a good age.")
    else:
        print("Sorry that is not a correct age.")
avail_toppings = ['mushrooms','cheese','extra cheese']
requested_toppings = ['mushrooms','french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in avail_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry we don't have {requested_topping}")
print("\nFinished makikng pizza.")

"""
    BOOLEAN EXPRESSIONS
"""
print("\t\n\nBOOLEAN EXPRESSIONS\n\n")

won = False
game_active = True

"""
    DICTIONARYS
"""
print("\t\n\nDICTIONARYS\n\n")
alien = {'color':'green','points':'5','description':'green alien'}
dict1 = {'shield':'rusty', 'sword':'shiny'}
print(dict1['sword'])
print(dict1['shield'])

newpoints = alien['points']
print(f"{newpoints} points")

#add new key-value pair
alien['x-position'] = 0
alien['y-position'] = 25
print(alien)

#starting from empty dictionary
alien1 = {}

alien1['color'] = 'red'
alien1['points'] = 10
print(alien1)

#modifying values
print(alien1)
alien1['color'] = 'blue'
print(alien1)

#moving an alien using speed
alien['speed'] = 'medium'
print(f"orignal postion: {alien['x-position']}")
if alien['speed'] == 'slow':
    x_increase = 1
elif alien['speed'] == 'medium':
    x_increase = 2
else:
    x_increase = 3

alien['x-position'] = alien['x-position'] + x_increase
print(f"new position: {alien['x-position']}")

#removing key-value pairs
del alien['points']
print(alien)
description = alien['description'].title()
print(description)


#using get() to access values
pointvalue = alien.get('points','No points')
print(pointvalue)

pointvalue = alien1.get('points','No points')
print(pointvalue)

#looping through a dictionary
for k, v in alien.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

for item, description in alien.items():
    print(f"\nItem: {item}")
    print(f"Description: {description}")    

invintory = {"sword":"rusty","key":"golden","shield":"hardy"}
requ_attack = ['sword','shield']
for item in invintory.keys():
    if item in requ_attack:
        description = invintory[item].title()
        print(f"\t{item.title()}, is {description}")
        
invintory = {"sword":"rusty","shield":"hardy"}
requ_attack = ['sword','shield']
if 'sword' in invintory and 'shield' in invintory:
    print("You have your sword and shield ready to go.")
if 'key' not in invintory.keys():
    print("You don't have a key")
#looping through all the keys
for item in alien.keys():
    print(item.title())

#loop through dictionary and return sorted keys
for item in sorted(alien.keys()):
    print(f"{item.title()}")

#looping through all values in dictionary
print("The alien is:" )
for item in alien.values():
    print(item)

#looping with repitition, removing repition
invintory['key'] = 'gold'
invintory['statue'] = 'gold'
for item in set(invintory.values()):
    print(item)

"""SETS
"""
#you can build set by using braces and seperating with comma
stuff = {'python','cage','water dish','python'}
print(stuff)

"""NESTING DICTIONARY/LIST
"""
# a list of dictionaries

gold = {'value':1,'weight':0,'description':'shiny'}
sword = {'value':5,'weight':6,'description':'rusty'}
shield = {'value':5,'weight':10,'descirption':'hardy'}

invintory = [gold,sword,shield]
for item in invintory:
    print(item)
    
#making aliens

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)

