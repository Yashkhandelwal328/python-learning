import pygame
from sys import exit


# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: # This will help to quit the window
#             pygame.quit()  # THis is basically opposite of pygame.init it uninitializes the code polor oppsoite
#     # draw all our elements 
#     #also update everything like ldisplay ill do below this line
#     pygame.display.update() # Now we can call the code and windows will stay forever but it wont get ant input (also the one used to close the window) (putting a line at line no 7 will make it get events)
# # When ever we use this and press crooss to quit we will get this error "pygame.error: video system not initialized" cuz we close pygame with QUIT but the while loop is still open 
# # We can try using a break statement
# # But the best way to do it by using sys module it helps to close any program entirely ezily


# now the better way to do it with exit() from sys module

pygame.init() # necessary This initializes the code of pygame
screen = pygame.display.set_mode((800,400)) # screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Runner') # THis is used to name the window
clock = pygame.time.Clock() # used to set a fps cap
test_font = pygame.font.Font('font/Pixeltype.ttf',50) # We will have to first create a text then display it as image

test_surface = pygame.Surface((100,200)) # test_surface = pygame.Surface((width,height))
# test_surface.fill('Red') # This will fill the test_suface with red color # Comented out cuz wanted to use image.load
sky_surface = pygame.image.load('graphics/Sky.png').convert() # help to load a graphic like image
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My game',False,'Black') # test_font.render(text,Anti Aliasing,color) # set AA to true for anything beside pixxel art cuz that maeks the edges smooth
# Now ill add animation in this first we need to import our snail image

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha() # will remove the background convert() is for it convert it to a format in with pygame can work faster
snail_x_pos = 600

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha() # Importing player
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # Will quit pygame then below one will quit while loo[]
            exit() # This will quit the while loop 
    
    screen.blit(sky_surface,(0,0)) # Block image transfer (fancy way of saying you want to put one surface on another surface) (surface,pos)
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    snail_x_pos -= 4 # This will dec snail x pos by the for loop 60 times per sec
    if snail_x_pos < -100:
        snail_x_pos = 800
    screen.blit(snail_surface,(snail_x_pos,250))
    screen.blit(player_surf,(80,200))
    pygame.display.update()
    clock.tick(60) # This will tell the for loop to only play at 60 fps cap
# Output will be a red screen on top of black at top left corner of 200 from left and 100 from top with is spread 100 w and 200b putting back to 0,0
# in pygame (0,0) is at top lefp corner we go right it increases x and botom = inc y opposite of normal graphs

