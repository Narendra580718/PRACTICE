user_number = int(input('Enter your number: '))
dic = []

def dictionary(user_list):
    for num in range(1,user_list+1,1):
        dic.append(num)

dictionary(user_number)
print(f"Your numebrs are {dic}")

user_list = int(input("Enter your number: "))
even = []
odd = []

def seperate(user_number):
    for num in range (1,user_number+1,1):
        if num %2==1:
            odd.append(num)
        else:
            even.append(num)

seperate(user_number)
print(f"The even numbers are {even} and the odd numbers are {odd}")