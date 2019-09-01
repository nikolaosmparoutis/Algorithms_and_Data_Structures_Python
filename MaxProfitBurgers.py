
t = 3
p = 7
b = 5
f = 2
h = 10
c = 12

profit = 0

def max_profit(t, p, b, f, h, c, profit):

	num_p=p//2 # num of 2-patty pieces
	if t<1 or t>100 or num_p <1 or b<1 or f<1 or b>100 or f>100:
		return 0 

	while (t>0 and num_p > 0 and (b+f)>0): # run while queries exists and ingredients # positive > 0
		if h>c and b > 0: # price of  meat > chicken sell all the meat first if enough bread exist 
			if num_p >= b: #if breads pieces >  meat pieces, sell all the meat  
				t -= 1
				num_p -= b	
				profit += b*h
				b = 0
			else:	#if bread pieces <  meat pieces sell all the bread with only meat (zero the breads),exist
				t -= 1
				num_p = 0		
				profit += b*h
				b -= num_p
				break
		if c > h and f > 0: # the same fprocess with chicken condition
			if num_p >= f:
				t -= 1
				num_p -= f	
				profit += f*c
				f = 0
			else:
				t -= 1
				num_p = 0		
				profit += f*c
				f -= num_p	
				break
		if c == h and p > f and p > 0: # same price for beef and chicken, sell the most pieces first 
			if num_p >= b:
				t -= 1
				num_p -= b	
				profit += b*h
				b = 0
			else:
				t -= 1
				num_p = 0		
				profit += b*h
				b -= num_p
				break
		if c == h and f > p and f > 0:
			if num_p >= f:
				t -= 1
				num_p -= f	
				profit += f*c
				f = 0
			else:
				t -= 1
				num_p = 0		
				profit += f*c
				f -= num_p	
				break
	return (profit)	
		
max_prof = max_profit(t,p,b,f,h,c,profit)
print('Max profit = {}' .format(max_prof))
			
			