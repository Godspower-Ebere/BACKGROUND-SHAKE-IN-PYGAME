import pygame
pygame.init()

size=width,height=(800,600)
screen=pygame.display.set_mode(size)

bg=pygame.transform.scale(pygame.image.load("bg.png"),(width+width/2,height+10))
x=-5
y=-5
shake=20

vibration=0
vibrate=False

vib=pygame.mixer.Sound("explosion.wav")

run=True
while run:
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
    key=pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        vibrate=True
        
    if vibrate:
        vibration+=1
        print(vibration)
        if vibration==10:
            x-=shake
            vib.play()
        if vibration==15:
            x+=shake
            
        if vibration==20:
            x-=shake
        if vibration==25:
            x+=shake                                                
            vibration=0
            vibrate=False
        
    screen.blit(bg,(x,y))
    pygame.display.update()
pygame.quit()
