import pygame
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
# -- Exit game flag set to false
done = False
sun_x = -40
sun_y = 100
sun_y_movement = 16
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
  # -- User input and controls
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    #End If
  #Next event
  # -- Game logic goes after this comment
  ### SRC - I like what you are doing here, but what can you do to slow this down?
  ### You really want to increment x by one each time.
  sun_y_movement = sun_y_movement - 1
  sun_x = sun_x + 22
  sun_y = sun_y  - sun_y_movement
  if sun_x == 686:
      sun_x = -40
      sun_y = 100
      sun_y_movement = 16
    #End If
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  pygame.draw.rect(screen, BLUE, (220,165,200,150))
  pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(15) ### SRC - 15fps is a bit slow, makes jerky animation
#End While - End of game loop
pygame.quit()

