class CreditCard:
	def __init__(self, card_no):
		self.card_no =card_no
		self.checksum_size =0;

	@classmethod
	def set_card(self, card):
		return self(str(card))

	@property
	def get_vendor(self):
		vendor =None
		crn =self.card_no
		if crn.startswith('4'):
			vendor ='Visa Card'
			self.checksum_size =3 
		elif crn.startswith(('50', '67', '58', '63')):
			vendor ='Maestro Card'
			self.checksum_size =2
		elif crn.startswith('5'):
			vendor ='Master Card'
			self.checksum_size =4
		elif crn.startswith('37'):
			vendor ='American Express'
			self.checksum_size =3
		elif crn.startswith('68'):
			vendor ='UnionPay Card'
			self.checksum_size = 2
		elif crn.startswith('7'):
			vendor ='Gasoline Card'
			self.checksum_size =4

		return vendor

	def card_len(self):
		flag ='L101'
		if 13 <= int(self.card_no) <=19:
			flag ='L201'
		return flag

	def validate(self):
		isvalid =False
		sum_ =0
		ccno =self.card_no[::-1] # 1. reverse card_no elements and store in ccno
		for i in range(len(ccno)): 
			if i %2 ==1:
				ix2 =int(ccno[i])*2 # 2. double every second number of ccno
				if len(str(ix2)) ==2: # check if ix2 gives a 2-digit number
					sum_ +=sum([int(x) for x in str(ix2)]) # if true add the digits, list comprehension used
				else:
					sum_ +=ix2
		if sum_ %10 ==0:
			isvalid =True
		return isvalid
	def check_sum(self):
		return self.card_no[-self.checksum_size:]
if __name__ == '__main__': 
	print("[+] Enter card number: ", end ='')
	card_no =input()
	crc =CreditCard.set_card(card_no)
	vendor =crc.get_vendor
	print(f"[+] ccn: {crc.card_no}") # credit card number -ccn
	print(f"[+] ccs: {crc.check_sum()}") # card checksum -ccs
	if vendor: # card vendor check -cvc
		print("[+] cvc: pass")

	else:
		print("[-] cvc: fail")

	len_test =crc.card_len()
	if len_test =='L201': # card length check -clc
		print("[+] clc: pass")
	else:
		print("[-] clc: fail")

	isvalid =crc.validate()
	if isvalid: # card boolean check -cbc
		print("[+] cbc: pass")
	else:
		print("[-] cbc: fail")