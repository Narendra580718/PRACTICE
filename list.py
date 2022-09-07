days_list = [
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
]

my_value = days_list[3]
print(my_value)

days_list.append("Sun")
print(days_list)

print("Your recent days are ")
for days in days_list:
    print(days, end = " ")

days_list.pop()
print(days_list)


