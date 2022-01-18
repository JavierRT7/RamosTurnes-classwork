from turtle import Screen
import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (105,105,105)
class Snow(pygame.sprite.Sprite):
    def __init__(self, x_ref, y_ref, speed, speed_x, colour):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.speed = speed
        self.speed_x = speed_x
        self.count = 0
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
        self.count = self.count + 1
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False
clock = pygame.time.Clock()
all_sprites_group = pygame.sprite.Group()
snow_group = pygame.sprite.Group()
dark_snow_group = pygame.sprite.Group()
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
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if count < 100000000000000000:
        if count % 2 == 0:
            snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), WHITE)
            all_sprites_group.add(snowflake)
            snow_group.add(snowflake)
        else:
            snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), GREY)
            all_sprites_group.add(snowflake)
            dark_snow_group.add(snowflake)
    count = count + 1
    screen.fill(BLACK)
    all_sprites_group.update()
    dark_snow_group.draw(screen)
    snow_group.draw(screen)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()