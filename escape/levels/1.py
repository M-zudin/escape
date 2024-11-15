xc=100
yc=475
while True:
    sleep(0.01)
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
                if yc==475 or yc==474:
                    for x in range(0,25):
                        yc-=4
                        sleep(0.01)
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
                            pygame.draw.rect(screen, r, [-100, 500, 500, 200], 5)
                            pygame.draw.rect(screen, r, [500, 500, 600, 200], 5)
                            pygame.draw.rect(screen, g, [650, 495, 100, 5], 5)
                            pygame.draw.circle(screen, white, (xc, yc), c)
                            pygame.display.update()                                                    
    if xc>400 and xc<500 and yc>=475 or yc<475 and no_fall==0:
        yc+=2
    if yc>600:
        xc=100
        yc=475
    if xc>650 and xc<750 and yc>470:
        break
    screen.fill(black)
    pygame.draw.rect(screen, r, [-100, 500, 500, 200], 5)
    pygame.draw.rect(screen, r, [500, 500, 600, 200], 5)
    pygame.draw.rect(screen, g, [650, 495, 100, 5], 5)
    pygame.draw.circle(screen, white, (xc, yc), c)
    pygame.display.update()
