import pygame
import random
import math
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
pygame.display.set_caption("Snow")
## -- Define the class snow which is a sprite
class Snow(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, color, width, height):
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(0, 600)
    self.rect.y = random.randrange(0, 400)
  #End Procedure
#End Class
# -- Exit game flag set to false
done = False
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
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()
