import pygame
import random
# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)
ORANGE = (255,150,0)
GREEN = (0,255,0)
# -- Initialise PyGame
pygame.init()
pygame.font.init()
pygame.mixer.init()
# -- Blank Screen
size = (1200,720)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("My Window")
#Classes
class Player(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, width, height, health, money, keys, score, bullets):
    # Set speed of the sprite
    self.speed_x = 0
    self.speed_y = 0
    self.health = 100
    self.money = 0
    self.keys = 0
    self.score = 0
    self.bullets = bullets
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    #self.image = pygame.Surface([width,height])
    self.image = pygame.image.load('paccers.png')
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.rect.x = 490
    self.rect.y = 40
  #End Procedure
# Class update function - runs for each pass through the game loop
  def update(self):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
      self.image = pygame.image.load('paccers - up.png')
      self.speed_y = -3
      self.rect.y = self.rect.y + self.speed_y
    #End If
    if keys[pygame.K_DOWN]:
      self.image = pygame.image.load('paccers - down.png')
      self.speed_y = 3
      self.rect.y = self.rect.y + self.speed_y
    #End If
    if keys[pygame.K_RIGHT]:
      self.image = pygame.image.load('paccers.png')
      self.speed_x = 3
      self.rect.x = self.rect.x + self.speed_x
    #End If
    if keys[pygame.K_LEFT]:
      self.image = pygame.image.load('paccers - left.png')
      self.speed_x = -3
      self.rect.x = self.rect.x + self.speed_x
    #End If
    if keys[pygame.K_w]:
      self.image = pygame.image.load('paccers - up.png')
      if self.bullets > 0:
        bullet = Bullet(RED, 5, 5, 0, -5)
        bullet.rect.x = player.rect.x + 10
        bullet.rect.y = player.rect.y - 3
        bullet_group.add(bullet)
        all_sprites_group.add(bullet)
        self.bullets = self.bullets - 1
      #End If
    #End If
    if keys[pygame.K_s]:
      self.image = pygame.image.load('paccers - down.png')
      if self.bullets > 0:
        bullet = Bullet(RED, 5, 5, 0, 5)
        bullet.rect.x = player.rect.x + 10
        bullet.rect.y = player.rect.y + 23
        bullet_group.add(bullet)
        all_sprites_group.add(bullet)
        self.bullets = self.bullets - 1
      #End If
    #End If
    if keys[pygame.K_a]:
      self.image = pygame.image.load('paccers - left.png')
      if self.bullets > 0:
        bullet = Bullet(RED, 5, 5, -5, 0)
        bullet.rect.x = player.rect.x - 3
        bullet.rect.y = player.rect.y + 10
        bullet_group.add(bullet)
        all_sprites_group.add(bullet)
        self.bullets = self.bullets - 1
      #End If
    #End If
    if keys[pygame.K_d]:
      self.image = pygame.image.load('paccers.png')
      if self.bullets > 0:
        bullet = Bullet(RED, 5, 5, 5, 0)
        bullet.rect.x = player.rect.x + 23
        bullet.rect.y = player.rect.y + 10
        bullet_group.add(bullet)
        all_sprites_group.add(bullet)
        self.bullets = self.bullets - 1
      #End If
    #End If
