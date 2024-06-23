import pygame
import turtle
import random

WIDTH  = 1000
HEIGHT = 600
food_size = 10
delay = 100
SIZE   = (WIDTH, HEIGHT)
FPS = 60

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(
                                    pygame.image.load("test_background.png"),
                                    SIZE)

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect = self.image.get_rect()
        self.rect.center = coords
        self.speed = 8

    def reset(self):
        window.blit(self.image, self.rect)

class Food(GameSprite):
    def update(self):
        ...

class Player(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] or keys [pygame.K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
        if keys[pygame.K_s] or keys [pygame.K_DOWN] and self.rect.top < HEIGHT:
                self.rect.y += self.speed
        if keys[pygame.K_d] or keys [pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.speed
        if keys[pygame.K_a] or keys [pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed


player = Player("test_image.png", (100,100), (100,100))
food = Food("test_food.png", (100,100), (random.randint(20, 600),random.randint(20, 600)))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    window.blit(background, (0,0))
    player.reset()
    player.update()
    food.reset()
    if pygame.sprite.collide_rect(food, player): 
        food.update()
    pygame.display.update()
    clock.tick(FPS)