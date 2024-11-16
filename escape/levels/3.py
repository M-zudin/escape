xp=250
p_dir=1
xc=100
yc=475
while True:
    sleep(0.01)
    if xp>=550:
        p_dir=-1
    if xp<=250:
        p_dir=1
    xp+=p_dir*2
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
                if xc==30 and c>25:
                    c/=2
            if i.key == pygame.K_w:
                if yc==475:
                    for x in range(0,25):
                        yc-=4
                        sleep(0.01)
                        if xp>=550:
                            p_dir=-1
                        if xp<=250:
                            p_dir=1
                        xp+=p_dir
                        for i in pygame.event.get():
                            if i.type == pygame.MOUSEBUTTONDOWN:
                                (x,y) = pygame.mouse.get_pos()
                                print(x,y)
                            if i.type == pygame.KEYDOWN :
                                if i.key == pygame.K_d:
                                    if xc<970 and yc<485:
                                        xc+=10
                                if i.key == pygame.K_a:
                                    if xc>30 and yc<485:
                                        xc-=10
                            if yc>600:
                                xc=100
                                yc=475
                            screen.fill(black)
                            pygame.draw.rect(screen, r, [-100, 500, 300, 200], 5)
                            pygame.draw.rect(screen, r, [700, 500, 400, 200], 5)
                            pygame.draw.rect(screen, r, [xp, 500, 100, 50], 5)
                            pygame.draw.rect(screen, g, [850, 495, 100, 5], 5)
                            pygame.draw.polygon(screen, d, [(750,500),(800,500),(775,450)],1)
                            pygame.draw.circle(screen, white, (xc, yc), c)
                            pygame.display.update()
                                                    
    if ((xc>200 and xc<700) and (xc<xp or xc>xp+100)) and yc>=475 or yc<475 and no_fall==0:
        yc+=2
    if yc>475:
        yc+=2
    if yc>600 or (xc>=750 and xc<=800 and yc==475) or (xc>=750 and xc<=800 and yc==425):
        xc=100
        yc=475
    if xc>850 and xc<950 and yc>470:
        break
    screen.fill(black)
    pygame.draw.rect(screen, r, [-100, 500, 300, 200], 5)
    pygame.draw.rect(screen, r, [700, 500, 400, 200], 5)
    pygame.draw.rect(screen, r, [xp, 500, 100, 50], 5)
    pygame.draw.rect(screen, g, [850, 495, 100, 5], 5)
    pygame.draw.polygon(screen, d, [(750,500),(800,500),(775,450)],1)
    pygame.draw.circle(screen, white, (xc, yc), c)
    pygame.display.update()
