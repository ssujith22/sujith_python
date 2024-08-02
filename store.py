items = [{"ItemID":1,"ItemName":"sugar","ItemPrice":40},
        {"ItemID":2,"ItemName":"Biscuit Marie Gold","ItemPrice":30},
        {"ItemID":3,"ItemName":"Apple","ItemPrice":175},
        {"ItemID":4,"ItemName":"Mango","ItemPrice":120},
        {"ItemID":5,"ItemName":"Milk","ItemPrice":36},
        {"ItemID":6,"ItemName":"Eggs","ItemPrice":8}
        ]
cart = []

def view_store():
    print("Available items in the store:")
    for item in items:
        print(f"ID:{item['ItemID']},Name:{item['ItemName']},Price:{item['ItemPrice']}")

def purchase_item():
    while True:
        item_id = int(input("Enter the item id to purchase: "))
        quantity = int(input("Enter the quantity: "))
        item = next((item for item in items if item["ItemID"]==item_id),None)
        if item:
            cart.append({"ItemID":item["ItemID"],"ItemName":item["ItemName"],"quantity":quantity,"ItemPrice":item["ItemPrice"],"Total":item["ItemPrice"]*quantity})
        else:
            print("Item not found")
        cont = input("Do you want to continue adding items? (yes/no): ").lower()
        if cont!= 'yes':
            break

def generate_invoice():
    with open("invoice.txt","w") as f:
        f.write("*** invoice copy ***\n")
        total_amount =0
        for idx, item in enumerate(cart,start=1):
            f.write(f"{idx}.{item['ItemName']}\t{item['quantity']}\t{item['ItemPrice']}\t{item['Total']}\n")
            total_amount += item['Total']
        f.write(f"\nTotal: {total_amount}")
        print("Invoice has been generated and saved to invoice.txt.")
    
def main_menu():
    while True:
        print("\n1.View the store")
        print("2.Purchase the item")
        print("6.Exit and Generate Invoice")
        #print("*" *70)
        print("\n")
        choice = int(input("Enter you choice: "))

        if choice == 1:
            view_store()
        elif choice ==2:
            purchase_item()
        elif choice ==6:
            generate_invoice()
            break
        else:
            print("Invalid choice, Please try again.")

main_menu()
            
