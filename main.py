import pygame
import turtle
import random

WIDTH  = 1000
HEIGHT = 600
food_size = 10
delay = 100
SIZE   = (WIDTH, HEIGHT)
FPS = 9
score = 0

window = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
background = pygame.transform.scale(
                                    pygame.image.load("background-6360861_1280.png"),
                                    SIZE)
grid_size = 40
grid_width = WIDTH//grid_size
grid_height = HEIGHT//grid_size

pygame.font.init()
font_big = pygame.font.Font(None, 70)
font_medium = pygame.font.Font(None, 35)
font_small = pygame.font.Font(None, 15)


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, filename, size, coords):
        self.image = pygame.transform.scale(pygame.image.load(filename),size)
        self.rect = self.image.get_rect()
        self.rect.topleft = coords
        self.speed = 8

    def reset(self):
        window.blit(self.image, self.rect)

class Snake():
    def __init__(self) -> None:
          self.segments = [
          GameSprite("head.png", (grid_size, grid_size), (120,120))     
          ]
          self.direction = "right"
          self.grow = False
    def check_collisions(self):
        head = self.segments[0]
        for s in self.segments[1:]:
            if pygame.sprite.collide_rect(head, s):
                return True
        return False
    def move(self):
        head = self.segments[0]
        x,y = head.rect.topleft
        if self.direction == "right":
             x += grid_size
        elif self.direction == "left":
             x -= grid_size
        elif self.direction == "top":
             y -= grid_size
        elif self.direction == "bottom":
             y += grid_size
        
        if self.grow:
            new_head = GameSprite("head.png", (grid_size, grid_size), (x,y))
            self.segments[0].image = pygame.transform.scale(
                pygame.image.load("body.png"), self.segments[0].rect.size
            )
            self.segments.insert(0, new_head)
            self.grow = False

        else: 
            for i in range(len(self.segments)-1, 0, -1):
                self.segments[i].rect.topleft = self.segments[i-1].rect.topleft
            head.rect.topleft = x,y


class Food(GameSprite):
    def update(self):
        self.rect.x = random.randint(40, WIDTH-100)
        self.rect.y = random.randint(40, HEIGHT-100)
        global score 
        score += 1

class Enemy(GameSprite):
    def update(self):
        self.rect.x = random.randint(20, 600)
        self.rect.y = random.randint(20, 600)
        global score
        score -= 1



# class Player(GameSprite):
#     def update(self):
#         keys = pygame.key.get_pressed()

#         if keys[pygame.K_UP] or keys [pygame.K_w] and self.rect.top > 0:
#                 self.rect.y -= self.speed
#         if keys[pygame.K_s] or keys [pygame.K_DOWN] and self.rect.top < HEIGHT:
#                 self.rect.y += self.speed
#         if keys[pygame.K_d] or keys [pygame.K_RIGHT] and self.rect.right < WIDTH:
#                 self.rect.x += self.speed
#         if keys[pygame.K_a] or keys [pygame.K_LEFT] and self.rect.left > 0:
#                 self.rect.x -= self.speed

x = random.randint(20,WIDTH-20)
y = random.randint(10, HEIGHT-10)


snake = Snake()
apple = Food("apple-439397_1280.png", (100,100), (x,y))

text_score = font_medium.render("Рахунок:" + str(score), True, (255,255,255))

game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and snake.direction != "bottom":
                snake.direction = "top"
            if event.key == pygame.K_s and snake.direction != "top":
                snake.direction = "bottom"
            if event.key == pygame.K_a and snake.direction != "right":
                snake.direction = "left"
            if event.key == pygame.K_d and snake.direction != "left":
                snake.direction = "right"

    window.blit(background, (0,0))
    snake.move()
    for i in snake.segments:
         i.reset()
    apple.reset()
    text_score = font_medium.render("Рахунок:" + str(score), True, (0,0,255))
    window.blit(text_score, (0,0))
    if pygame.sprite.collide_rect(apple, snake.segments[0]): 
        apple.update()
        snake.grow = True
    if snake.check_collisions():
        game_over = True
    pygame.display.update()
    clock.tick(FPS)