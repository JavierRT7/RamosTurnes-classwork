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
x_direction = -2
y_direction = -2
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20
padd_collision = x_padd + 7.5
padd_collision_y1 = y_padd + 30
padd_collision_y2 = y_padd - 30
ai_length = 15
ai_width = 60
x_ai = 625
y_ai = 20
ai_collision = x_ai + 7.5
ai_collision_y1 = y_ai + 30
ai_collision_y2 = y_ai - 30
ai_direction = 2
colour = BLACK
winner = '.'
score = 'Score: 0'
score_int = 0
score2 = 'Score: 0'
score2_int = 0
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
    ### SRC - You can fix this by not including this in the for loop!
  if keys[pygame.K_UP]:
        y_padd = y_padd - 5
        padd_collision_y1 = y_padd + 30
        padd_collision_y2 = y_padd - 30
  if keys[pygame.K_DOWN]:
        y_padd = y_padd + 5
        padd_collision_y1 = y_padd + 30
        padd_collision_y2 = y_padd - 30
  #Next event
  # -- Game logic goes after this comment
  if x_val < 8:  ### SRC - It might not be equal, especially if you make the ball go faster.
    if y_val < padd_collision_y1:
      if y_val > padd_collision_y2:
        x_direction = 3
        if y_direction == 2:
          y_direction = 3
        #End If
        if y_direction == -2:
          y_direction = -3
        #End If  
      #End If
    #End If
  #End If
  if x_val > 617:  ### SRC - It might not be equal, especially if you make the ball go faster.
    if y_val < ai_collision_y1:
      if y_val > ai_collision_y2:
        x_direction = -3
      #End If
    #End If
  #End If
  if y_direction > 0:
      ai_direction = 2
  #End If
  if y_direction < 0:
      ai_direction = -2
  #End If
  if y_ai > 460:
      ai_direction = -2
  #End If
  if y_ai < 0:
      ai_direction = 2
  #End If
  if x_val > 640:
      x_direction = 2
      x_val = 320
      y_val = 200
      score_int = score_int + 1
      #End If
  if x_val < -10:
      x_direction = -2
      x_val = 320
      y_val = 200
      score2_int = score2_int + 1
      #End If
  if y_val < 0:
      y_direction = 2
      #End If
  if y_val > 480:
      y_direction = -2
      #End if
  if score_int == 1:
      score = 'Score: 1'
      #End If
  if score_int == 2:
      score = 'Score: 2'
      #End If
  if score_int == 3:
      score = 'Score: 3'
      #End If
  if score_int == 4:
      score = 'Score: 4'
      #End If
  if score_int == 5:
      score = 'Score: 5'
      winner = 'Player Wins!'
      colour = WHITE
      #End If
  if score2_int == 1:
      score2 = 'Score: 1'
      #End If
  if score2_int == 2:
      score2 = 'Score: 2'
      #End If
  if score2_int == 3:
      score2 = 'Score: 3'
      #End If
  if score2_int == 4:
      score2 = 'Score: 4'
      #End If
  if score2_int == 5:
      score2 = 'Score: 5'
      winner = 'Computer Wins!'
      colour = WHITE
      #End If
  x_val = x_val + x_direction
  y_val = y_val + y_direction
  y_ai = y_ai + ai_direction
  ai_collision_y1 = y_ai + 26
  ai_collision_y2 = y_ai - 26
  # -- Screen background is BLACK
  screen.fill (BLACK)
  # -- Draw here
  pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,ball_width))
  pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
  pygame.draw.rect(screen, YELLOW, (x_ai, y_ai, ai_length, ai_width))
  font = pygame.font.SysFont('Calibri', 25, True, False)
  text = font.render(score, True, WHITE)
  screen.blit(text, [10, 10])
  font = pygame.font.SysFont('Calibri', 25, True, False)
  text = font.render(score2, True, WHITE)
  screen.blit(text, [550, 10])
  font = pygame.font.SysFont('Calibri', 60, True, False)
  text = font.render(winner, True, colour)
  screen.blit(text, [200, 240])
  # -- flip display to reveal new position of objects
  pygame.display.flip()
  # - The clock ticks over
  clock.tick(60)
#End While - End of game loop
pygame.quit()
