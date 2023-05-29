#Пинг-понг
from pygame import *

window = display.set_mode((700,500))
display.set_caption('Пинг-понг')
col = (200, 255, 153)

class  GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player (GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += speed

racket1 = Player('racket.png', 30, 200, 50, 200, 150)
racket2 = Player('racket.png', 620, 200, 50, 200, 150)
ball = GameSprite('1_1735.png', 200, 200, 70, 70, 50)
speed = 2
speed_x = 3
speed_y = 3
game = True
finish = False
clock = time.Clock()
FPS = 60
font.init()
font = font.Font(None, 30)
lose1 = font.render("Игрок 1 проиграл", True,(180,0,0))
lose2 = font.render("Игрок 2 проиграл",True,(180,0,0))
#задай фон сцены
while game:
    #обработай событие «клик по кнопке "Закрыть окно"»
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(col)
        racket1.reset()
        racket2.reset()
        ball.reset()
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y > 450 or ball.rect.y< 0:
            speed_y *= -1
        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
        if ball.rect.x < 0:
            filter=True
            window.blit(lose1, (200, 200))
            game = False
        if ball.rect.x > 700:
            filter=True
            window.blit(lose2, (200, 200))
            game = False
    display.update()
    clock.tick(FPS)