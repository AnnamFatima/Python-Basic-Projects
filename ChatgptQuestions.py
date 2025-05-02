'''
def greet_user(name):
    return f"Assalamualikum, {name}! You're ready to slay the day."

user_name = input("Enter your name: ")
message = greet_user(user_name)
print(message)
'''

'''
age = int(input (" Enter your age: "))

if age < 3:
    print("You're a baby")
elif age < 13:
    print("You're a child")
elif age < 20:
    print("You're a Teenager")
else:
    print("You're an adult")
'''
'''
for i in range (1,6):
    print("I am learning Python Day- ", i)
'''

'''
count = 1
while count <= 5:
    print("This is count : " , count)
    count += 1
    '''

'''
for i in range (1,6):
    print("I am Annam, I rise again")
'''

'''
count = 10
while count >=1:
   
    print (count)
    count -=1
    '''

'''#Print a square of stars

for i in range(5):
    for j in range (5):
        print("*" , end=" ")
    print()
    '''

'''#Print a right angled triangle

for i in range(1,6):
    for j in range (i):
        print("*", end=" ")
    print()
    '''

'''
#Print a square of # using nested loops

for i in range (5):
    for j in range (5):
        print ("#" , end= " ")
    print()
    '''

'''
#Print a triangle with your daughter’s name instead of *

name = "Qunoot"
for i in range (1,6):
    for j in range(i):
        print(name , end=" ")
    print()
    '''

'''
#Bonus: Try using numbers (1, 2, 3...) in a triangle

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    '''

'''
#Write a loop that prints numbers 1–10 but skips 5 using continue.

for i in range (1,11):
    if i == 5 :
        continue
    print(i)
    '''

'''
#Write a loop that stops completely if number equals 7 using break.

for i in range (1,11):
    if i == 7:
        break
    print(i)
    '''

'''
#Using pass in an if condition (just for practice)
for i in range (1,6):
    if i ==3:
        pass
    print(i)'''

#WHILE LOOP

'''
#Write a while loop that prints numbers 1 to 5.

counter = 1
while counter <= 5:
    print(counter)
    counter = counter + 1
    '''

'''
#2. While loop that prints even numbers from 2 to 10

counter = 2
while counter <=10:
    print (counter)
    counter = counter + 2
    '''

'''
#3. While loop that stops when you reach 7 (using break)

counter = 1
while counter <=10:
    if counter == 7:
        break
    print(counter)
    counter = counter+1
'''

'''#A loop that prints numbers 1 to 5.

for i in range (1,6):
    print (i)

#Skip number 3 using continue.

for i in range (1,6):
    if i == 3:
        continue
    print (i)
'''

'''#Break the loop if the number is 4.
for i in range (1,6):
    if i == 4:
        break
    print(i)
'''

'''# Write a function that prints “Bismillah, let’s begin!”

def begin():
    print("Bismillah, Let's Begin!")

begin()'''

'''#Write a function that adds two numbers and prints the result.
def add(x,y):
    print(x + y)
add(5,7)
'''

'''#Write a function that takes your daughter's name as input and says "You are a blessing, [name]!"

def name(Qunoot):
    print(f"You are a blessing, {Qunoot}!")

name("Qunoot")'''

'''#Write a function to greet a user by name.

def Greet(name , greeting="Hello"):
    return(f"{greeting} {name}")
print(Greet("Annam"))'''

'''#Write a function that takes two numbers and returns their sum.

def sum(x,y):
    print(x + y)

sum(11,20)'''

'''#Write a function to calculate BMI (takes weight & height).
def calculate_bmi():

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = weight / (height **2)
    print(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi <25 :
        print("You have a normal weight.")
    elif 25 <= bmi < 30 :
        print("You are overweight.")
    else:
        print("You are obese")
calculate_bmi()
'''

