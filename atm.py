total_price = 0
card_type = "visa"
is_same_bank = True
is_expired = False

print("Please insert your card: ")
required_amt = int(input("Please insert your required amount: "))

def read_card():
    card_details = [200000, False, False]
    total_price = card_details[0]
    is_same_bank = card_details[1]
    is_expired = card_details[2]
    if is_expired == False:
        print("Fetching data from the bank ...")
        perform_transaction(total_price, is_same_bank)
    else:
        print("Sorry, your card has been expired.")

def perform_transaction(total_amt, is_same_bank):
    if is_same_bank:
        charge = 0
    else:
        charge = 25

    if required_amt > total_amt:
        print("Not enough balance")
    else:
        print(f"Remaining balance is: {total_amt-required_amt-charge}")

read_card()







            
      

        
            




