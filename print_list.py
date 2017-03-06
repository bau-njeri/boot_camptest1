def prime_numbers(j,i,n,op):

	for x in range(0,n):
		if x<=0 or x==1:
			for i in range(2,x):
				pass
		elif i%x==0 and x%x==0 and x%1==0:
			print (x)

	prime_numbers()		
