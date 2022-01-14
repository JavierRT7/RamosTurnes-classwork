from turtle import Screen
import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
# Create the snow variables
class Snow(pygame.sprite.Sprite):
    # Define the constructor for apple
    def __init__(self, x_ref, y_ref, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and load image
        self.image = pygame.Surface([10,10])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        # Set the position of the apple attributes
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
    #End Procedure
    # Update Function
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y >= 500:
            self.rect.y = random.randint(-100,0)
            self.rect.x = random.randint(0,700)
            self.speed = random.randint(1,3)
class House(pygame.sprite.Sprite):
    # Define the constructor for apple
    def __init__(self, x_ref, y_ref, colour):
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
    #End Procedure
    def update(self):
        if self.colour == GREEN:
            self.colour = RED
        else:
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
house = House(300, 400, GREEN)
all_sprites_group.add(house)
for count in range(1000):
    snowflake = Snow(random.randint(0,700), random.randint(-100,0), random.randint(1,3))
    all_sprites_group.add(snowflake)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    # --- Game logic should go here

    # --- Screen-clearing code goes here
    screen.fill(BLACK)
    all_sprites_group.update()
    all_sprites_group.draw(screen)
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    
 
    # --- Drawing code should go here
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()