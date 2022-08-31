#EC2 Random Name Generator

import string
import time
import random

greetings = ['Hello', 'Hi', 'Hey', 'Howdy', 'Hola']

#greet your user and ask their name
value = random.choice(greetings)
print(value + ', User!')
print("Welcome to your EC2 Random Name Generator!") 
name = input("What is your name?\n")
print(("Thank you. Nice to meet you, ") + (name.capitalize()) + ("."))

#get the users department name to see if it is approved
dept = input("Do you work in Accounting, Marketing, or FinOps?\n").upper()

#user needs to be in an approved department
while True:
    try:
        list = ["ACCOUNTING", "MARKETING", "FINOPS"]
        if dept not in list:
            raise ValueError
        break
    except ValueError:
        print("Access Denied")
        exit()
    else: 
        print("Great, let's get started.")
        
#get the number of instances needed by the user
while True:
    try:
        instnumb = int(input("How many names are you needing today? "))
        print("Great! We will get you " + str(instnumb) + (" random instance names now!"))
        print("Here is your list, prepare to copy:")
        time.sleep(1.5)
    except ValueError:
        print("Numbers between 1-5 only. Please try again.")
        continue
    else:
        break
    
#random names will be generated

n = instnumb
N = 3

for _ in range(n):
    custom_id = str(''.join([random.choice(string.ascii_letters + string.digits) for instnumb in range(10)]))
    print('{}-{}'.format(dept[0 : N], custom_id))
    
print(("Thanks for using the Random Name Generator, ") + (name.capitalize()) + (". See you next time."))