#End Class
class Wall(pygame.sprite.Sprite):
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
class Display(pygame.sprite.Sprite):
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
class Enemy(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, width, height, speed_x, speed_y, wall_group):
    # Set speed of the sprite
    self.speed_x = speed_x
    self.speed_y = speed_y
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.image.load('ghost.jpg')
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.old_x = self.rect.x
    self.old_y = self.rect.y
    self.wall_group = wall_group
    #self.enemy_hit_list = []pygame.sprite.spritecollide(self, wall_group, False)
  #End Procedure
  def update(self):
    if self.speed_x > 0:
      self.image = pygame.image.load('ghost - right.jpg')
    #End If
    if self.speed_x < 0:
      self.image = pygame.image.load('ghost.jpg')
    #End If
    self.rect.x = self.rect.x + self.speed_x
    self.rect.y = self.rect.y + self.speed_y
    enemy_hit_list = pygame.sprite.spritecollide(self, self.wall_group, False)
    for foo in enemy_hit_list:
      self.speed_x = random.randint(-3, 3)
      self.speed_y = random.randint(-3, 3)
      if self.speed_x == 0 and self.speed_y == 0:
        self.speed_x = random.randint(-3, 3)
        self.speed_y = random.randint(-3, 3)
      self.rect.x = self.old_x
      self.rect.y = self.old_y
    #Next
    enemy_group.remove(self)
    enemy_enemy_hit_list = pygame.sprite.spritecollide(self, enemy_group, False)
    for foo in enemy_enemy_hit_list:
      self.speed_x = random.randint(-3, 3)
      self.speed_y = random.randint(-3, 3)
      self.rect.x = self.old_x
      self.rect.y = self.old_y
    #Next
    enemy_group.add(self)
    if self.speed_x == 0 and self.speed_y == 0:
      self.speed_x = random.randint(-3, 3)
      self.speed_y = random.randint(-3, 3)
    self.old_x = self.rect.x
    self.old_y = self.rect.y
  #End Procedure
#End Class
class Boss(pygame.sprite.Sprite):
  def __init__(self, width, height, speed_x, speed_y, wall_group, health, bullets):
    # Set speed of the sprite
    self.speed_x = speed_x
    self.speed_y = speed_y
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.image.load('boss.png')
    # Set the position of the sprite
    self.rect = self.image.get_rect()
    self.old_x = self.rect.x
    self.old_y = self.rect.y
    self.wall_group = wall_group
    self.health = health
    self.bullets = bullets
    #self.enemy_hit_list = []pygame.sprite.spritecollide(self, wall_group, False)
  #End Procedure
  def update(self):
    if self.speed_x > 0:
      self.image = pygame.image.load('boss.png')
    #End If
    if self.speed_x < 0:
      self.image = pygame.image.load('boss - left.png')
    #End If
    self.rect.x = self.rect.x + self.speed_x
    self.rect.y = self.rect.y + self.speed_y
    boss_hit_list = pygame.sprite.spritecollide(self, self.wall_group, False)
    for foo in boss_hit_list:
      self.speed_x = random.randint(-5, 5)
      self.speed_y = random.randint(-5, 5)
      if self.speed_x == 0 and self.speed_y == 0:
        self.speed_x = random.randint(-5, 5)
        self.speed_y = random.randint(-5, 5)
      self.rect.x = self.old_x
      self.rect.y = self.old_y
    #Next
    self.old_x = self.rect.x
    self.old_y = self.rect.y
    if self.bullets > 0:
      if player.rect.x == boss.rect.x and player.rect.y > boss.rect.y:
        boss_bullet = Bullet(RED, 5, 5, 0, 5)
        boss_bullet.rect.x = boss.rect.x + 15
        boss_bullet.rect.y = boss.rect.y + 15
        boss_bullet_group.add(boss_bullet)
        all_sprites_group.add(boss_bullet)
        boss.bullets = boss.bullets - 1
      #End If
      if player.rect.x == boss.rect.x and player.rect.y < boss.rect.y:
        boss_bullet = Bullet(RED, 5, 5, 0, -5)
        boss_bullet.rect.x = boss.rect.x + 15
        boss_bullet.rect.y = boss.rect.y + 15
        boss_bullet_group.add(boss_bullet)
        all_sprites_group.add(boss_bullet)
        boss.bullets = boss.bullets - 1
      #End If
      if player.rect.y == boss.rect.y and player.rect.x > boss.rect.x:
        boss_bullet = Bullet(RED, 5, 5, 5, 0)
        boss_bullet.rect.x = boss.rect.x + 15
        boss_bullet.rect.y = boss.rect.y + 15
        boss_bullet_group.add(boss_bullet)
        all_sprites_group.add(boss_bullet)
        boss.bullets = boss.bullets - 1
      #End If
      if player.rect.y == boss.rect.y and player.rect.x < boss.rect.x:
        boss_bullet = Bullet(RED, 5, 5, -5, 0)
        boss_bullet.rect.x = boss.rect.x + 15
        boss_bullet.rect.y = boss.rect.y + 15
        boss_bullet_group.add(boss_bullet)
        all_sprites_group.add(boss_bullet)
        boss.bullets = boss.bullets - 1
      #End If
    #End If
  #End Procedure
