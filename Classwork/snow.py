from turtle import Screen
import pygame
import random
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
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
            if floor.rect.y > 0 and self.count % 3 == 0:
                floor.rect.y = floor.rect.y - 1
        if self.rect.x > 700:
            self.speed_x = random.randint(-2,-1)
        if self.rect.x <= -10:
            self.speed_x = random.randint(1,2)
        if self.speed_x == 0:
            self.speed_x = random.randint(-2,2)
        self.count = self.count + 1
class House(pygame.sprite.Sprite):
    def __init__(self, x_ref, y_ref, colour, count):
        super().__init__()
        self.image = pygame.Surface([80,100])
        self.colour = colour
        self.image.fill(self.colour)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        self.count = count
    def update(self):
        self.count = self.count + 1
        if self.colour == GREEN and self.count % 30 == 0:
            self.colour = RED
        elif self.count % 30 == 0:
            self.colour = GREEN
        self.image.fill(self.colour)
class Floor(pygame.sprite.Sprite):
    def __init__(self, x_ref, y_ref):
        super().__init__()
        self.image = pygame.Surface([700,500])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")
done = False
clock = pygame.time.Clock()
all_sprites_group = pygame.sprite.Group()
snow_group = pygame.sprite.Group()
dark_snow_group = pygame.sprite.Group()
house_group = pygame.sprite.Group()
house = House(300, 400, GREEN, 0)
house_group.add(house)
all_sprites_group.add(house)
floor = Floor(0,500)
snow_group.add(floor)
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
    if count < 1000:
        if count % 2 == 0:
            snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), WHITE)
            all_sprites_group.add(snowflake)
            snow_group.add(snowflake)
        else:
            snowflake = Snow(random.randint(0,700), random.randint(-100,-10), random.randint(1,3), random.randint(-2,2), GREY)
            all_sprites_group.add(snowflake)
            dark_snow_group.add(snowflake)
    if floor.rect.y == 0:
        snow_group.remove(floor)
    count = count + 1
    screen.fill(BLACK)
    all_sprites_group.update()
    dark_snow_group.draw(screen)
    house_group.draw(screen)
    snow_group.draw(screen)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()