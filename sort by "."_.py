p=input("enter multiple sentence with every sentence terminated by.=>")
l=[]
for i in p.split("."):
	i=i.lower()
	l.append(i)
l.sort()
print("sentence in alphabetical order=>")
for w in l:
	print(w)
