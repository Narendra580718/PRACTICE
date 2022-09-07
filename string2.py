f_name = input("your first name:")
l_name = input("yourlast name:")

def your_name():
    your_name = f_name + " " + l_name
    print(f"your full name is: {your_name}")
    return your_name

your_name()