def Perfect(numb):
	if numb <= 0: 
		print('Enter a natural number:')
		return False
	
	divis = []
	for i in range(numb,0,-1):
		if numb%i==0: divis.append(i)
	if numb*2==sum(divis): return True
	else: return False
		
p = int(input('Enter a number: '))
if(Perfect(p)):
    print('Perfect')
else:
    print('Not Perfect')
