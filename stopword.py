import io
from nltk.corpus import stopwords

sw=set(stopwords.words("english"))
print(sw)

file=open("bgs1.text")
line=file.read()
for w in line.split():
	if not w in sw:
		f1=open("output.text","a")
		f1.write(" "+w)
		f1.close()



