import math
def minimax(curdepth,nodeindex,maxturn,scores,maxdepth):
	if curdepth==maxdepth:
		return scores[nodeindex]
	if maxturn:
		return max(minimax(curdepth+1,nodeindex*2,False,scores,maxdepth),	minimax(curdepth+1,nodeindex*2+1,False,scores,maxdepth))
	else:
		return min(minimax(curdepth+1,nodeindex*2,True,scores,maxdepth),minimax(curdepth+1,nodeindex*2+1,True,scores,maxdepth))
scores=[2,8,6,-5,3,2,-1,7]
depth=math.log(len(scores),2)
print("value of game=>",minimax(0,0,False,scores,depth))
