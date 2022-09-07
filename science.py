def calc_weight(m,g = 50):
    print(f"your weight is: {m*g}N")
    return m*g

mass = int(input(f"Please enter your mass:"))
print(f"your weight is : {calc_weight(mass)}N")