

"""
# Break statement Example:

print("Output with 'break':")
for i in range(10):
    if i == 7:
        print(f"Encountered 'break' at i={i}") 
        break
    print(i)


print('''
----------------------------
----------------------------
      ''')
# Continue Statement Example 
print("\nOutput with 'continue':")
for i in range(5):
    if i == 2:
        print(f"Skipped iteration with 'continue' at i={i}")
        continue
    print(i)





def greet():

    y = 10 + 5
    x = int(input("The number you want to sum with y \n"))

    print(f"the number is {x + y}")

# Call the function to execute
greet()



# Comparison Operators 
age = 15
is_adult = age >= 18
is_teenager = age >= 13 and age < 18
print("Is adult?", is_adult)
print("Is teenager?", is_teenager)

"""


"""
def sajid() :
    print("Hi I am Sajid Hossain. I am here to introduce you about ourselves.")

    name_of_their = str(input("What is your name?"))

    print(f"Hello, {name_of_their}")

sajid()

"""
import random
print("Welcome to Love Calculator!")
name1 = str(input("What is your name? \n"))
name2 = str(input("What's your crush's name? \n"))

print(f"Your love score is {random.randint(1,100)}")

