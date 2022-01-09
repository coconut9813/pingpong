from pygame import*

window = display.set_mode((900, 700))
display.set_caption('pingpong')
background = transform.scale(image.load("space.jpg"),(900, 700))
mixer.init()
mixer.music.load('W.mp3')
mixer.music.play()
clock = time.Clock()
FPS = 60
font.init()
font = font.SysFont('Futura', 70)

class GaySprite(sprite.Sprite):
    def __init__(self, image1, x, y, speed, heigh, width):
        super().__init__()
        self.heigh = heigh
        self.width = width
        self.image = transform.scale(image.load(image1), (width, heigh))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def recet(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))

class Player(GaySprite):
    
    def update(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_s] and self.rect.y < 415:
            self.rect.y += self.speed

        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update2(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_DOWN] and self.rect.y < 415:
            self.rect.y += self.speed

        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

game = True
finish = False
player1 = Player('waaaaaaaaaa.png', 5, 250, 5, 280, 180)
player2 = Player('waaaaaaa2.png', 715, 250, 5, 280, 180)
#player2 = Player('ultramarine.png', 715, 250, 5, 280, 180)

while game:
    for e in event.get():
        if e.type == QUIT:
             game = False

    
    
    clock.tick(FPS)
    
    if finish != True:
        window.blit(background,(0, 0)) 
        player1.recet()
        player1.update()
        player2.recet()
        player2.update2()
    display.update() 

