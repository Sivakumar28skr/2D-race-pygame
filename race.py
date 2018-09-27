import pygame,time,random,shelve
from pygame.locals import*


pygame.init()

pygame.mixer.music.load('Cars Life is a Highway.mp3')
display_width= 450
display_hieght= 600

white=(255,255,255)
black=(0,0,0)
bright_black=(50,50,50)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
dark_green=(0,199,0)
dark_red=(200,0,0)

gameDisplay= pygame.display.set_mode((display_width,display_hieght))
pygame.display.set_caption('A bit Racey')
clock=pygame.time.Clock()

carImg=pygame.image.load('cars.png')
carImg=pygame.transform.scale(carImg,(90,160))

carIcon=pygame.image.load('caricon.jpg')
pygame.display.set_icon(carIcon)

oppcarImg=pygame.image.load('car.png')
oppcarImg=pygame.transform.scale(oppcarImg,(90,160))

road=pygame.image.load('road.jpg')
road=pygame.transform.scale(road,(450,600))

def line(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay, color,[thingx,thingy,thingw,thingh])
    #gameDisplay.blit(line,(thingx,thingy))
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
def oppcar(x,y):
    gameDisplay.blit(oppcarImg,(x,y))

    
def message_display(text,size,color,x,y):
    largeText=pygame.font.SysFont('comicsansms',size)
    textSurf=largeText.render(text,True,color)
    TextRect= textSurf.get_rect()
    TextRect.center= (x,y)
    gameDisplay.blit(textSurf,TextRect)
    pygame.display.update()
    
def carscore(count):
    font=pygame.font.SysFont(None,35)
    text=font.render('Score: '+ str(count), True, blue)
    gameDisplay.blit(text,(0,0))
def crash(score):
    pygame.mixer.music.stop()
    #sound.play()
    message_display('You Crashed',60,blue,(display_width/2),(display_hieght/2))
    time.sleep(3)
    gameDisplay.fill(black)
    message_display('You Crashed',60,blue,(display_width/2),(display_hieght/2))
    message_display('Click Space for Restart',20,red,(display_width/2),(display_hieght/2+100))
    message_display('Click Esc for Quit',20,red,(display_width/2),(display_hieght/2+180))
    shelfFile=shelve.open('race')
    highScore=shelfFile['highscore']
    if score > highScore:
        shelfFile['highscore']=score
        shelfFile.close
        message_display(('Highscore :'+str(score)),25,white,(display_width/2-100),(display_hieght/2+270))
        message_display(('Score :'+str(score)),30,white,(display_width/2-100),(display_hieght/2+230))
    else:
        message_display(('Highscore :'+str(highScore)),25,white,(display_width/2-100),(display_hieght/2+270))
    message_display(('Score :'+str(score)),30,white,(display_width/2-100),(display_hieght/2+230))
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
                elif event.key ==pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    game_loop()
                if event.key==pygame.K_ESCAPE:
                    pygame.quit()

                    quit()
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause=False
    l=3
    while l>=0:
        pygame.draw.rect(gameDisplay, (50,50,50),[display_width/2-30,display_hieght/2-100,80,80])
        message_display(str(l),60,red,(display_width/2+10),(display_hieght/2-70))
        l=l-1
        pygame.display.update()
        time.sleep(1)
def paused():
    pygame.mixer.music.pause()
    message_display('Paused',90,red,(display_width/2),(display_hieght/2))
    while pause:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    unpause()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    game_loop()        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        pygame.draw.rect(gameDisplay,dark_green,(100,400,80,40))
        message_display('continue',20,bright_black,140,420)
        pygame.draw.rect(gameDisplay,dark_red,(290,400,80,40))
        message_display('Restart',20,bright_black,330,420)
        
        if 100<mouse[0]<180 and 400<mouse[1]<440:
            pygame.draw.rect(gameDisplay,green,(100,400,80,40))
            message_display('continue',20,black,140,420)
            pygame.display.update()
            if click[0]==1:
                unpause()
        #pygame.draw.rect(gameDisplay,red,(200,400,80,40))
        if 290<mouse[0]<370 and 400<mouse[1]<440:
            pygame.draw.rect(gameDisplay,red,(290,400,80,40))
            message_display('Restart',20,black,330,420)
            pygame.display.update()
            if click[0]==1:
                game_loop()
             
        pygame.display.update()
        clock.tick(30)
def intro():
    message_display('Car Race',90,red,(display_width/2),(display_hieght/2))
    time.sleep(1)
    message_display('Click Space to Begin',20,blue,(display_width/2),(display_hieght/2+50))
    while True:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    
                pygame.quit()
                quit()
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    game_loop()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_SPACE:
                    game_loop()        
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        pygame.draw.rect(gameDisplay,dark_green,(170,400,80,40))
        if 170<mouse[0]<270 and 400<mouse[1]<450:
            pygame.draw.rect(gameDisplay,green,(170,400,80,40))
            message_display('GO>>',25,black,210,420)
            if click[0]==1:
                game_loop()
        message_display('GO>>',25,bright_black,210,420)     
        pygame.display.update()
        clock.tick(15)

def game_loop():
    l=3
    while l>=0:
        pygame.draw.rect(gameDisplay, (50,50,50),[display_width/2-30,display_hieght/2-100,80,80])
        message_display(str(l),60,red,(display_width/2+10),(display_hieght/2-70))
        l=l-1
        pygame.display.update()
        time.sleep(1)
    pygame.mixer.music.play()
    global pause
    liney1=0
    liney2=170
    liney3=340
    liney4=510
    thing_startx=random.choice([80,display_width-170])
    thing_starty=-600
    thing_speed=5
    line_speed=3
    line_length=130
    x = 80
    y = (display_hieght * 0.75)

    x_change=0
    score=0
    crashed=False
    while not crashed:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:

                
                
                pygame.quit()
                quit()

            
            if event.type== pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    x=80
                elif event.key ==pygame.K_RIGHT:
                    x=display_width-170
                elif event.key==pygame.K_p:
                    pause=True
                    paused()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    x=80
                if event.key==pygame.K_RIGHT:
                    x=display_width-170
                elif event.key==pygame.K_p:
                    pause=True
                    paused()
        gameDisplay.fill(white)
        gameDisplay.blit(road,(0,0))
        
            
        line(display_width/2,liney1,20,line_length,white)
        line(display_width/2,liney2,20,line_length,white)
        line(display_width/2,liney3,20,line_length,white)
        line(display_width/2,liney4,20,line_length,white)
        liney1+=line_speed
        liney2+=line_speed
        liney3+=line_speed
        liney4+=line_speed
        if liney4>display_hieght:
            liney4=0-line_length+40
            line_speed+=1
        if liney3>display_hieght:
            liney3=0-line_length+40
        if liney2>display_hieght:
            liney2=0-line_length+40
        if liney1>display_hieght:
            liney1=0-line_length+40
        oppcar(thing_startx,thing_starty)
        thing_starty+=thing_speed
        car(x,y)
        carscore(str(score))
        if thing_starty > display_hieght:
            thing_starty=0-160
            thing_startx=random.choice([80,display_width-170])
            score+=1
            thing_speed+=1
        if y< thing_starty+150:

            if x==thing_startx: #and x<thing_startx+100 or x+90>thing_startx and x+90<thing_startx+80:
                thing_speed=0
                crash(score)
                
                
        pygame.display.update()
        clock.tick(40)

        
intro() 

pygame.quit()
quit()
