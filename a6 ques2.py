def Palin(phr):	
	list1 = list(''.join(phr.split()))
	if list1 == list(reversed(list1)):	#can use [::-1] as well, however reversed faster
		return True 
	else:
		return False
	
	
	
input1 = input('Enter a Phrase: ')
if Palin(input1):
	print("This is a palindrome. ")
	
else: 
	print('This is not.')
	
