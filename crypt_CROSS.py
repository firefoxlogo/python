def distinct(*args):
	return len(set(args))==len(args)
for c in range(0,10):
	for r in range(0,10):
		for o in range(0,10):
			for s in range(0,10):
				for a in range(0,10):
					for d in range(1,10):
						for n in range(0,10):
							for g in range(0,10):
								for e in range(0,10):
									if distinct(c,r,o,s,a,d,n,g,e):
										cross=10000*c+1000*r+100*o+10*s+s
										roads=10000*r+1000*o+100*a+10*d+s
										danger=100000*d+10000*a+1000*n+100*g+10*e+r
										if cross+roads==danger:
											print(cross,"+",roads,"=",danger)
