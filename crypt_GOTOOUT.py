def distinct(*args):
	return len(set(args))==len(args)

for o in range(0,10):
	for t in range(0,10):
		for g in range(0,10):
			for u in range(0,10):
				if distinct(g,o,t,u):
					go=10*g+o
					to=10*t+o
					out=100*o+10*u+t
					if go+to==out:
						print("g=",g)
						print("o=",o)
						print("t=",t)
						print("u=",u)
						print(go,"+",to,"=",out)

	
