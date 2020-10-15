import pygame
import random
import math
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255, 0, 0)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")
## -- Define the class snow which is a sprite
class Invader(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, color, width, height, speed):
    # Set speed of the sprite
    self.speed = speed
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = random.randrange(0, 600)
    self.rect.y = random.randrange(0, -50, -1)
  #End Procedure
#End Class
# Class update function - runs for each pass through the game loop
  def update(self):
    self.rect.y = self.rect.y + self.speed
    
class Player(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, color, width, height, bullet_count):
    # Set speed of the sprite
    self.speed = 0
    self.bullet_count = 50
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = 10
    self.rect.y = 470
    ### SRC - I'm not sure what the line below was trying to do...
    ##self.rect = (300, size[0] - height)
  #End Procedure

# Class update function - runs for each pass through the game loop
  def update(self):
    self.rect.x = self.rect.x + self.speed
#End Class
class Bullet(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, color, width, height, speed):
    # Set speed of the sprite
    self.speed = 2
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = player.rect.x
    self.rect.y = player.rect.y
  #End Procedure
# Class update function - runs for each pass through the game loop
  def update(self):
    self.rect.y = self.rect.y - self.speed
#End Class
  #End Procedure   
# -- Exit game flag set to false
done = False
lives = 5
Lives = "Lives: 5"
score = 0
Score = "Score: 0"
Bullets = "Bullets: 50"
# Create a list of the snow blocks
invader_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# Create the snowflakes
number_of_invaders = 10 # we are creating 50 snowflakes
for x in range (number_of_invaders):
    invader = Invader(BLUE, 10, 10, 1) # snowflakes are white with size 5 by 5 px
    invader_group.add (invader) # adds the new snowflake to the group of snowflakes
    all_sprites_group.add (invader) # adds it to the group of all Sprites
#Next x
player = Player(YELLOW, 10, 10, 50) # snowflakes are white with size 5 by 5 px
player_group.add (player) # adds the new snowflake to the group of snowflakes
all_sprites_group.add (player) # adds it to the group of all Sprites
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
  # -- User inputs here
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
    elif event.type == pygame.KEYDOWN: # - a key is down
      if event.key == pygame.K_LEFT: # - if the left key pressed
        player.speed = -3 # speed set to -3
      elif event.key == pygame.K_RIGHT: # - if the right key pressed
        player.speed = 3 # speed set to 3
    elif event.type == pygame.KEYUP: # - a key released
      if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        player.speed = 0 # speed set to 0
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        bullet = Bullet(RED, 2, 2, 2) # snowflakes are white with size 5 by 5 px
        bullet_group.add (bullet) # adds the new snowflake to the group of snowflakes
        all_sprites_group.add (bullet) # adds it to the group of all Sprites
        player.bullet_count = player.bullet_count - 1
        Bullets = "Bullets: " + str(player.bullet_count)
  #Next event
  # -- Game logic goes after this comment
  bullet_hit_group = pygame.sprite.groupcollide(bullet_group, invader_group, dokilla=False, dokillb=True, collided=None)
  for foo in bullet_hit_group:
          score = score + 5
          Score = "Score: " + str(score)
  #Next Event
  # -- when invader hits the player add 5 to score.
  player_hit_group = pygame.sprite.spritecollide(player, invader_group, True)
  for foo in player_hit_group:
    lives = lives - 1
    Lives = "Lives: " + str(lives)
  #Next Event
  all_sprites_group.update()
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  font = pygame.font.SysFont('Calibri', 25, True, False)
  text = font.render(Lives, True, WHITE)
  screen.blit(text, [10, 10])
  font = pygame.font.SysFont('Calibri', 25, True, False)
  text = font.render(Score, True, WHITE)
  screen.blit(text, [10, 30])
  font = pygame.font.SysFont('Calibri', 25, True, False)
  text = font.render(Bullets, True, WHITE)
  screen.blit(text, [10, 50])
  all_sprites_group.draw (screen)
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()

