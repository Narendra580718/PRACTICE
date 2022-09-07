name = input("What is your name: ")
age = int(input("What is your age: "))

if age < 0 :
    print("Invalid")

elif age > 10 :
    print(f"Dear {name}, your price will be Rs.150")

elif age == 10:
    print(f"Dear {name}, your price will be Rs.100")

elif age < 10 :
    print(f"Dear {name}, your price wil be Rs.50")
