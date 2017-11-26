import os
import sys
from person import Person

class Player(Person):
	def __init__(self):
		Person.__init__(self)
		self.x = 1
		self.y = 1
		self.lifes = 3
		self.score = 0
		self.bombdropped = 0

	def spawnBomberman(self,arr,perm):
		arr[2*self.y+2][4*self.x+2]='B'
		arr[2*self.y+2][4*self.x+3]='B'
		arr[2*self.y+2][4*self.x+4]='B'
		arr[2*self.y+2][4*self.x+5]='B'
		arr[2*self.y+3][4*self.x+2]='B'
		arr[2*self.y+3][4*self.x+3]='B'
		arr[2*self.y+3][4*self.x+4]='B'
		arr[2*self.y+3][4*self.x+5]='B'

	def clearMan(self,arr,perm):
		arr[2*self.y+2][4*self.x+2]=' '
		arr[2*self.y+2][4*self.x+3]=' '
		arr[2*self.y+2][4*self.x+4]=' '
		arr[2*self.y+2][4*self.x+5]=' '
		arr[2*self.y+3][4*self.x+2]=' '
		arr[2*self.y+3][4*self.x+3]=' '
		arr[2*self.y+3][4*self.x+4]=' '
		arr[2*self.y+3][4*self.x+5]=' '

	def moveRight(self,arr,perm):
		self.clearMan(arr,perm)
		if self.x<31 and perm[self.y][self.x+1]==0:
			self.x+=1
			self.spawnBomberman(arr,perm)
			return 1
		self.spawnBomberman(arr,perm)
		return 0
		
	def moveUp(self,arr,perm):
		self.clearMan(arr,perm)
		if self.y>1 and perm[self.y-1][self.x]==0:
			self.y-=1
			self.spawnBomberman(arr,perm)
			return 1
		self.spawnBomberman(arr,perm)
		return 0

	def moveLeft(self,arr,perm):
		self.clearMan(arr,perm)
		if self.x>1 and perm[self.y][self.x-1]==0:
			self.x-=1
			self.spawnBomberman(arr,perm)
			return 1
		self.spawnBomberman(arr,perm)
		return 0

	def moveDown(self,arr,perm):
		self.clearMan(arr,perm)
		if self.y<15 and perm[self.y+1][self.x]==0:
			self.y+=1
			self.spawnBomberman(arr,perm)
			return 1
		self.spawnBomberman(arr,perm)
		return 0



