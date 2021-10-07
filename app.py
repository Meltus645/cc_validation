import time
import os
import sys
from colorama import Fore, Back, Style,init
import random
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
def progress(curr):
	step =random.randint(0, 5)
	if curr + step >100:
		step =0
	return step

if __name__ == '__main__':
	init()
	clrscn() 
	print(Fore.GREEN+"[+] Enter card number: ", end ='')
	card_no =input()
	crc =CreditCard.set_card(card_no)
	clrscn()
	print(Fore.GREEN+"[+] Determining your input ...")
	if crc.cardlen <=0:
		print(Fore.RED+"[-] Input not found")
		time.sleep(1)
		print(Fore.RED+"[-] Closing ...")
		print(Style.RESET_ALL)
		time.sleep(1)
		sys.exit(0)
	time.sleep(1)
	clrscn()
	i =0
	while i<100:
		sys.stdout.write(f"\r[+] Validating Card.... {i}% Complete")
		sys.stdout.flush()
		i =i+progress(i)
		time.sleep(33/99)
	clrscn()
	time.sleep(33/99)
	print(Fore.GREEN+"[+] Complete")
	time.sleep(1)
	clrscn()
	print(Fore.GREEN+"[+] Generating Report")
	time.sleep(2)
	clrscn()
	print(Fore.YELLOW+"==========Validation Report==========")
	print("\n")
	time.sleep(1)
	vendor =crc.get_vendor
	print(f"{Fore.GREEN}[+] Credit Number: {crc.card_no}") # credit card number -ccn
	time.sleep(1)
	if vendor: # card vendor check -cvc
		print(f"{Fore.GREEN}[+] Vendor check: Pass - {vendor}")

	else:
		print(f"{Fore.RED}[-] Vendor check: Fail -Unknown")
	time.sleep(1)
	if crc.check_sum() >0: # card checksum -ccs
		print(f"{Fore.GREEN}[+] Checksum check: Pass - {crc.check_sum()}") 
	else:
		print(f"{Fore.RED}[-] Checksum check: Fail - Unknown")
	time.sleep(1)
	len_test =crc.card_len()
	if len_test =='L201': # card length check -clc
		print(f"{Fore.GREEN}[+] Size Check: Pass - {len(crc.card_no)} digits")
	else:
		print(f"{Fore.RED}[-] clc: Fail - {len(crc.card_no)} digits")

	time.sleep(1)
	isvalid =crc.validate()
	if isvalid: # card boolean check -cbc
		print(Fore.GREEN+"[+] Algo Check: Pass - Valid Card")
	else:
		print(Fore.RED+"[-] Algo Check: Fail - Invalid Card")
	print(Style.RESET_ALL)