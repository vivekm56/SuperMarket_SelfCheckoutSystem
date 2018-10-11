from products import Products

	class CheckoutRegister:
	def __init__(self):
		self.currentBarCode = input('Please enter the bar code of your item: ')

	def scan_item(barCode):
		code = int(barCode)
		items = Products.items
		if(code in items):
			item = items[code]
			Products.totalAmount += item['price']
			Products.dueAmount += item['price']
			return {'message': item['name'] + ', '+ item['unit'] + ' - $' + str(item['price']), 'item': item}
		return {'message': 'This product does not exist in out inventory.'}

	def accept_payment(amount):
		if(amount < 0):
			print("We don't accept negative money!")
		else:
			Products.paymentReceived += amount
			Products.dueAmount = Products.dueAmount - amount


	def print_receipt():
		print('\n\n-----Final Receipts-----')
		for i in Products.totalProducts[:]:
			print(i.name + ', '+ i['unit'] + '   $' + str(i['price']))
		print('\n\nTotal Amount due: $' + str(Products.totalAmount))
		print('Total received: $' + str(Products.paymentReceived))
		print('Change given: $' + str(abs(Products.dueAmount)))
		print('\n\n Thank You for shopping at FedUni!')
