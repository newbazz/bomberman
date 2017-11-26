from multiprocessing import Process
import sys, tty, termios
import threading
import _thread
import queue
import os
import sys
import getch
import time
import random
from player import Player
from bricks import Brick
from bomb import Bomb
from enemy import Enemy
from permanent import Wall

print('\x1b[8;50;170t')
level=1
checklevel=1

while(level<=3):
	
	arr = [['' for x in range(135)] for y in range(135)] 
	perm = [[0 for i in range(1,33)] for j in range(1,17)]
	wl = Wall()
	wl.makeWall(arr)
	wl.makeInterior(arr,perm)
	bombOn = 0
	moves=0
	bm = None
	enemy = [None for x in range(2*level+3)]

	def brickMaker():
		global level
		i=1
		while i!=15*level+30:
			brck = Brick()
			x = brck.makeBrick(arr,perm)
			if x==1:
				i+=1
			
	
	def printGame():
		global bm
		time.sleep(0.15)
		for i in range(2,36):
			for j in range(1,135):
				if(j!=134):
					if(arr[i][j]=='#'):
						print("\033[1;37;47m"+" "+"\033[0m",end="")
					elif(arr[i][j]=='X'):
						print(arr[i][j],end="")
					elif(arr[i][j]=='B'):
						print("\033[1;32;48m"+arr[i][j]+"\033[0m",end="")
					elif(arr[i][j]=='E'):
						print("\033[1;31;48m"+arr[i][j]+"\033[0m",end="")
					elif(arr[i][j]=='O' or arr[i][j]=='0' or arr[i][j]=='1' or arr[i][j]=='2'):
						print("\033[1;36;48m"+arr[i][j]+"\033[0m",end="")
					elif(arr[i][j]=='e'):
						print("\033[1;33;48m"+arr[i][j]+"\033[0m",end="")
					elif(arr[i][j]=='/'):
						print("\033[1;35;48m"+arr[i][j]+"\033[0m",end="")
					else:
					 	print(arr[i][j],end="")
				else:
					print("\033[1;37;47m"+" "+"\033[0m")
		print('YOUR SCORE: ',end="")
		print(bm.score)
		print('YOUR LIFE: ',end="")
		print(bm.lifes)
	
	bmb=None
	bm=Player()
	bm.spawnBomberman(arr,perm)
	brickMaker()
	r=0
	while r!=2*level+3:
		x = random.randint(1,31)
		y = random.randint(1,15)
		if (perm[y][x]==0 and not(x==1 and y==1)):
			enemy[r]=Enemy(x,y)
			enemy[r].spawnEnemy(arr,perm)
			r+=1
	printGame()

	def moveEnemy():
		global enemy
		global checklevel
		global level
		i=0
		count=0
		enemyremaining=2*level+3
		while i!=2*level+3:
			count+=1
			while(i<2*level+3 and enemy[i]==None):
				if enemy[i]==None:
					enemyremaining-=1
				i+=1
	
			if enemyremaining==0:
				checklevel+=1
	
			if i>=2*level+3:
				break
	
			if(enemy[i].movement==1):
				x = enemy[i].moveLeft(arr,perm)
				if(x==0):
					enemy[i].movement = random.choice([2,3,4])
				else:
					i+=1
			elif(enemy[i].movement==2):
				x = enemy[i].moveUp(arr,perm)
				if(x==0):
					enemy[i].movement = random.choice([1,3,4])
				else:
					i+=1
			elif(enemy[i].movement==3):
				x = enemy[i].moveRight(arr,perm)
				if(x==0):
					enemy[i].movement = random.choice([1,2,4])
				else:
					i+=1
			elif(enemy[i].movement==4):
				x = enemy[i].moveDown(arr,perm)
				if(x==0):
					enemy[i].movement = random.choice([1,2,3])
				else:
					i+=1
	
			if count>=4*2*level+10:
				break
	
	def sideExplode():
		global moves
		global arr
		global perm
		global enemy
		global bm
		global level	
		global bmb
		if(bmb is not None and moves==1):
			arr[2*bmb.y+2][4*bmb.x+2]='2'
			arr[2*bmb.y+2][4*bmb.x+3]='2'
			arr[2*bmb.y+2][4*bmb.x+4]='2'
			arr[2*bmb.y+2][4*bmb.x+5]='2'
			arr[2*bmb.y+3][4*bmb.x+2]='2'
			arr[2*bmb.y+3][4*bmb.x+3]='2'
			arr[2*bmb.y+3][4*bmb.x+4]='2'
			arr[2*bmb.y+3][4*bmb.x+5]='2'
		
		if(bmb is not None and moves==2):
			arr[2*bmb.y+2][4*bmb.x+2]='1'
			arr[2*bmb.y+2][4*bmb.x+3]='1'
			arr[2*bmb.y+2][4*bmb.x+4]='1'
			arr[2*bmb.y+2][4*bmb.x+5]='1'
			arr[2*bmb.y+3][4*bmb.x+2]='1'
			arr[2*bmb.y+3][4*bmb.x+3]='1'
			arr[2*bmb.y+3][4*bmb.x+4]='1'
			arr[2*bmb.y+3][4*bmb.x+5]='1'
	
		if(bmb is not None and moves==3):
			moves=0
			bmb.explode(arr,bm)
			time.sleep(0.2)
			check = bmb.fire(arr,perm,bm,enemy,level)
			printGame()
			time.sleep(0.8)
			bmb.remove(arr,perm,bm)
			bmb=None
			bombOn=0
			if(check==0):
				bm.lifes=0
				printGame()
				sys.exit(0)
	
	while True:
		printGame()
		char = getch.getch()
		rv = 0
		if(char == 'd'):
			rv = bm.moveRight(arr,perm)
			moves+=1
		elif(char == 's'):
			rv = bm.moveDown(arr,perm)
			moves+=1
		elif(char == 'a'):
			rv = bm.moveLeft(arr,perm)
			moves+=1
		elif(char == 'w'):
			rv = bm.moveUp(arr,perm)
			moves+=1
		elif(char == 'b'):
			if bm.bombdropped == 0:
				bmb = Bomb(bm)
				moves = 0
		elif(char == 'q'):
			printGame()
			sys.exit(0)
	
	#	print(moves, bm.bombdropped, bombOn)			
		if(moves==1 and bm.bombdropped == 1):
			bmb.bombShow(arr,perm)
			bombOn = 1
	
		moveEnemy()
		for i in range(2*level+3):
			while(i<2*level+3 and enemy[i]==None):
				i+=1
	
			if i>=2*level+3:
				break
	#print(bm.x,enemy[i].x,bm.y,enemy[i].y)
			if(bm.x==enemy[i].x and bm.y==enemy[i].y):
				bm.lifes-=1
				if(bm.lifes>0):
					bm.x=1
					bm.y=1
					bm.spawnBomberman(arr,perm)
					i=6
				elif(bm.lifes==0):
					printGame()
					sys.exit(0)
		sideExplode()
		global level
		global checklevel
		if(checklevel!=level):
			level=checklevel
			break
