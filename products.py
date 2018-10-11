class Products:
	items = {
		123: {'name': 'milk', 'unit': '1 litre', 'price': 1, 'weight': 1},
		234: {'name': 'bread', 'unit': '1 packet', 'price': 3.5, 'weight': 1},
		345: {'name': 'oil', 'unit': '1 litre', 'price': 6, 'weight': 1},
        456: {'name': 'butter', 'unit': '1 packet', 'price': 10, 'weight': 1},
        789: {'name': 'buttermilk', 'unit': '1 litre', 'price': 0.5, 'weight': 1},
		910: {'name': 'rusk', 'unit': '1 packet', 'price': 4, 'weight': 1},
		870: {'name': 'cockies', 'unit': '1 packet', 'price': 2, 'weight': 1},
		357: {'name': 'tea-leaves', 'unit': '1 packet', 'price': 2.75, 'weight': 1},
		753: {'name': 'coffee', 'unit': '1 packet', 'price': 5, 'weight': 1},
		957: {'name': 'candy', 'unit': '1 packet', 'price': 2.75, 'weight': 1},
	}
	totalProducts = []
	totalAmount = 0.0
	paymentReceived = 0.0
	dueAmount = 0.0
