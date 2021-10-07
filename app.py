import time
import os
from colorama import Fore, Back, Style
class CreditCard:
	def __init__(self, card_no):
		self.card_no =card_no.strip()
		self.checksum_size =0;
		self.cardlen =len(self.card_no)

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
		if 13 <= self.cardlen <=19:
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
		return int(self.card_no[-self.checksum_size:])

def clrscn():
	if os.name =='posix': # mac, linux
		_=os.system('clear')

	else: # windows
		_=os.system('cls')

if __name__ == '__main__':
	clrscn() 
	print(Fore.GREEN+"[+] Enter card number: ", end ='')
	card_no =input()
	crc =CreditCard.set_card(card_no)
	clrscn()
	print(Fore.GREEN+"[+] Determining your input ...")

	time.sleep(1)
	print(Fore.YELLOW+"==========RESULTS==========")
	print("\n")
	time.sleep(1)
	vendor =crc.get_vendor
	print(f"{Fore.GREEN}[+] ccn: {crc.card_no}") # credit card number -ccn
	time.sleep(1)
	if crc.check_sum() >0: # card checksum -ccs
		print(f"{Fore.GREEN}[+] ccs: {crc.check_sum()}") 
	else:
		print(f"{Fore.RED}[-] ccs: fail")
	time.sleep(1)
	if vendor: # card vendor check -cvc
		print(Fore.GREEN+"[+] cvc: pass")

	else:
		print(Fore.RED+"[-] cvc: fail")

	time.sleep(1)
	len_test =crc.card_len()
	if len_test =='L201': # card length check -clc
		print(Fore.GREEN+"[+] clc: pass")
	else:
		print(Fore.RED+"[-] clc: fail")

	time.sleep(1)
	isvalid =crc.validate()
	if isvalid: # card boolean check -cbc
		print(Fore.GREEN+"[+] cbc: pass")
	else:
		print(Fore.RED+"[-] cbc: fail")
	print(Style.RESET_ALL)