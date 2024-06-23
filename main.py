import pygame
import turtle
import random

WIDTH  = 1000
HEIGHT = 600
food_size = 10
delay = 100
SIZE   = (WIDTH, HEIGHT)
FPS = 60
score = 0

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(
                                    pygame.image.load("test_background.png"),
                                    SIZE)

pygame.font.init()
font_big = pygame.font.Font(None, 70)
font_medium = pygame.font.Font(None, 35)
font_small = pygame.font.Font(None, 15)

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
        self.rect.x = random.randint(20, 600)
        self.rect.y = random.randint(20, 600)
        global score 
        score += 1

class Enemy(GameSprite):
     def update(self):
          self.rect.x = random.randint(20, 600)
          self.rect.y = random.randint(20, 600)
          global score
          score -= 1

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
    text_score = font_medium.render("Рахунок:" + str(score), True, (0,0,255))
    window.blit(text_score, (0,0))
    if pygame.sprite.collide_rect(food, player): 
        food.update()
    pygame.display.update()
    clock.tick(FPS)