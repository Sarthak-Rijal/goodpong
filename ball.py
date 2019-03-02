import pygame
import math
from paddle_object import paddle

pygame.init()

WIDTH = 858
HEIGHT = 525
WALL_PADDING = 5


class Ball(object):
	
	def __init__(self, screen,x,y,size,x_speed,y_speed):
		
		self.screen = screen
		self.x = x
		self.y = y
		self.size = size
		self.x_speed = x_speed
		self.y_speed = y_speed 

	def move(self):
		self.x+=self.x_speed
		self.y+=self.y_speed

		if (self.y <= WALL_PADDING or self.y + self.size >= HEIGHT - WALL_PADDING):
			self.y_speed = -self.y_speed

		pygame.draw.rect(self.screen,(255,255,255),[self.x,self.y,self.size,self.size])


	def bounce(self,angle,padd, speed = 15):
		relativeY = (padd.y+(padd.length/2)) - self.y+self.size/2
		normalizedY = (relativeY / (padd.length / 2))
		bounceAngle = normalizedY * angle
		if (padd.player == 'one'):
			self.x_speed = -math.cos(bounceAngle)* speed
			self.y_speed = -math.sin(bounceAngle)* speed
		else:
			self.x_speed = math.cos(bounceAngle)* speed
			self.y_speed = -math.sin(bounceAngle)* speed

		

	def collide(self,other):
		return other.colliderect(pygame.Rect(self.x,self.y,self.size,self.size))


