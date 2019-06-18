# The ball is flying to the left and tothe right 
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Flying ball")
#clock = pygame.time.Clock()

x=250
y=250
r=30
vol=10

done = False
clock = pygame.time.Clock()
left=True

while not done:
    pygame.time.delay(100)

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    # змінює координату х центра круга
    
    if left == True and x>r+vol:
        x = x-vol
        left=True
    else: 
        left=False

    if left == False and x<500-r-vol:
        x = x+vol
        left=False
    else:
        left=True

    # забирає слід
    screen.fill((0,0,0))

    # малює круг
    pygame.draw.circle(screen, (128,0,0), (x,y), r)
    
    
    pygame.display.update()
	#clock.tick(60)
