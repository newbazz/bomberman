import sys
import os
from person import Person

class Enemy(Person):
	def __init__(self,x,y):
		Person.__init__(self)
		self.x = x
		self.y = y
		self.typ=0
		self.movement=1

	def spawnEnemy(self,arr,perm):
		perm[self.y][self.x]=3
		arr[2*self.y+2][4*self.x+2]='E'
		arr[2*self.y+2][4*self.x+3]='E'
		arr[2*self.y+2][4*self.x+4]='E'
		arr[2*self.y+2][4*self.x+5]='E'
		arr[2*self.y+3][4*self.x+2]='E'
		arr[2*self.y+3][4*self.x+3]='E'
		arr[2*self.y+3][4*self.x+4]='E'
		arr[2*self.y+3][4*self.x+5]='E'

	def clearEnemy(self,arr,perm):
		perm[self.y][self.x]=0
		arr[2*self.y+2][4*self.x+2]=' '
		arr[2*self.y+2][4*self.x+3]=' '
		arr[2*self.y+2][4*self.x+4]=' '
		arr[2*self.y+2][4*self.x+5]=' '
		arr[2*self.y+3][4*self.x+2]=' '
		arr[2*self.y+3][4*self.x+3]=' '
		arr[2*self.y+3][4*self.x+4]=' '
		arr[2*self.y+3][4*self.x+5]=' '

	def moveRight(self,arr,perm):
		self.clearEnemy(arr,perm)
		if self.x<31 and (perm[self.y][self.x+1]==0 or perm[self.y][self.x+1]==3):
			self.x+=1
			self.spawnEnemy(arr,perm)
			return 1
		self.spawnEnemy(arr,perm)
		return 0
		
	def moveUp(self,arr,perm):
		self.clearEnemy(arr,perm)
		if self.y>1 and (perm[self.y-1][self.x]==0 or perm[self.y-1][self.x]==3):
			self.y-=1
			self.spawnEnemy(arr,perm)
			return 1
		self.spawnEnemy(arr,perm)
		return 0

	def moveLeft(self,arr,perm):
		self.clearEnemy(arr,perm)
		if self.x>1 and (perm[self.y][self.x-1]==0 or perm[self.y][self.x-1]==3):
			self.x-=1
			self.spawnEnemy(arr,perm)
			return 1
		self.spawnEnemy(arr,perm)
		return 0

	def moveDown(self,arr,perm):
		self.clearEnemy(arr,perm)
		if self.y<15 and (perm[self.y+1][self.x]==0 or perm[self.y+1][self.x]==3):
			self.y+=1
			self.spawnEnemy(arr,perm)
			return 1
		self.spawnEnemy(arr,perm)
		return 0



