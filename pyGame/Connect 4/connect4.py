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
size = (840,720)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Connect 4")

#Classes
class Piece(pygame.sprite.Sprite):
    # Define the constructor for brick
    def __init__(self, x_ref, y_ref, image):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and load image
        self.image = image
        self.rect = self.image.get_rect()
        # Set the position of the brick attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
    #End Procedure
#End Class

#Sprite Groups
all_sprites_group = pygame.sprite.Group()

#Globals
player1 = pygame.image.load('player1.jpg')
player2 = pygame.image.load('player2.jpg')
y_1 = 600
y_2 = 600
y_3 = 600
y_4 = 600
y_5 = 600
y_6 = 600
y_7 = 600
turn = 1
map = [[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],
[0,0,0,0,0,0],]
win1 = False
win2 = False

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
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            if y_1 >= 0:
                if turn == 1:
                    piece = Piece(0, y_1, player1)
                    all_sprites_group.add(piece)
                    map[0][(600-y_1)//120] = 1
                    turn = 2
                elif turn == 2:
                    piece = Piece(0, y_1, player2)
                    all_sprites_group.add(piece)
                    map[0][(600-y_1)//120] = 2
                    turn = 1
                #End If
                y_1 = y_1 - 120
        elif event.key == pygame.K_2:
            if y_2 >= 0:
                if turn == 1:
                    piece = Piece(120, y_2, player1)
                    all_sprites_group.add(piece)
                    map[1][(600-y_2)//120] = 1
                    turn = 2
                elif turn == 2:
                    piece = Piece(120, y_2, player2)
                    all_sprites_group.add(piece)
                    map[1][(600-y_2)//120] = 2
                    turn = 1
                #End If
                y_2 = y_2 - 120
        elif event.key == pygame.K_3:
            if y_3 >= 0:
                if turn == 1:
                    piece = Piece(240, y_3, player1)
                    map[2][(600-y_3)//120] = 1
                    all_sprites_group.add(piece)
                    turn = 2
                elif turn == 2:
                    piece = Piece(240, y_3, player2)
                    all_sprites_group.add(piece)
                    map[2][(600-y_3)//120] = 2
                    turn = 1
                #End If
                y_3 = y_3 - 120
        elif event.key == pygame.K_4:
            if y_4 >= 0:
                if turn == 1:
                    piece = Piece(360, y_4, player1)
                    all_sprites_group.add(piece)
                    map[3][(600-y_4)//120] = 1
                    turn = 2
                elif turn == 2:
                    piece = Piece(360, y_4, player2)
                    all_sprites_group.add(piece)
                    map[3][(600-y_4)//120] = 2
                    turn = 1
                #End If
                y_4 = y_4 - 120
        elif event.key == pygame.K_5:
            if y_5 >= 0:
                if turn == 1:
                    piece = Piece(480, y_5, player1)
                    all_sprites_group.add(piece)
                    map[4][(600-y_5)//120] = 1
                    turn = 2
                elif turn == 2:
                    piece = Piece(480, y_5, player2)
                    all_sprites_group.add(piece)
                    map[4][(600-y_5)//120] = 2
                    turn = 1
                #End If
                y_5 = y_5 - 120
        elif event.key == pygame.K_6:
            if y_6 >= 0:
                if turn == 1:
                    piece = Piece(600, y_6, player1)
                    all_sprites_group.add(piece)
                    map[5][(600-y_6)//120] = 1
                    turn = 2
                elif turn == 2:
                    piece = Piece(600, y_6, player2)
                    all_sprites_group.add(piece)
                    map[5][(600-y_6)//120] = 2
                    turn = 1
                #End If
                y_6 = y_6 - 120
        elif event.key == pygame.K_7:
            if y_7 >= 0:
                if turn == 1:
                    piece = Piece(720, y_7, player1)
                    all_sprites_group.add(piece)
                    map[6][(600-y_7)//120] = 1
                    turn = 2
                elif turn == 2:
                    piece = Piece(720, y_7, player2)
                    all_sprites_group.add(piece)
                    map[6][(600-y_7)//120] = 2
                    turn = 1
                #End If
                y_7 = y_7 - 120
        #End If
    #End If
  #Next event
  for counter in range(6):
    number1 = 0
    number2 = 0
    for count in range(7):
        if map[count][counter] == 0:
            number1 = 0
            number2 = 0
        if map[count][counter] == 1:
            number1 = number1 + 1 
            number2 = 0
            if number1 == 4 or number2 == 4:
                win1 = True
        if map[count][counter] == 2:
            number1 = 0
            number2 = number2 + 1
            if number1 == 4 or number2 == 4:
                win2 = True
  for counter in range(7):
    number1 = 0
    number2 = 0
    for count in range(6):
        if map[counter][count] == 0:
            number1 = 0
            number2 = 0
        if map[counter][count] == 1:
            number1 = number1 + 1 
            number2 = 0
            if number1 == 4 or number2 == 4:
                win1 = True
        if map[counter][count] == 2:
            number1 = 0
            number2 = number2 + 1
            if number1 == 4 or number2 == 4:
                win2 = True  
  number1 = 0
  number2 = 0
  for count in range(4):
    if map[count + 3][count] == 0:
        number1 = 0
        number2 = 0
    if map[count + 3][count] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count + 3][count] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True
  number1 = 0
  number2 = 0
  for count in range(5):
    if map[count + 2][count] == 0:
        number1 = 0
        number2 = 0
    if map[count + 2][count] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count + 2][count] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True
  number1 = 0
  number2 = 0
  for count in range(6):
    if map[count + 1][count] == 0:
        number1 = 0
        number2 = 0
    if map[count + 1][count] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count + 1][count] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
  number1 = 0
  number2 = 0
  for count in range(6):
    if map[count][count] == 0:
        number1 = 0
        number2 = 0
    if map[count][count] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count][count] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
  number1 = 0
  number2 = 0
  for count in range(5):
    if map[count][count + 1] == 0:
        number1 = 0
        number2 = 0
    if map[count][count + 1] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count][count + 1] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True    
  number1 = 0
  number2 = 0
  for count in range(4):
    if map[count][count + 2] == 0:
        number1 = 0
        number2 = 0
    if map[count][count + 2] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count][count + 2] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True    
  number1 = 0
  number2 = 0
  counter = 3
  for count in range(4):
    if map[count][counter] == 0:
        number1 = 0
        number2 = 0
    if map[count][counter] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count][counter] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
    counter = counter - 1
  number1 = 0
  number2 = 0
  counter = 4
  for count in range(5):
    if map[count][counter] == 0:
        number1 = 0
        number2 = 0
    if map[count][counter] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count][counter] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
    counter = counter - 1          
  number1 = 0
  number2 = 0
  counter = 5
  for count in range(6):
    if map[count][counter] == 0:
        number1 = 0
        number2 = 0
    if map[count][counter] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count][counter] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
    counter = counter - 1  
  number1 = 0
  number2 = 0
  counter = 5
  for count in range(6):
    if map[count + 1][counter] == 0:
        number1 = 0
        number2 = 0
    if map[count + 1][counter] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count + 1][counter] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
    counter = counter - 1 
  number1 = 0
  number2 = 0
  counter = 5
  for count in range(5):
    if map[count + 2][counter] == 0:
        number1 = 0
        number2 = 0
    if map[count + 2][counter] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count + 2][counter] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
    counter = counter - 1       
  number1 = 0
  number2 = 0
  counter = 5
  for count in range(4):
    if map[count + 3][counter] == 0:
        number1 = 0
        number2 = 0
    if map[count + 3][counter] == 1:
        number1 = number1 + 1
        number2 = 0
        if number1 == 4 or number2 == 4:
                win1 = True
    if map[count + 3][counter] == 2:
        number1 = 0
        number2 = number2 + 1
        if number1 == 4 or number2 == 4:
                win2 = True  
    counter = counter - 1                                 
  # -- Game logic goes after this comment 
  # -- Screen background is BLACK
  screen.fill (WHITE)
  # -- Draw here
  all_sprites_group.draw(screen)
  pygame.draw.rect(screen, BLACK, (0, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (120, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (240, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (360, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (480, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (600, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (720, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (840, 0, 1, 720))
  pygame.draw.rect(screen, BLACK, (0, 0, 840, 1))
  pygame.draw.rect(screen, BLACK, (0, 120, 840, 1))
  pygame.draw.rect(screen, BLACK, (0, 240, 840, 1))
  pygame.draw.rect(screen, BLACK, (0, 360, 840, 1))  
  pygame.draw.rect(screen, BLACK, (0, 480, 840, 1))
  pygame.draw.rect(screen, BLACK, (0, 600, 840, 1))
  pygame.draw.rect(screen, BLACK, (0, 720, 840, 1))
  if win1 == True:
    pygame.draw.rect(screen, BLACK, (0, 0, 840, 720))
    font = pygame.font.SysFont('ComicSans', 100, True, False)
    text = font.render('Player 1 Wins!', True, WHITE)
    screen.blit(text, [65, 300])
  elif win2 == True:
    pygame.draw.rect(screen, BLACK, (0, 0, 840, 720))
    font = pygame.font.SysFont('ComicSans', 100, True, False)
    text = font.render('Player 2 Wins!', True, WHITE)
    screen.blit(text, [65, 300])  
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()