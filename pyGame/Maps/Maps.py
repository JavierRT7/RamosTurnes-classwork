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
## -- Define the class tile which is a sprite
class tile(pygame.sprite.Sprite):
    # Define the constructor for invader
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        # Set the position of the player attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class
class Player(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, color, width, height):
    # Set speed of the sprite
    self.speed_x = 0
    self.speed_y = 0
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = 20
    self.rect.y = 20
  #End Procedure

# Class update function - runs for each pass through the game loop
  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      self.speed_y = -1
      self.rect.y = self.rect.y + self.speed_y
    #End If
    if keys[pygame.K_DOWN]:
      self.speed_y = 1
      self.rect.y = self.rect.y + self.speed_y
    #End If
    if keys[pygame.K_RIGHT]:
      self.speed_x = 1
      self.rect.x = self.rect.x + self.speed_x
    #End If
    if keys[pygame.K_LEFT]:
      self.speed_x = -1
      self.rect.x = self.rect.x + self.speed_x
    #End If
#End Class
pacman_old_x = 20
pacman_old_y = 20
map = [[1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,0,0,0,0,1],
[1,1,0,1,1,1,1,1,0,1],
[1,0,0,0,0,0,1,0,0,1],
[1,0,1,0,1,0,1,1,0,1],
[1,0,1,0,1,0,1,0,0,1],
[1,0,1,0,1,0,1,1,1,1],
[1,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1]]
done = False
# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()
# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
        if map[x][y] == 1:
            my_wall = tile(BLUE, 20, 20, x*20, y *20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)
        #End If
    #Next
#Next
pacman = Player(YELLOW, 10, 10)
player_list.add(pacman)
all_sprites_list.add(pacman)
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
  # -- Check for collisions between pacman and wall tiles
  player_hit_list = pygame.sprite.spritecollide(pacman, wall_list, False)
  print (pacman.rect.x)
  for foo in player_hit_list:
    pacman.speed_x = 0
    pacman.speed_y = 0
    pacman.rect.x = pacman_old_x
    pacman.rect.y = pacman_old_y
  #Next
  pacman_old_x = pacman.rect.x
  pacman_old_y = pacman.rect.y
  # -- Game logic goes after this comment
  all_sprites_list.update()
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  all_sprites_list.draw (screen)
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()
