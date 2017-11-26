from random import randint

class Brick:
	def makeBrick(self,arr,perm):
		x = randint(1,31)
		y = randint(1,15)
		if (perm[y][x]==0 and not(x==1 and y==1)):
			arr[2*y+2][4*x+2]='/'
			arr[2*y+2][4*x+3]='/'
			arr[2*y+2][4*x+4]='/'
			arr[2*y+2][4*x+5]='/'
			arr[2*y+3][4*x+2]='/'
			arr[2*y+3][4*x+3]='/'
			arr[2*y+3][4*x+4]='/'
			arr[2*y+3][4*x+5]='/'
			perm[y][x]=2
			return 1
		return 0

	

