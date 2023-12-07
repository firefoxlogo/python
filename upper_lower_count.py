s=input("Enter string with lower and upper case letter=>")
l=0
u=0
for i in s:
	if i.islower():
		l=l+1
	if i.isupper():
		u=u+1
print("No of lower case=>",l)
print("No of upper case=>",u)
