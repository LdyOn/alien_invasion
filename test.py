import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite

from setting import Setting
from ship import Ship
from game_stats import GameStats
import game_functions as gf


group_a = Group();

class A(Sprite):
	"""docstring for A"""
	def __init__(self):
		super().__init__()
		self.hello = 123

	def say(self):
		print("hello")
for x in range(10):
	a = A()
	group_a.add(a)
# for a in group_a:
# 	a.say()
mark = []
for x in range(27):
	mark.append(1)
	break;
print(mark)
		