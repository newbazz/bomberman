import os
import sys

class Bomb:
	def __init__(self,bomberman):
		if bomberman.bombdropped == 0:
			self.x = bomberman.x
			self.y = bomberman.y
			self.time = 3
			self.show = 0
			bomberman.bombdropped = 1
		else:
			return None
	
	def bombShow(self,arr,perm):
		self.show = 1
		arr[2*self.y+2][4*self.x+2]='O'
		arr[2*self.y+2][4*self.x+3]='O'
		arr[2*self.y+2][4*self.x+4]='O'
		arr[2*self.y+2][4*self.x+5]='O'
		arr[2*self.y+3][4*self.x+2]='O'
		arr[2*self.y+3][4*self.x+3]='O'
		arr[2*self.y+3][4*self.x+4]='O'
		arr[2*self.y+3][4*self.x+5]='O'
		perm[self.y][self.x] = 1

	def explode(self,arr,bomberman):
		self.show = 0
		bomberman.bombdropped = 0	
		arr[2*self.y+2][4*self.x+2]=' '
		arr[2*self.y+2][4*self.x+3]=' '
		arr[2*self.y+2][4*self.x+4]=' '
		arr[2*self.y+2][4*self.x+5]=' '
		arr[2*self.y+3][4*self.x+2]=' '
		arr[2*self.y+3][4*self.x+3]=' '
		arr[2*self.y+3][4*self.x+4]=' '
		arr[2*self.y+3][4*self.x+5]=' '

	def makeE(self,arr,x,y):
		arr[2*y+2][4*x+2]='e'
		arr[2*y+2][4*x+3]='e'
		arr[2*y+2][4*x+4]='e'
		arr[2*y+2][4*x+5]='e'
		arr[2*y+3][4*x+2]='e'
		arr[2*y+3][4*x+3]='e'
		arr[2*y+3][4*x+4]='e'
		arr[2*y+3][4*x+5]='e'

	def removeE(self,arr,x,y):
		arr[2*y+2][4*x+2]=' '
		arr[2*y+2][4*x+3]=' '
		arr[2*y+2][4*x+4]=' '
		arr[2*y+2][4*x+5]=' '
		arr[2*y+3][4*x+2]=' '
		arr[2*y+3][4*x+3]=' '
		arr[2*y+3][4*x+4]=' '
		arr[2*y+3][4*x+5]=' '


	def fire(self,arr,perm,bomberman,en,level):
		x,y = self.x,self.y
		perm[y][x]=0
		if((bomberman.x==self.x and bomberman.y==self.y) or (bomberman.x==self.x+1 and bomberman.y==self.y) or (bomberman.x==self.x and bomberman.y==self.y+1) or (bomberman.x==self.x-1 and bomberman.y==self.y) or (bomberman.x==self.x and bomberman.y==self.y-1)):
			bomberman.lifes-=1
			if(bomberman.lifes>0):
				bomberman.x = 1
				bomberman.y = 1
				bomberman.spawnBomberman(arr,perm)
			elif(bomberman.lifes==0):
				return 0
		

		self.makeE(arr,x,y)

		x,y = self.x+1,self.y
		if self.x<31 and (perm[self.y][self.x+1]==2 or perm[self.y][self.x+1]==0 or perm[self.y][self.x+1]==3):
			if(perm[self.y][self.x+1]==2):
				bomberman.score+=20
			if(perm[self.y][self.x+1]==3):
				print('awsd')
				bomberman.score+=100
			self.makeE(arr,x,y)
			perm[self.y][self.x+1]=0

		x,y = self.x,self.y+1
		if self.y<15 and (perm[self.y+1][self.x]==2 or perm[self.y+1][self.x]==0 or perm[self.y+1][self.x]==3):
			if(perm[self.y+1][self.x]==2):
				bomberman.score+=20
			if(perm[self.y+1][self.x]==3):
				print('awsd')
				bomberman.score+=100
			self.makeE(arr,x,y)
			perm[self.y+1][self.x]=0

		x,y = self.x-1,self.y
		if self.x>1 and (perm[self.y][self.x-1]==2 or perm[self.y][self.x-1]==0 or perm[self.y][self.x-1]==3):
			if(perm[self.y][self.x-1]==2):
				bomberman.score+=20
			if(perm[self.y][self.x-1]==3):
				print('awsd')
				bomberman.score+=100
			self.makeE(arr,x,y)
			perm[self.y][self.x-1]=0

		x,y = self.x,self.y-1
		if self.y>1 and (perm[self.y-1][self.x]==2 or perm[self.y-1][self.x]==0 or perm[self.y-1][self.x]==3):
			if(perm[self.y-1][self.x]==2):
				bomberman.score+=20
			if(perm[self.y-1][self.x]==3):
				print('awsd')
				bomberman.score+=100
			self.makeE(arr,x,y)
			perm[self.y-1][self.x]=0

		for i in range(2*level+3):
			if(en[i]!=None and ((en[i].x==self.x and en[i].y==self.y) or (en[i].x==self.x+1 and en[i].y==self.y) or (en[i].x==self.x and en[i].y==self.y+1) or (en[i].x==self.x-1 and en[i].y==self.y) or (en[i].x==self.x and en[i].y==self.y-1))):
				perm[en[i].y][en[i].x]=0
				en[i].living = 0
#		en[i].clearEnemy(arr,perm)
				en[i]=None
		return 1

	def remove(self,arr,perm,bomberman):
		x,y = self.x,self.y
		self.removeE(arr,x,y)

		x,y = self.x+1,self.y
		if self.x<31 and (perm[self.y][self.x+1]==2 or perm[self.y][self.x+1]==0):
			self.removeE(arr,x,y)
			perm[self.y][self.x+1]=0

		x,y = self.x,self.y+1
		if self.y<15 and (perm[self.y+1][self.x]==2 or perm[self.y+1][self.x]==0):
			self.removeE(arr,x,y)
			perm[self.y+1][self.x]=0

		x,y = self.x-1,self.y
		if self.x>1 and (perm[self.y][self.x-1]==2 or perm[self.y][self.x-1]==0):
			self.removeE(arr,x,y)
			perm[self.y][self.x-1]=0

		x,y = self.x,self.y-1
		if self.y>1 and (perm[self.y-1][self.x]==2 or perm[self.y-1][self.x]==0):
			self.removeE(arr,x,y)
			perm[self.y-1][self.x]=0


