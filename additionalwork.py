#1 ask two integernumer with usee and a function should return their addition:
first = int(input("What is your first number: "))
second = int(input("What is your second number: "))

def addition():
    sum = first + second
    print(f"The addition of two numbers are: {sum}")
    return addition

addition()

#2 ask an informationof your laptop and function should return like this:
#brand_name, model_name price
#eg dell vostro @80000

brand_name = input("Please enter your brand: ")
model_name = input("Please enter your model: ")
price = int(input("Please enter your price: "))

def laptop_specs():
    print(f"{brand_name} {model_name} @ Rs. {price}")

laptop_specs()
