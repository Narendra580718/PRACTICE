user_details = {
    "first_name" : "Narendra",
    "last_name" : "Maharjan",
    "contacts" : 9818142441,
    "nationality" : "Nepali",
    "language_spoke" : "Nepali",
    "fav_food" : "Pizza",
}

print(user_details["first_name"])


for key,value in user_details.items():
    print(f"The key is {key} and the value is {value}")

for key in user_details.keys():
    print(f"They keys are {key}")

for value in user_details.values():
    print(f"The values are {value}")