f_name = input("your first name:")
l_name = input("your last name is:")

def your_fullname():
    print (f"your full name is:", f_name + " " + l_name )
    return f_name, l_name 

your_fullname()