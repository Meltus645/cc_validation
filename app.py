class CreditCard:
	def __init__(self, card_no):
		self.card_no =card_no

	@classmethod
	def set_card(self, card):
		return self(card)

	@property
	def get_vendor(self):
		vendor =None
		crn =str(self.card_no)
		if crn.startswith('4'):
			vendor ='Visa Card' 
		elif crn.startswith(('50', '67', '58', '63')):
			vendor ='Maestro Card'
		elif crn.startswith('5'):
			vendor ='Master Card'
		elif crn.startswith('37'):
			vendor ='American Express'
		elif crn.startswith('68'):
			vendor ='UnionPay Card'
		elif crn.startswith('7'):
			vendor ='Gasoline Card'

		return vendor
	
if __name__ == '__main__':
	print("[+] Enter card number: ", end ='')
	card_no =int(input())
	ccv =CreditCard(card_no)
	vendor =ccv.get_vendor()
	print(f"[+] Card Number: {card_no}")
	if vendor:
		print(f"[+] Card Vendor: {vendor}")

	else:
		print(f"[-] Unknown card vendor!")