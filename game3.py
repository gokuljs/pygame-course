# creating interactions 
import pygame  # import pygame library for accesing pygame frame work


pygame.init() # intializes all the modules for required for it
screen = pygame.display.set_mode((400, 300)) # display window which is going to pop up in desired size and height
done = False
is_blue = True

while not done:
    for event in pygame.event.get(): # if we did not give pygame.event.get() event is going to become unresponsive  un
        if event.type == pygame.QUIT:# this even is fired up during close button of the window
            done = True
    pygame.draw.rect(screen,(0,128,255),pygame.Rect(30,30,60,60)) #creating rectangle in the screen
# in the a bove line rect represents an rectangle the after three cooderniates represents screen color and pygame.react
    # is used to mention co ordinates of the rectangle
    if is_blue:
        color = (0, 128, 255)   #this part of code pick a color conditionally
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))

    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:# this contion wat happens is if we press the space key the
                                            # color of the recatngular box which we have created will change drastically

        is_blue = not is_blue


    pygame.display.flip() #his call is required in order for any updates that you make to the game screen to become visible.