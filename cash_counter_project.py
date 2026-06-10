



# class CashRegister:
#     def __init__(self):
#         self.items=[]
#
#     def add(self,item=input("Enter item to add")):
#         self.items.append(item)
#         return self.items
#
#
#
# my_item=CashRegister()
# print(my_item.add())
#
#
# items={"pizza":{"price":100}}
# print(items["pizza"])




class CashRegister:
    TAX_RATE = 0.05

    def __init__(self, cashier_name):
        self.cashier_name = cashier_name
        self.purchase = []

    def add_product(self, product, quantity=1):
        self.purchase.append({
            "name": product["name"],
            "price": product["price"],
            "quantity": quantity
        })

    def show_products(self):
        if not self.purchase:
            print("Cart is empty.")
            return

        print("\nProducts in Cart:")
        for item in self.purchase:
            print(f"{item['name']} - ${item['price']} x {item['quantity']}")

    def remove_product(self, name):
        self.purchase = [
            item for item in self.purchase
            if item["name"] != name
        ]

    def get_subtotal(self):
        return sum(
            item["price"] * item["quantity"]
            for item in self.purchase
        )

    def get_taxes(self):
        return self.get_subtotal() * self.TAX_RATE

    def get_total(self):
        return self.get_subtotal() + self.get_taxes()

    def clear_purchase(self):
        self.purchase.clear()


register = CashRegister("Shreyas")

while True:
    print("\n===== CASH REGISTER =====")
    print("1. Add Product")
    print("2. Show Products")
    print("3. Remove Product")
    print("4. Show Total")
    print("5. Clear Purchase")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Product Name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        product = {
            "name": name,
            "price": price
        }

        register.add_product(product, quantity)

    elif choice == "2":
        register.show_products()

    elif choice == "3":
        name = input("Enter product name to remove: ")
        register.remove_product(name)

    elif choice == "4":
        print(f"Subtotal: ${register.get_subtotal():.2f}")
        print(f"Tax: ${register.get_taxes():.2f}")
        print(f"Total: ${register.get_total():.2f}")

    elif choice == "5":
        register.clear_purchase()
        print("Purchase cleared.")

    elif choice == "6":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")