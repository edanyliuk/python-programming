import json

with open("orders.json", "r") as derulo_file:
    menu = json.load(derulo_file) # converts json file to python dictionary

print(type(menu))
print(json.dumps(menu, indent = 2)) #present info better than print(cohort). Dumps takes a dictionary and makes it into a string
#2 and 4 are the most common indents

customer_orders = menu

customer_total = 0
email_list = []
for email in customer_orders:
    email_list.append(email["customer_email"])
         
customer_total = len(set(email_list))
print(customer_total)

answer = ""
for customer in customer_orders:
    if customer["id"] == 13:
        answer += customer["customer_name"] + " " + customer["customer_email"]

print(answer)

orderfortwenty = []
for customertwenty in customer_orders:
    if customertwenty["id"] == 20:
        for order in customertwenty["orders"]:
            orderfortwenty.append(order["item"])

print(orderfortwenty)

binge_drinkers = []
for alcoholic_customer in customer_orders:
    for booze_item in alcoholic_customer["orders"]:
        if "Wine" in booze_item["item"]:
            binge_drinkers.append(alcoholic_customer["customer_name"])

print(binge_drinkers)

matti_spend = 0
for customer_matti in customer_orders:
    if customer_matti["customer_name"] == "Matti":
        for order_prices in customer_matti["orders"]:
            if "$" in order_prices["price"]:
                matti_spend += float(order_prices["price"])

print(matti_spend)


