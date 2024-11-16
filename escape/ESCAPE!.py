import pygame
from hashlib import sha256
from time import sleep
no_fall=None
hasher=sha256()
cheat='5126' #2183 отключение падения 5126 - клик тп
hasher.update(cheat.encode('utf-8'))
if hasher.hexdigest()=='bc83cbb2d6dcba934deedb695609dd3ae689a72b210a8f1b86f6b1bc4c68d348':
    no_fall=1
    click_tp=0
elif hasher.hexdigest()=='74e06e9fbf9e88254ac47ed99bad31b06eb331c2dead308f74236d88f3041c0f':
    no_fall=0
    click_tp=1
else:
    no_fall=0
    click_tp=0
pygame.init()
screen = pygame.display.set_mode([1000,1000])
pygame.display.set_caption('Escape')
white=(255,255,255)
black=(0,0,0)
screen.fill(black)
pygame.display.update()
pygame.key.set_repeat(20,50)
r=(150,100,200)
g=(0,255,0)
d=(255,0,0)
c=25
a=open('levels//1.py','rb')
lvl_data=a.read()
a.close()
exec(lvl_data)
lvl_data=None
a=open('levels//2.py','rb')
lvl_data=a.read()
a.close()
exec(lvl_data)
lvl_data=None
com=0
a=open('levels//3.py','rb')
lvl_data=a.read()
a.close()
exec(lvl_data)
lvl_data=None
com=0
