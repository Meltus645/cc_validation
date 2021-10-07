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

	def card_len(self):
		flag ='L101'
		if 13 <= self.card_no <=19:
			flag ='L201'
		return flag
	
if __name__ == '__main__':
	print("[+] Enter card number: ", end ='')
	card_no =int(input())
	crc =CreditCard.set_card(card_no)
	vendor =crc.get_vendor
	print(f"[+] ccn: {crc.card_no}") # credit card number -ccn
	if vendor: # card vendor check -cvc
		print("[+] cvc: pass")

	else:
		print("[-] cvc: fail")

	len_test =crc.card_len()
	if len_test =='L201': # card length check -clc
		print("[+] clc: pass")
	else:
		print("[-] clc: fail")