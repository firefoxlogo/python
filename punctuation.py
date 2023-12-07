s=input("enter sentence with punctuation marks=>")
pm="~`!@#$%$^&*()_-+={}[]:;\"'<>,.?/"
us=""
for i in s:
	if not i in pm:
		us=us+i
print("sentence without punctuation marks=>")
print(us)
		
