gas = "G"
oil = "O"
num_hypen = 50
banner = "-" * num_hypen
message = "Welcome to Gas Station Supplier Program!"
full_banner = f"{banner}\n {'*' * 3} {message} {'*' * 3}\n{banner} "
print(full_banner)

selection = input("Please select the type of purchase: \n G:Gas\n O:Oil\n >>> ").upper()
number_of_liter = float(input(" Please enter the number of litres of gas:"))
gas_price = float(number_of_liter * 1.07)

if number_of_liter > 4000:
    discount = gas_price * 0.9
    print(f"the total price of gasoline is {discount}")
else:
    print(f"the total price of gasoline is {gas_price}")
