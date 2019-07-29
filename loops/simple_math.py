count1 = input("How much is 4 + 4?: ")

while count1 != "8":
    print("Sorry, try again.")
    count1 = input("How much is 4 + 4?: ")

else:
    count2 = input("Congrats! Next one: How much is 5 + 4?: ")
    while count2 != "9":
        print("Sorry, try again.")
        count2 = input("How much is 5 + 4?: ")

print("Congrats")
