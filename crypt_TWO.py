def distinct(*args):
	return len(set(args))==len(args)

for t in range(0,10):
	for w in range(0,10):
		for o in range(0,10):
			for f in range(1,10):
				for u in range(0,10):
					for r in range(0,10):
						if distinct(t,w,o,f,u,r):
							two=100*t+10*w+o
							four=1000*f+100*o+10*u+r
							if two+two==four:
								print(two,"+",two,"=",four)
								
