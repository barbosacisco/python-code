name = input("Hello, please type your name: ")

if name != "":
    age = int(input("Great, now please type your age: "))
    diff = 100 - age
    diff = str(diff)
    message = "You will be 100 years old in " + diff + " years."
    number = int(input("Please type another number: "))
    print(message * number)
else:
    print("Sorry I need you to type your name in order to proceed. ")

