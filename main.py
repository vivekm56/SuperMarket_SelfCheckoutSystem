from checkoutregister import CheckoutRegister
from products import Products


def handle_interaction():
	barCode = CheckoutRegister().currentBarCode
	scannedData = CheckoutRegister.scan_item(barCode)
	print(scannedData['message'])
	if('item' in scannedData):
		Products.totalProducts.append(scannedData['item'])
	needMoreProduct = input('Would you like to scan another product (Y/N) ')
	if(needMoreProduct == 'y'):
		handle_interaction()



#bag_products function.
def bag_products(product_list):
  bag_list = []
  non_bagged_items = []
  #initialize maximum weight that a bag carry.
  MAX_BAG_WEIGHT = 5.0
  # To search the Weight of each item into product list.
  for product in product_list:
	#To add item into items_without_bag from item list if total purchased weight> maximum weight.
    if product['weight'] > MAX_BAG_WEIGHT:
      product_list.remove(product)
      non_bagged_items.append(product)
  #initialized list current_bag_contents.
  current_bag_contents = []
  #initialized the current_bag_weight variable to 0.0.
  current_bag_weight = 0.0
  #repeat the loop till item list length.
  while len(product_list) > 0:
    #initialize products into product_list.
    temp_product = product_list[0]

    product_list.remove(temp_product)
	#check current_bag_weight is less than to maximum bag weight.
    if current_bag_weight + temp_product['weight'] <= MAX_BAG_WEIGHT:
      #if total purchased item weight is less than to maximum weight than append it to current_bag_contents list.
      current_bag_contents.append(temp_product)
      current_bag_weight += temp_product['weight']

      if (len(product_list) == 0):
        bag_list.append(current_bag_contents)

    else:
      bag_list.append(current_bag_contents)
      # here current bag contains products from barcode which taken by user.
      current_bag_contents = []
      current_bag_weight = 0.0

 # assign numbers to bag.
  for index, bag in enumerate(bag_list):
    output = 'Bag ' + str(index + 1) + ' contains: '
    # to print bag items output
    for product in bag:
      output += product['name'] + '\t'
    print(output, '\n')

  # to print non_bagged_items.
  if (len(non_bagged_items) > 0):
    output = 'Non-bagged items: '
    # contains non bag item list.
    for item in non_bagged_items:
        output += item + '\t'
    print(output,'\n')



#get_float function.
def get_float(prompt):
	#initialize value of value variable.
    value = float(0.0)
	#check the condition of variable.
    while True:
        try:
			#take input from user in float type.
            value = float(input(prompt))
			#check user input
            if value < 0.0:
                print("We don't accept negative money!")
                continue
			# break loop with above mention message.
            break
		# if user input is not in float type.
        except ValueError:
            print('Please enter a valid floating point value.')
	#return to value and start loop again.
    return value

def main():
	handle_interaction()
	bag_products(Products.totalProducts)
	while(Products.dueAmount > 0):
		#print('Payment due: $'+ str(Products.dueAmount) )
		receivedAmount = get_float("\nPayment due: " + str(Products.dueAmount) + ". Please enter an amount to pay: ")
		CheckoutRegister.accept_payment(int(receivedAmount))
		CheckoutRegister.print_receipt()

	processNext = input("(N)ext customer, or (Q)uit?(N/Q):")
	if processNext == "N":
                main()


if __name__ == '__main__':
	print('---------------------Welcome to FedUni Checkout!------------------------')
	main()
