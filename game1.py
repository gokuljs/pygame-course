
import pygame  # import pygame library for accesing pygame frame work


pygame.init() # intializes all the modules for required for it
screen = pygame.display.set_mode((400, 300)) # display window which is going to pop up in desired size and height
done = False

while not done:
    for event in pygame.event.get(): # if we did not give pygame.event.get() event is going to become unresponsive  un
        if event.type == pygame.QUIT:# this even is fired up during close button of the window
            done = True

    pygame.display.flip() #his call is required in order for any updates that you make to the game screen to become visible.