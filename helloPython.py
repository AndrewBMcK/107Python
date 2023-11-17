#  let name = "andrew"

name = "andrew"
total = 12.50
found = False
age = 34
print(name)

#if statement

if age < 50:
    print("well looks like you are below 50 years old")
elif age > 50:
    print("you are older than 50 years old")

print("well looks like im outside of the if statement")

#functions

def say_hello():
    print("Hello")

def say_goodbye(name):
    print("Goodbye "+name)

#call the function

say_hello()
say_goodbye("Andrew")