from turtle import Screen
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (105,105,105)
# Create the snow variables
class Snow(pygame.sprite.Sprite):
    # Define the constructor for apple
    def __init__(self, x_ref, y_ref, speed, speed_x, colour):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and load image
        self.image = pygame.Surface([10,10])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        # Set the position of the apple attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.speed_x = speed_x
    #End Procedure
    # Update Function
    def update(self):
        self.rect.y = self.rect.y + self.speed
        self.rect.x = self.rect.x + self.speed_x
        if self.rect.y > 500:
            self.rect.y = random.randint(-100,-10)
            self.rect.x = random.randint(0,700)
            self.speed = random.randint(1,3)
        if self.rect.x > 700:
            self.speed_x = random.randint(-2,-1)
        if self.rect.x <= -10:
            self.speed_x = random.randint(1,2)
        if self.speed_x == 0:
            self.speed_x = random.randint(-2,2)
class House(pygame.sprite.Sprite):
    # Define the constructor for apple
    def __init__(self, x_ref, y_ref, colour, count):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and load image
        self.image = pygame.Surface([80,100])
        self.colour = colour
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        # Set the position of the apple attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.count = count
    #End Procedure
    def update(self):
        self.count = self.count + 1
        if self.colour == GREEN and self.count % 30 == 0:
            self.colour = RED
        elif self.count % 30 == 0:
            self.colour = GREEN
        self.image.fill(self.colour)
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Snow")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
all_sprites_group = pygame.sprite.Group()
snow_group = pygame.sprite.Group()
dark_snow_group = pygame.sprite.Group()
house_group = pygame.sprite.Group()
house = House(300, 400, GREEN, 0)
house_group.add(house)
all_sprites_group.add(house)
count = 0
for count in range(10):
    if count % 2 == 0:
        snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), WHITE)
        all_sprites_group.add(snowflake)
        snow_group.add(snowflake)
    else:
        snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), GREY)
        all_sprites_group.add(snowflake)
        dark_snow_group.add(snowflake)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here
    if count < 1000:
        if count % 2 == 0:
            snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), WHITE)
            all_sprites_group.add(snowflake)
            snow_group.add(snowflake)
        else:
            snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), GREY)
            all_sprites_group.add(snowflake)
            dark_snow_group.add(snowflake)
    count = count + 1
    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    all_sprites_group.update()
    dark_snow_group.draw(screen)
    house_group.draw(screen)
    snow_group.draw(screen)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
 
    # --- Drawing code should go here
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(30)
 
# Close the window and quit.
pygame.quit()