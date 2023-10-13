print("--------------------------------------------------")
print("*** Welcome to Gas Station Supplier Program! ***")
print("--------------------------------------------------")
type = input("Please select the type of purchase:\nG: Gas\nO: Oil\n>>> ")

if(type == "O" or type == "o"):
    product = "Oil"
    cases = float(input("Enter # of cases of Oil: "))
    litres = cases * 12
    original_cost_per_litre = 1.27
    price_before = litres * original_cost_per_litre
    if cases > 8:
        price_after = price_before * 0.9
    else:
        price_after = price_before

