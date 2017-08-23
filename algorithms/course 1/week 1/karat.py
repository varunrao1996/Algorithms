def karat(x,y):
	if len(str(x)) == 1 or len(str(y)) == 1:
		return x*y
	else:
		n = max(len(str(x)),len(str(y)))
		half = n/2
		a = x / 10**(half)
		b = x % 10**(half)
		c = y / 10**(half)
		d = y % 10**(half)
		ac = karat(a,c)
		bd = karat(b,d)
		sop = karat(a+b,c+d) - ac - bd
		prod = ac * 10**(2*half) + (sop * 10**half) + bd
		return prod

if __name__=="__main__":

	x=input("Enter x: ")
	y=input("Enter y: ")
	z=karat(x,y)
	print "The solution is: ",z