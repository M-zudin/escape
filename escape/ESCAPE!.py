a=open('data//2-alt.dat')
f=a.readline()
if f.lower()=='use 2-alt level instead of 2: true':
    use_2_alt=True
else:
    use_2_alt=False
b=open('data//level.dat')
lvl=int(b.read())
b.close()
import pygame
from hashlib import sha256
from time import sleep
import os
no_fall=None
hasher=sha256()
cheat='51' #2183 отключение падения 5126 - клик телепорт 134680472 секретный скины
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
screen = pygame.display.set_mode([1000,800])
pygame.display.set_caption('Escape')
white=(255,255,255)
black=(0,0,0)
screen.fill(black)
pygame.display.update()
pygame.key.set_repeat(20,50)
ye=(200,180,0)
gr=(200,200,200)
r=(150,100,200)
g=(0,255,0)
d=(255,0,0)
f1 = pygame.font.Font(None, 100)
text1 = f1.render('lvl', 1, (255, 255, 255))
c=25
def save_lvl():
    os.remove('data//level.dat')
    b=open('data//level.dat','wb')
    b.write(str(lvl).encode('utf-8'))
    b.close()
def start_level(num):
    lvl_data=None
    a=open(f'levels//{num}.py','rb')
    lvl_data=a.read()
    a.close()
    exec(lvl_data)
def menu():
    global text1,lvl
    while True:
        a=0
        text1 = f1.render('lvl', 1, (255, 255, 255))
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                if x>50 and x<200 and y<200 and y>50:
                    while a==0:
                        for i in pygame.event.get():
                            if i.type == pygame.MOUSEBUTTONDOWN:
                                (x,y) = pygame.mouse.get_pos()
                                if x>50 and x<200 and y<200 and y>50:
                                    a+=1
                                if x>50 and x<200 and y<400 and y>250:
                                    start_level(1)
                                    if lvl<1:
                                        lvl+=1
                                        save_lvl()
                                if x>250 and x<400 and y<400 and y>250 and lvl>0:
                                    if use_2_alt==True:
                                        start_level('2-alt')
                                        if lvl<2:
                                            lvl+=1
                                            save_lvl()
                                    else:
                                        start_level(2)
                                        if lvl<2:
                                            lvl+=1
                                            save_lvl()
                                if x>450 and x<600 and y<400 and y>250 and lvl>1:
                                    start_level(3)
                                    if lvl<3:
                                        lvl+=1
                                        save_lvl()
                        text1 = f1.render('x', 1, (255, 255, 255))
                        text2 = f1.render('1', 1, (255, 255, 255))
                        text3 = f1.render('2', 1, (255, 255, 255))
                        text4 = f1.render('3', 1, (255, 255, 255))
                        screen.fill(black)
                        pygame.draw.rect(screen, ye, [50, 50, 150, 150])
                        pygame.draw.rect(screen, ye, [50, 250, 150, 150])
                        if lvl<1:
                            pygame.draw.rect(screen, gr, [250, 250, 150, 150])
                        else:
                            pygame.draw.rect(screen, ye, [250, 250, 150, 150])
                        if lvl<2:
                            pygame.draw.rect(screen, gr, [450, 250, 150, 150])
                        else:
                            pygame.draw.rect(screen, ye, [450, 250, 150, 150])
                        screen.blit(text1, (105, 95))
                        screen.blit(text2, (105, 295))
                        screen.blit(text3, (305, 295))
                        screen.blit(text4, (505, 295))
                        pygame.display.update()
        screen.fill(black)
        pygame.draw.rect(screen, ye, [50, 50, 150, 150])
        pygame.draw.rect(screen, ye, [250, 50, 150, 150])
        pygame.draw.circle(screen, white, (325,125), 65)
        screen.blit(text1, (85, 95))
        pygame.display.update()
menu()

