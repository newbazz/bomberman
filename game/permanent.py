import sys
import os

class Wall:
	def makeWall(self,arr):
		for i in range(1,37):
			for j in range(1,135):
				if (i == 1 or i == 2 or i == 3 or j == 1 or j == 2 or j == 3 or j == 4 or j == 5 or j == 134 or i == 34 or i == 36 or i == 35 or j== 133 or j == 130 or j == 131 or j == 132):
					arr[i][j] = '#'

				else:
					arr[i][j] = ' '
	
	def makeInterior(self,arr,perm):
		for i in range(6,34):
			k = i - 5
			for j in range(10,130):
				l = j - 9
				if (((l%8==1) or (l%8==2) or (l%8==3) or (l%8==4)) and ((k%4==1) or (k%4==2))):
					arr[i][j] = 'X'
				if l%8==1 and k%4==1:
					perm[int((i-2)/2)][int((j-2)/4)]=1
	
	
