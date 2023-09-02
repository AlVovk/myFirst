from pygame import *
win_width = 700
win_height = 500
run = True
finish = False #отвечает за то как кончилась игра
YELLOW = (222, 222, 11) 
window = display.set_mode((win_width, win_height))
display.set_caption('LABIRINT')
class GameSprite (sprite.Sprite):
    def __init__ (self, picture, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(picture),( w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player (GameSprite):
    def __init__ (self, player_image, player_w, player_h,player_x, player_y, speed_x, speed_y ):
        GameSprite.__init__(self, player_image, player_w, player_h,player_x, player_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        if player.rect.x <= win_width-80 and player.speed_x > 0 or player.rect.x >= 0 and player.speed_x < 0:
            self.rect.x += self.speed_x
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.speed_x > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left)
        elif self.speed_x < 0:
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 

        if player.rect.y <= win_height-110 and player.speed_y > 0 or player.rect.y >= 0 and player.speed_y < 0:
            self.rect.y += self.speed_y
player = Player('leonardo.png', 80, 100, 50, 50, 0, 0)
final = GameSprite ('exit.png', 100, 50,600, 50)


wall1 = GameSprite('wall1.png', 50, 100, 300, 100)
wall2 = GameSprite('wall1.png', 50, 100, 300,200)
wall3 = GameSprite('wall1.png', 50, 100, 300,150)
wall4 = GameSprite('wall1.png', 50, 100, 300,130)
wall5 = GameSprite('wall1.png', 50, 100, 300,180)
win = transform.scale(image.load('winner_1.jpg'), (700, 500))
#создаём группу для стен
barriers = sprite.Group()
#добавляем стены в группу
barriers.add(wall1)
barriers.add(wall2)
barriers.add(wall3)
barriers.add(wall4)
barriers.add(wall5)



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN: 
            if e.key == K_LEFT:
                player.speed_x = -5
            elif e.key == K_RIGHT:
                player.speed_x = 5
            elif e.key == K_UP:
                player.speed_y = -5
            elif e.key == K_DOWN:
                player.speed_y = 5
        elif e.type == KEYUP: #отжатие клавиши
            if e.key == K_UP:
                player.speed_y = 0
            elif e.key == K_DOWN:
                player.speed_y = 0
            elif e.key == K_LEFT:
                player.speed_x = 0
            elif e.key == K_RIGHT:
                player.speed_x = 0

    if not finish:
        window.fill(YELLOW)
        player.update()

        barriers.draw(window)#отрисовка группы стен
        player.reset()
        final.reset()
        if sprite.collide_rect(player, final):
            finish = True
            window.blit((win), (0, 0))
    time.delay(50)

    display.update()
