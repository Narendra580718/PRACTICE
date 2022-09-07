#1 ask two integernumer with user and a function should return their addition:

first_number = int(input("enter your first number: "))
second_number = int(input("enter your second number: "))

def addition(f_number, s_number):
    sum = f"{f_number + s_number}"
    print(sum )
    return sum

addition(first_number, second_number)

#2 ask an informationof your laptop and function should return like this:
#brand_name, model_name price
#eg dell vostro @80000

brand_name = input("Please enter your laptop brand: ")
model_name = input("Please enter your laptop model: ")
price = int(input("Please enter the price: "))

def laptop_specs(b_name, m_name, price):
    print(f"{b_name} {m_name} {price}")
    return laptop_specs

laptop_specs(brand_name, model_name, price)
