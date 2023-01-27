def Pascal(n):
	numb = [[1]]
	if n<=0: print("Enter a valid value")
	elif n==1: print(numb[0][0])
	elif n>1:
		for i in range(1,n):
			rows=[]
			for j in range(i+1):
				if j==0 or j==i: rows.append(1)
				else: rows.append(numb[i-1][j-1] + numb[i-1][j])
			
			numb.append(rows)
			'''
			space = n-i - 1
			for j in range(space): print(' ', end = '')
			for j in rows: print(j, end = ' ')
			print()
			'''
			#this code doesnt works for double digit or greater ints, so have to create another loop
		last_rows = ' '.join(map(str,numb[n-1]))
		max_chr = len(last_rows)
		for i in numb:
			chrs = ' '.join(map(str,i))
			space = (max_chr - len(chrs))//2
			for j in range(space): print(' ', end = '')
			for j in i: print(j, end = ' ')
			print()	
		
		
	
Pascal(int(input('Enter number of rows: ')))
