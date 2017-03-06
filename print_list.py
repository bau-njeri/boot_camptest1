def prime_numbers(N):

	for x in range(0,50):
		if x<=0 or x==1:
			for i in range(2,x):
				pass
		elif x%N==0 and x%x==0 and x%1==0:
			print (x)

	prime_numbers(7)		
