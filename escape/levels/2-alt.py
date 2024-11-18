#maybe it will be called "lost level"
xc=100
yc=475
p=0
xp=250
while True:
        sleep(0.02)
        if xp>600:
            p+=1
        if xp<250:
            p+=1
        if p%2==0:
            xp+=3
        if p%2==1:
            xp-=3
        screen.fill(black)
        for i in pygame.event.get():
            if i.type == pygame.MOUSEBUTTONDOWN:
                (x,y) = pygame.mouse.get_pos()
                print(x,y)
                if click_tp==1:
                    xc=(x,y)[0]
                    yc=(x,y)[1]
            if i.type == pygame.KEYDOWN :
                if i.key == pygame.K_d:
                    if xc<970 and yc<485:
                        xc+=10
                    if xc==970:
                        c=c*2
                if i.key == pygame.K_a:
                    if xc>30 and yc<485:
                        xc-=10
                if i.key == pygame.K_w:
                    if yc>470 and yc<480:
                        for x in range(0,25):
                            sleep(0.02)
                            yc-=4
                            if xp>650:
                                p+=1
                            if xp<250:
                                p+=1
                            if p%2==0:
                                xp+=3
                            if p%2==1:
                                xp-=3
                            for i in pygame.event.get():
                                if i.type == pygame.MOUSEBUTTONDOWN:
                                    (x,y) = pygame.mouse.get_pos()
                                    print(x,y)
                                keys = pygame.key.get_pressed()
                                if keys[pygame.K_d]:
                                    if xc<970 and yc<485:
                                        xc+=10
                                if keys[pygame.K_a]:
                                    if xc>30 and yc<485:
                                        xc-=10
                                if yc>600:
                                    xc=100
                                    yc=475
                                screen.fill(black)
                                pygame.draw.rect(screen, r, [-100, 500, 350, 200], 5)
                                pygame.draw.rect(screen, r, [700, 500, 600, 200], 5)
                                pygame.draw.rect(screen, r, [xp, 500, 100, 10], 5)
                                pygame.draw.rect(screen, g, [850, 495, 100, 5], 5)
                                pygame.draw.circle(screen, white, (xc, yc), c)
                                pygame.display.update()
        
        if xc>250 and xc<700 and yc>=475 or yc<475 and no_fall==0:
            if xc>xp-5 and xc<xp+105 and yc>473 and yc<478:
                print('',end='')
            else:
                yc+=4
                    
        if yc>600:
            xc=100
            yc=475
        if xc>850 and xc<950 and yc>470:
            break
        pygame.draw.rect(screen, r, [-100, 500, 350, 200], 5)
        pygame.draw.rect(screen, r, [700, 500, 600, 200], 5)
        pygame.draw.rect(screen, r, [xp, 500,100,10], 5)
        pygame.draw.rect(screen, g, [850, 495, 100, 5], 5)
        pygame.draw.circle(screen, white, (xc, yc), c)
        pygame.display.update()
