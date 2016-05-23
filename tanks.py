import pygame
import math
import random

class Walls(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("wall.bmp")
        #self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
class Proof_Walls(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("proof_wall.bmp")

        self.rect = self.image.get_rect()
class Grace(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("grace.bmp")
        self.image.set_colorkey((0,0,0))

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

    def __init__(self,  x = 300, y = 400, vx = 0, vy = 0, a = 500, pos = 'u', x_bul=0, y_bul=0, r_bul = 2):
        """Constructor of Player class"""
        
        self.x, self.y, self.vx, self.vy, self.a, self.pos, self.r_bul = \
                x, y, vx, vy, a, pos, r_bul
        self.tank = Block((0,255,255), 28, 28)
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.tank)
        self.x = 300
        self.y = 350
        self.tank.rect.x = self.x
        self.tank.rect.y = self.y
        self.refresh_color()

    def update(self, game):
        """Update Player state"""

        
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

          
        game.block_hit_list = pygame.sprite.spritecollide(self.tank, game.block_list, False)
        if len(game.block_hit_list) > 0:
            
            self.vx = 0
            self.vy = 0
            if self.pos == 'l':
                self.x = self.x + 2
            if self.pos == 'r':
                self.x = self.x -2
            if self.pos == 'd':
                self.y = self.y -2
            if self.pos == 'u':
                self.y = self.y + 2
            
            game.block_hit_list = []
        game.opp_player_hit_list = pygame.sprite.spritecollide(self.tank, game.opposite_player.player_list, False)
        if len(game.opp_player_hit_list) > 0:
            self.vx = 0
            game.opposite_player.vx = 0
            game.opposite_player.vy = 0
            self.vy = 0
            if (self.pos == 'l') and (game.opposite_player.pos == 'l') and (self.x >= game.opposite_player.x):
                self.x = self.x + 2
                game.opposite_player.x = game.opposite_player.x - 2
                
            if self.pos == 'l':
                self.x = self.x + 2
                
            if (self.pos == 'r') and (game.opposite_player.pos == 'r') and (self.x <= game.opposite_player.x):
                self.x = self.x -2
                game.opposite_player.x = game.opposite_player.x + 2
                
            if self.pos == 'r':
                self.x = self.x -2
                game.opp_player_hit_list = []
            if (self.pos == 'd') and (game.opposite_player.pos == 'd') and (self.y <= game.opposite_player.y):
                self.y = self.y - 2
                game.opposite_player.y = game.opposite_player.y + 2

            if (self.pos == 'u') and (game.opposite_player.pos == 'u') and (self.y >= game.opposite_player.y):
                self.y = self.y + 2
                game.opposite_player.y = game.opposite_player.y -2

            game.opp_player_hit_list = []
        (self.vx) -= (game.delta * self.vx * 10)
        (self.vy) -= (game.delta * self.vy * 10)
        self.x += self.vx * game.delta
        self.y += self.vy * game.delta
        self.tank.rect.x = self.x
        self.tank.rect.y = self.y
        

        """Do not let Player get out of the Game window"""
        if self.tank.rect.x < 15:
            if self.vx < 0:
                self.vx = 0
            self.tank.rect.x = 15
            
        if self.tank.rect.y < 15:
            if self.vy < 0:
                self.vy = 0
            self.tank.rect.y = 15
            
        if self.tank.rect.x > (game.width - 18):
            if self.vx > 0:
                self.vx = 0
            self.tank.rect.x = game.width - 18
           
        if self.tank.rect.y > (game.height - 13):
            if self.vy > 0:
                self.vy = 0
            self.tank.rect.y = game.height - 13


    def render(self, game):
        """Draw Player on the Game window"""



class OpponentPlayer:
    def refresh_color(self):
        """Set color(it depens on the module of Player speed)"""
        self.color = max(0, int(math.sqrt(self.vx ** 2
            + self.vy ** 2)) + 100)

    def __init__(self,  x = 300, y = 400, vx = 0, vy = 0, a = 500, pos = 'u', x_bul=0, y_bul=0, r_bul = 2):
        """Constructor of Player class"""
        
        self.x, self.y, self.vx, self.vy, self.a, self.pos, self.r_bul = \
                x, y, vx, vy, a, pos, r_bul
        self.tank = Block((0,255,255), 28, 28)
        self.player_list = pygame.sprite.Group()
        self.player_list.add(self.tank)
        self.x = 350
        self.y = 350
        self.tank.rect.x = self.x
        self.tank.rect.y = self.y
        self.refresh_color()

    def update(self, game):
        """Update Player state"""
        
        if game.pressed[pygame.K_a]:
            if self.pos == 'u':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 90)
                self.pos = 'l'
            if self.pos == 'r':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 180)
                self.pos = 'l'
            if self.pos == 'd':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, -90)
                self.pos = 'l'
            self.vx = -200
            
            
        if game.pressed[pygame.K_d]:
            if self.pos == 'u':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, -90)
                self.pos = 'r'
            if self.pos == 'l':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 180)
                self.pos = 'r'
            if self.pos == 'd':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 90)
                self.pos = 'r'
            self.vx = 200
            
            
            
        if game.pressed[pygame.K_w]:
            
            if self.pos == 'r':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 90)
                self.pos = 'u'
            if self.pos == 'l':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, -90)
                self.pos = 'u'
            if self.pos == 'd':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 180)
                self.pos = 'u'
            self.vy = -200
            
            
            
        if game.pressed[pygame.K_s]:
            if self.pos == 'r':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, -90)
                self.pos = 'd'
            if self.pos == 'l':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 90)
                self.pos = 'd'
            if self.pos == 'u':
                game.opposite_tank = pygame.transform.rotate(game.opposite_tank, 180)
                self.pos = 'd'
            self.vy = 200
            
            
          
        game.block_hit_list = pygame.sprite.spritecollide(self.tank, game.block_list, False)
        
        if len(game.block_hit_list) > 0:
            #print(1)
            self.vx = 0
            self.vy = 0
            if self.pos == 'l':
                self.x = self.x + 2
            if self.pos == 'r':
                self.x = self.x -2
            if self.pos == 'd':
                self.y = self.y -2
            if self.pos == 'u':
                self.y = self.y + 2
            
            game.block_hit_list = []
        game.player_hit_list = pygame.sprite.spritecollide(self.tank, game.player.player_list, False)
        if len(game.player_hit_list) > 0:
            self.vx = 0
            game.player.vx = 0
            game.player.vy = 0
            self.vy = 0
            if (self.pos == 'l') and (game.player.pos == 'l') and (self.x >= game.player.x):
                self.x = self.x + 2
                game.player.x = game.player.x - 2
            if self.pos == 'l':
                self.x = self.x + 2
                game.player_hit_list = []
            if (self.pos == 'r') and (game.player.pos == 'r') and (self.x <= game.player.x):
                self.x = self.x - 2
                game.player.x = game.player.x + 2
            if self.pos == 'r':
                self.x = self.x -2
                game.player_hit_list = []
            if (self.pos == 'd') and (game.player.pos == 'd') and (self.y <= game.player.y):
                self.y = self.y - 2
                game.player.y = game.player.y + 2
            
               
            if (self.pos == 'u') and (game.player.pos == 'u') and (self.y >= game.player.y):
                self.y = self.y + 4
                game.player.y = game.player.y - 2
            
                
            game.player_hit_list = []
        (self.vx) -= (game.delta * self.vx * 10)
        (self.vy) -= (game.delta * self.vy * 10)
        self.x += self.vx * game.delta
        self.y += self.vy * game.delta
        self.tank.rect.x = self.x
        self.tank.rect.y = self.y
        
        
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
        self.screen = pygame.display.set_mode(self.size, pygame.HWSURFACE)
        # set window caption
        pygame.display.set_caption('Tanks')
        self.space = pygame.image.load('space.bmp')
        
        # get object to help track time
        self.clock = pygame.time.Clock()
        # set default tool
        self.tool = 'run'
        self.player = Player()
        self.opposite_player = OpponentPlayer()
     
        self.tank_image_up = pygame.image.load('tanks_up.bmp')
        self.opposite_tank = pygame.image.load('opposite_tank.bmp')
        self.block_list = pygame.sprite.Group()
        self.grace_list = pygame.sprite.Group()
        self.player_hit_list = pygame.sprite.Group()
        self.opp_player_hit_list = pygame.sprite.Group()
        
        i = 0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 0
            self.block.rect.y = i
            self.block_list.add(self.block)
            i = i + 28
            if not i <= 400:
                break
        k = 0    
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = self.width - 35
            self.block.rect.y = k
            self.block_list.add(self.block)
            k = k + 28
            if not k <= 400:
                break
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = k
            self.block.rect.y = self.height - 20
            self.block_list.add(self.block)
            k = k + 20
            if not k <= 100:
                break
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 640 - k
            self.block.rect.y = self.height - 20
            self.block_list.add(self.block)
            k = k + 10
            if not k <= 150:
                break
        k=0
        while True:
            self.block = Proof_Walls((0,0,0), 40, 40)
            self.block.rect.x = 320 + k
            self.block.rect.y = 100
            self.block_list.add(self.block)
            k = k + 32
            if not k <= 160:
                break
        k=0
        while True:
            self.block = Grace((0,0,0), 40, 40)
            self.block.rect.x = self.height - 20 - k
            self.block.rect.y = 50
            self.grace_list.add(self.block)
            k = k + 32
            if not k <= 160:
                break
        k=0
        while True:
            self.block = Proof_Walls((0,0,0), 40, 40)
            self.block.rect.x = 100
            self.block.rect.y = 50 + k
            self.block_list.add(self.block)
            k = k + 32
            if not k <= 100:
                break
        self.block = Grace((0,0,0), 40, 40)
        self.block.rect.x = 100
        self.block.rect.y = 177
        self.grace_list.add(self.block)
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 100
            self.block.rect.y = 215 + k
            self.block_list.add(self.block)
            k = k + 30
            if not k <= 100:
                break
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 170
            self.block.rect.y = 180 + k
            self.block_list.add(self.block)
            k = k + 30
            if not k <= 140:
                break
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 200 + k
            self.block.rect.y = 300
            self.block_list.add(self.block)
            k = k + 30
            if not k <= 250:
                break
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = self.width - 60- k
            self.block.rect.y = 135
            self.block_list.add(self.block)
            k = k + 30
            if not k <= 100:
                break
        k=0
        while True:
            self.block = Walls((0,0,0), 40, 40)
            self.block.rect.x = 490
            self.block.rect.y = 165 + k
            self.block_list.add(self.block)
            k = k + 30
            if not k <= 60:
                break
        self.block = Walls((0,0,0), 40, 40)
        self.block.rect.x = 525
        self.block.rect.y = 225
        self.block_list.add(self.block)
        

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
        self.opposite_player.update(self)

    def render(self):
        """Render the scene"""

        self.screen.blit(self.space, (0,0))
        self.player.render(self)
        self.opposite_player.render(self)
        self.tank_image_up.set_colorkey((0,0,0))
        self.opposite_tank.set_colorkey((0,0,0))
        self.screen.blit(self.tank_image_up, ((self.player.tank.rect.x -5 ), (self.player.tank.rect.y - 5)))
        self.screen.blit(self.opposite_tank, ((self.opposite_player.tank.rect.x -5 ), (self.opposite_player.tank.rect.y - 5)))
        
        pygame.draw.rect(self.screen, (255, 0, 0), ((0,0),(20,20)), 0) 

        self.block_list.draw(self.screen)
        self.grace_list.draw(self.screen)
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
