### SRC - This is a good start but needs some more work

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
pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
  # -- User input and controls
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    #End If
    keys = pygame.key.get_pressed()
        ## - the up key or down key has been pressed
    ### SRC - do not change the position of the paddle here, just it's speed/direction.
    if keys[pygame.K_UP]:
          y_padd = y_padd - 5 
    if keys[pygame.K_DOWN]:
          y_padd = y_padd + 5
  #Next event
  # -- Game logic goes after this comment
  if x_val == x_padd:  ### SRC - It might not be equal, especially if you make the ball go faster.
      if y_val == y_padd:
          x_direction = 1
      #End If
  #End If
  if x_val == 640:
      x_direction = -1
      #End If
  if x_val < -10:
      x_direction = 1
      x_val = 150
      y_val = 200
      #End If
  if y_val == 0:
      y_direction = 1
      #End If
  if y_val == 480:
      y_direction = -1
  x_val = x_val + x_direction
  y_val = y_val + y_direction
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
  pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()
