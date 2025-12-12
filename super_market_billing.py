cart = {}

items_list = {
    "rice":10,
    "salt":20,
    "oil":150,
    "shampoo":40,
    "sandelsoap": 70,
    "horlicks": 120,
    "milkpowder":60,
    "mirchi powder":35,
    "sugar":65,
    "dhaal":20,
    "surf":55,
    "badam nuts":200,

}

name = input("Enter your name: ").lower()
print(f"Welcome to our super market {name}")

print("items         prices")
print("--"*25)
for items, prices in items_list.items():
    print(f"{items:15} {prices}")

while True:
    item_name = input("Enter you item name:")

    if item_name == "exit":
        break
    if item_name in items_list:
        print("you addedd item successfully")
        item_qantity = int(input("Enter your quantity: "))
        unit_price = items_list[item_name]
        total_price = unit_price * item_qantity
        cart[item_name] = {"quantity": item_qantity, "total": total_price}
        # print(f"Total price for your quantity = {total_price}")
    else:
        print("please enter valid input")

print("--"*25)
print("       FINAL BILL       ")
print("--"*25)
print("items           prices")
print("--"*25)

grand_total = 0

for item, details in cart.items():
    unit_price = items_list[item]
    print(f"{item:15} Qty: {details['quantity']} X Rs.{unit_price} = Rs.{details['total']}")
    grand_total += details['total']
    
tax_amount = grand_total * 0.12
final_total = grand_total + tax_amount


print("--"*25)
print(f"Subtotal: Rs.{grand_total}")
print(f"Tax (12%): Rs.{tax_amount}")
print(f"GRAND TOTAL: Rs.{final_total}")
print(f"Thank you {name} for purchasing in our super market")
      
        
    
                
    
        
        
        
           

        


