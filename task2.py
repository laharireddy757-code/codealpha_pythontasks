stocks = {
    "apple": 150,
    "tesla": 700,
    "google": 2800,
    "amazon": 3300,
    "microsoft": 300
}

total = 0

n = int(input("How many stocks do you want to add? "))

for i in range(n):
    name = input("Enter stock name: ").lower()
    qty = int(input("Enter quantity: "))

    if name in stocks:
        total += stocks[name] * qty
    else:
        print("Stock not found")

print("Total Investment Value:", total)