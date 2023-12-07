
def toh(n,s,d,t):
	if n==1:
		print("Move plate 1 from source",s,"to destion ",d)
		return
	toh(n-1,s,t,d)
	print("Move plate", n, "from source",s,"to destination ",d)
	toh(n-1,t,d,s)

n=int(input("Number of plates=>"))
toh(n,"A","B","C")
