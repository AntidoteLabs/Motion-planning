from random import randint
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt

max_x = 10
max_y = 10
min_x = 0
min_y = 0

image = np.zeros(shape=(10, 10))
x = randint(0, 9)
y = randint(0, 9)
image[x, y] = 1

start_x = x
start_y = y
x = randint(0, 9)
y = randint(0, 9)
image[x, y] = 3

goal_x = x
goal_y = y

obstacles_x = []
obstacles_y  = []
obstacles = 10*2

for i in range(obstacles):
    flag = False
    while flag == False:
        x = randint(0, 9)
        y = randint(0, 9)
        if image[x, y]==0:
            flag = True
            image[x, y] = 4
            obstacles_x.append(x)
            obstacles_y.append(y)

#plt.imshow(image, interpolation='nearest')
#plt.show()
#scipy.misc.toimage(image, cmin=0.0).save('image.jpg')

print (start_y,start_x)
print (goal_x,goal_y)

#for i in range(0,10*2):
#	print (obstacles_x[i],obstacles_y[i])


final_path_x = []
final_path_y = []

vis = np.zeros(shape=(10,10))
def dfs(x,y,X,Y):
	print (x,y,X,Y)
	if x<0 or x>=max_x or y<0 or y>=max_y:
		return -1,-1,0
	if vis[x][y]!=0.0:
		return -1,-1,0
	else:
		vis[x][y]=1
		if x==X and y==Y:
			return x,y,1
		else:
			dx,dy,flag=dfs(x+1,y,X,Y)
			if dx!=-1 and dy!=-1 and flag==1:
				final_path_y.append(dy)
				final_path_x.append(dx)
				return x+1,y,1
			dx,dy,flag=dfs(x-1,y,X,Y)
			if dx!=-1 and dy!=-1 and flag==1:
				final_path_y.append(dy)
				final_path_x.append(dx)
				return x-1,y,1
			dx,dy,flag=dfs(x,y-1,X,Y)
			if dx!=-1 and dy!=-1 and flag==1:
				final_path_y.append(dy)
				final_path_x.append(dx)
				return x,y-1,1
			dx,dy,flag=dfs(x,y+1,X,Y)

			if dx!=-1 and dy!=-1 and flag==1:
				final_path_y.append(dy)
				final_path_x.append(dx)
				return x,y+1,flag
			





dx,dy,flag = dfs(start_x,start_y,goal_x,goal_y)

final_path_x.append(dx)
final_path_y.append(dy)

if dx!=-1 and dy!=-1 and flag==1:
	for i in range(0,len(final_path_y)):
		image[final_path_x[i],final_path_y[i]]=6
	image[start_x,start_y]=1
	image[goal_x,goal_y]=3
	plt.imshow(image, interpolation='nearest')
	plt.show()

else:
	print ("Path doesn't exits")
	print(final_path_x,final_path_y)
	plt.imshow(image, interpolation='nearest')
	plt.show()
