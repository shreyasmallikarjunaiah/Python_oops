
string="abcdef"
for i in string[len(string)::-1]:
	print(i)

class CashRegister:
	Tax=0.05
	def __init__(self):
		self.purchase = []

	def add_items(self, items,quantity=1):
		self.purchase.append({
			"name": items["name"],
			"price": items["price"],
			"quantity": quantity
		})

	def show_item(self):
		return self.purchase

	def remove_item(self, name):
		return self.purchase.remove(name)

	def total_ammount(self):
		return sum(
			item["price"] * item["quantity"]
			for item in self.purchase
		)

	def tax(self):
		return self.total_ammount() * self.Tax

	def grand_total(self):
		return self.tax() * self.Tax




my_cart = CashRegister()

while True:
	print('''
	1-add itemg
	2-show items
	3-delete item
	4-total_ammount
	5-grand total''')
	selection = (int(input("enter your choice:")))


	if selection==1:
		name=input("enter name:")
		price=int(input("enter price:"))
		quantity=int(input("enter quantity:"))
		items={"name":name,"price":price}
		my_cart.add_items(items,quantity)



	elif selection==2:
		my_cart.show_item()
		print(my_cart.show_item())



	elif selection==3:
		my_cart.remove_item(input("name the item "))
		print(my_cart.show_item())

	elif selection==4:
		my_cart.total_ammount()
		print(my_cart.total_ammount())

	elif selection==5:
		my_cart.grand_total()
		print(my_cart.grand_total())


