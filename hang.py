name=input("enter your name=>")
print("wel come {} for hangman game!!!".format(name))
word="sunday"
count=0
attempt=len(word)+3
fail=0
guess=""
while count<attempt and fail==0:
	for i in word:
		if i in guess:
			print(i,end=" ")
		else:
			print("_",end=" ")
	print("Enter your character=>")
	c=input("")
	count=count+1
	guess=guess+c
	solve=0
	for i in word:
		if i in guess:
			solve=solve+1
	if(solve==len(word)):
		fail=1
if (fail==1):
	for i in word:
		if i in guess:
			print(i,end=" ")
		else:
			print("_",end=" ")

	print("you won ",name)
else:
	print("Better luck next time", name)
	
	
		
