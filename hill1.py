import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return (-x)**3
	
input1=np.arange(-5.0,5.0,0.1)
result=[]
for i in input1:
	result.append(f(i))
print("max result={}".format(max(result)))
plt.plot(input1,result)
xmin=0.0
plt.axvline(x=xmin,ls="--",color="red")
plt.show()

