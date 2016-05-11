import pygame
import math
import random

class Walls(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall.bmp")#pygame.Surface([width, height])
        #self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
class Player:
    def refresh_color(self):
        """Set color(it depens on the module of Player speed)"""
        self.color = max(0, int(math.sqrt(self.vx ** 2
            + self.vy ** 2)) + 100)

    def __init__(self,  x = 100, y = 100, vx = 0, vy = 0, a = 500, pos = 'u', x_bul=0, y_bul=0, r_bul = 2):
        """Constructor of Player class"""
        
        self.x, self.y, self.vx, self.vy, self.a, self.pos, self.r_bul = \
                x, y, vx, vy, a, pos, r_bul
        self.tank = Block((0,255,255), 28, 28)
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.tank)
        self.x = 100
        self.y = 100
        self.tank.rect.x = self.x
        self.tank.rect.y = self.y
        self.refresh_color()

    def update(self, game):
        """Update Player state"""
        """  game.block_hit_list = pygame.sprite.spritecollide(self.tank, game.block_list, False)
        
        if len(game.block_hit_list) > 0:
            self.vx = 0
            self.vy = 0
            game.block_hit_list = [] """
        
        if game.pressed[pygame.K_LEFT]:
            if self.pos == 'u':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 90)
                self.pos = 'l'
            if self.pos == 'r':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 180)
                self.pos = 'l'
            if self.pos == 'd':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, -90)
                self.pos = 'l'
            self.vx = -200
            
            #self.vx -= game.delta * self.a
        if game.pressed[pygame.K_RIGHT]:
            if self.pos == 'u':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, -90)
                self.pos = 'r'
            if self.pos == 'l':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 180)
                self.pos = 'r'
            if self.pos == 'd':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 90)
                self.pos = 'r'
            self.vx = 200
            
            #self.vx += game.delta * self.a
            
        if game.pressed[pygame.K_UP]:
            if self.pos == 'r':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 90)
                self.pos = 'u'
            if self.pos == 'l':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, -90)
                self.pos = 'u'
            if self.pos == 'd':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 180)
                self.pos = 'u'
            self.vy = -200
            
            #self.vy -= game.delta * self.a
            
        if game.pressed[pygame.K_DOWN]:
            if self.pos == 'r':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, -90)
                self.pos = 'd'
            if self.pos == 'l':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 90)
                self.pos = 'd'
            if self.pos == 'u':
                game.tank_image_up = pygame.transform.rotate(game.tank_image_up, 180)
                self.pos = 'd'
            self.vy = 200
            
            #self.vy += game.delta * self.a
          
        game.block_hit_list = pygame.sprite.spritecollide(self.tank, game.block_list, False)
        if len(game.block_hit_list) > 0:
            #print(1)
            self.vx = 0
            self.vy = 0
            if self.pos == 'l':
                self.x = self.x + 2
            if self.pos == 'r':
                self.x = self.x -2
            
            game.block_hit_list = []
        (self.vx) -= (game.delta * self.vx * 10)
        (self.vy) -= (game.delta * self.vy * 10)
        self.x += self.vx * game.delta
        self.y += self.vy * game.delta
        self.tank.rect.x = self.x
        self.tank.rect.y = self.y
        
        #print(self.vy)
        #print(self.tank.rect.y)
        #self.x += self.vx * game.delta
        #self.y += self.vy * game.delta
        #if game.pressed[pygame.K_SPACE]:
            #self.x_bul = self.x
            #self.y_bul = self.y
        """Do not let Player get out of the Game window"""
        if self.tank.rect.x < 15:
            if self.vx < 0:
                self.vx = 0
            self.tank.rect.x = 15
            #self.x = self.rect_x
        if self.tank.rect.y < 15:
            if self.vy < 0:
                self.vy = 0
            self.tank.rect.y = 15
            #self.y = 15
        if self.tank.rect.x > (game.width - 18):
            if self.vx > 0:
                self.vx = 0
            self.tank.rect.x = game.width - 18
            #self.x = game.width - 18
        if self.tank.rect.y > (game.height - 13):#self.r:
            if self.vy > 0:
                self.vy = 0
            self.tank.rect.y = game.height - 13
            #self.y = game.height - 13#self.r


       # self.refresh_color()

    def render(self, game):
        """Draw Player on the Game window"""
        #self.player_list.draw(game.screen)
        #pygame.image.load("tanks.bmp") 
        #pygame.draw.circle(game.screen,
                #(self.color, self.color, self.color),
                #(int(self.x), int(self.y)), self.r)

class Game:
    def tick(self):
        """Return time in seconds since previous call
        and limit speed of the game to 50 fps"""
        self.delta = self.clock.tick(50) / 1000.0
        

    def __init__(self):
        """Constructor of the Game"""
        self._running = True
        self.size = self.width, self.height = 640, 400
        # create main display - 640x400 window
        # try to use hardware acceleration
        #self.screen = pygame.display.set_mode(((width +margin)*n+margin,(height+margin)*n+margin))# создаём окно
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        # set window caption
        pygame.display.set_caption('Tanks')
        self.space = pygame.image.load('space.bmp')
        
        # get object to help track time
        self.clock = pygame.time.Clock()
        # set default tool
        self.tool = 'run'
        self.player = Player()
        #self.ar = pygame.PixelArray(self.screen)
        self.tank_image_up = pygame.image.load('tanks_up.bmp')
        self.block_list = pygame.sprite.Group()
        i = 0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 0#random.randrange(self.width)
            self.block.rect.y = i#random.randrange(self.height)
            self.block_list.add(self.block)
            i = i + 10
            if not i <= 400:
                break
        k = 0    
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = self.width - 40#random.randrange(self.width)
            self.block.rect.y = k#random.randrange(self.height)
            self.block_list.add(self.block)
            k = k + 10
            if not k <= 400:
                break
        
        

    def event_handler(self, event):
        """Handling one pygame event"""
        if event.type == pygame.QUIT:
            # close window event
            self.exit()
        elif event.type == pygame.KEYDOWN:
            # keyboard event on press ESC
            if event.key == pygame.K_ESCAPE:
                self.exit()

    def move(self):
        """Here game objects update their positions"""
        self.tick()
        self.pressed = pygame.key.get_pressed()

        self.player.update(self)

    def render(self):
        """Render the scene"""
        #self.screen.fill((255, 0, 0))
        self.screen.blit(self.space, (0,0))
        self.player.render(self)
        self.tank_image_up.set_colorkey((0,0,0))
        self.screen.blit(self.tank_image_up, ((self.player.tank.rect.x -5 ), (self.player.tank.rect.y - 5)))
        #self.screen.blit(self.tank_image_up, ((self.player.x), (self.player.y)))
        pygame.draw.rect(self.screen, (255, 0, 0), ((0,0),(20,20)), 0) 
        #self.ar[int(self.player.x/10.0),int(self.player.y/10.0)] = (200,200,200)
        self.block_list.draw(self.screen)
        pygame.display.flip()

    def exit(self):
        """Exit the game"""
        self._running = False

    def cleanup(self):
        """Cleanup the Game"""
        pygame.quit()

    def execute(self):
        """Execution loop of the game"""
        while(self._running):
            # get all pygame events from queue
            for event in pygame.event.get():
                self.event_handler(event)
            self.move()
            self.render()
        self.cleanup()

if __name__ == "__main__":
    game = Game()
    game.execute()