#End Class
class Bullet(pygame.sprite.Sprite):
  # Define the constructor for snow
  def __init__(self, color, width, height, speed_x, speed_y):
    # Set speed of the sprite
    self.speed_x = speed_x
    self.speed_y = speed_y
    # Call the sprite constructor
    super().__init__()
    # Create a sprite and fill it with colour
    self.image = pygame.Surface([width,height])
    self.image.fill(color)
    # Set the position of the sprite
    self.rect = self.image.get_rect()
  #End Procedure
# Class update function - runs for each pass through the game loop
  def update(self):
    self.rect.x = self.rect.x + self.speed_x
    self.rect.y = self.rect.y + self.speed_y
  #End Procedure
#End Class
# -- Exit game flag set to false
map = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1],
[1,0,1,1,1,1,1,1,1,0,0,0,1,0,0,1,0,1],
[1,0,0,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],
[1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
[1,0,1,1,1,0,0,0,1,0,0,1,1,1,1,0,0,1],
[1,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,1],
[1,0,0,1,1,1,0,0,1,1,1,1,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1],
[1,0,0,1,1,1,0,0,0,0,1,0,1,1,1,1,0,1],
[1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,1],
[1,0,0,1,0,1,1,1,0,1,1,1,1,1,1,0,0,1],
[1,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,1],
[1,0,1,1,1,1,0,0,1,1,1,0,0,0,0,1,0,1],
[1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,0,1],
[1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,0,1],
[1,0,0,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
screen_colour = WHITE
done = False
all_sprites_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
display_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
boss_group = pygame.sprite.Group()
boss_bullet_group = pygame.sprite.Group()
enemy_number = 20
player = Player(20, 20, 100, 0, 0, 0, 1000)
player_group.add(player)
all_sprites_group.add(player)
for y in range(18):
    for x in range(25):
        if map[x][y] == 1:
            my_wall = Wall(RED, 40, 40, x*40, y *40)
            wall_group.add(my_wall)
            all_sprites_group.add(my_wall)
        #End If
    #Next
#Next
for y in range(18):
    for x in range(35):
        if map[x][y] == 2:
            my_display = Display(BLACK, 40, 40, x*40, y *40)
            display_group.add(my_display)
            all_sprites_group.add(my_display)
        #End If
    #Next
#Next
for counter in range(enemy_number):
  enemy = Enemy(20, 20, random.randint(-3, 3), -3, wall_group)
  enemy.rect.x = (counter + 1) * 45
  enemy.rect.y = 660
  enemy_group.add(enemy)
  all_sprites_group.add(enemy)
#Next
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
  player_hit_list = pygame.sprite.spritecollide(player, wall_group, False)
  for foo in player_hit_list:
    player.rect.x = player_old_x
    player.rect.y = player_old_y
    player.speed_x = 0
    player.speed_y = 0
  #Next
  player_old_x = player.rect.x
  player_old_y = player.rect.y
  # -- Game logic goes after this comment
  bullet_hit_group = pygame.sprite.groupcollide(bullet_group, wall_group, dokilla=True, dokillb=False, collided=None)
  bullet_enemy_hit_group = pygame.sprite.groupcollide(bullet_group, enemy_group, dokilla=False, dokillb=True, collided=None)
  enemy_player_hit_group = pygame.sprite.spritecollide(player, enemy_group, True)
  player_boss_hit_group = pygame.sprite.groupcollide(player_group, boss_group, dokilla=False, dokillb=False, collided=None)
  boss_bullet_hit_group = pygame.sprite.groupcollide(boss_bullet_group, wall_group, dokilla=True, dokillb=False, collided=None)
  for foo in player_boss_hit_group:
    player.health = 0
  #Next
  if enemy_number < 1:
    if boss.health > 0:
      bullet_boss_hit_group = pygame.sprite.groupcollide(bullet_group, boss_group, dokilla=True, dokillb=False, collided=None)
      for foo in bullet_boss_hit_group:
        boss.health = boss.health - 1
      #Next
    #End If
  #End If
  if player.health > 0:
    boss_bullet_player_hit_group = pygame.sprite.groupcollide(boss_bullet_group, player_group, dokilla=True, dokillb=False, collided=None)
    for foo in boss_bullet_player_hit_group:
      if player.health > 0:
        player.health = player.health - 5
      #End If
    #Next
  #End If
  for foo in bullet_enemy_hit_group:
    enemy_number = enemy_number - 1
    if enemy_number == 0:
      boss = Boss(30, 30, 5, 0, wall_group, 200, 500)
      boss.rect.x = 40
      boss.rect.y = 40
      boss_group.add(boss)
      all_sprites_group.add(boss)
    #End If
  #Next
  for foo in enemy_player_hit_group:
    player.health = player.health - 5
    enemy_number = enemy_number - 1
    if enemy_number == 0:
      boss = Boss(30, 30, 5, 0, wall_group, 200, 500)
      boss.rect.x = 40
      boss.rect.y = 40
      boss_group.add(boss)
      all_sprites_group.add(boss)
    #End If
  #Next
  if enemy_number < 1:
    if boss.health < 1:
      all_sprites_group.remove(boss)
    #End If
  #End If
  if player.health < 1:
    all_sprites_group.remove(player)
  #End If
  enemyNumber = 'Enemies: ' + str(enemy_number)
  Health = 'Health: ' + str(player.health)
  Money = 'Money: ' + str(player.money)
  Keys = 'Keys: ' + str(player.keys)
  Score = 'Score: ' + str(player.score)
  Bullets = 'Bullets: ' + str(player.bullets)
  if enemy_number < 1:
    bossHealth = 'Boss Health: ' + str(boss.health)
    bossBullets = 'Boss Bullets: ' + str(boss.bullets)
  #End If
  all_sprites_group.update()
  # -- Screen background is BLACK
  screen.fill (screen_colour)
  # -- Draw here
  if player.health < 1:
    bigfont = pygame.font.SysFont('Calibri', 60, True, False)
    bigtext = bigfont.render('You Lose! Bad Luck Bruv!', True, BLACK)
    screen.blit(bigtext, [300, 320])
  elif enemy_number < 1 and boss.health < 1 and player.health > 0:
    bigfont = pygame.font.SysFont('Calibri', 60, True, False)
    bigtext = bigfont.render('Winner Winner Chicken Dinner!', True, BLACK)
    screen.blit(bigtext, [225, 320])
  else:
    all_sprites_group.draw (screen)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Health, True, WHITE)
    screen.blit(text, [1005, 10])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Money, True, WHITE)
    screen.blit(text, [1005, 40])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Keys, True, WHITE)
    screen.blit(text, [1005, 70])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Score, True, WHITE)
    screen.blit(text, [1005, 100])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(Bullets, True, WHITE)
    screen.blit(text, [1005, 130])
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render(enemyNumber, True, WHITE)
    screen.blit(text, [1005, 160])
    if enemy_number < 1:
      if boss.health > 0:
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(bossHealth, True, WHITE)
        screen.blit(text, [1005, 190])
        font = pygame.font.SysFont('Calibri', 25, True, False)
        text = font.render(bossBullets, True, WHITE)
        screen.blit(text, [1005, 220])
      #End If
    #End If
  #End If
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()
