import pygame as pg
from settings import *

class Coordinate:
    def __init__(self, co):
        self._x = co[0]
        self._y = co[0]

        @property
        def x(self):
            return (self._x)

        @x.setter
        def x(self, i):
            self._x = i

        @property
        def y(self):
            return (self._x)

        @x.setter
        def y(self, i):
            self._y = i

        @property
        def pos(self):
            return ((self._x, self._y))

coord = Coordinate

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.vx, self.vy = 0, 0
        self.x = x * TILESIZE
        self.y = y * TILESIZE

    def get_keys(self):
        self.vx, self.vy = 0, 0
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.vx = -PLAYER_SPEED
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.vx = PLAYER_SPEED
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.vy = -PLAYER_SPEED
        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.vy = PLAYER_SPEED
        if self.vx != 0 and self.vy != 0:
            self.vx *= 0.7071
            self.vy *= 0.7071

    def collide_with_walls(self, dir):
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vx > 0:
                    self.x = hits[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.x = hits[0].rect.right
                self.vx = 0
                self.rect.x = self.x
        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vy > 0:
                    self.y = hits[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.y = hits[0].rect.bottom
                self.vy = 0
                self.rect.y = self.y

    def update(self):
        self.get_keys()
        self.x += self.vx * self.game.dt
        self.y += self.vy * self.game.dt
        self.rect.x = self.x
        self.collide_with_walls('x')
        self.rect.y = self.y
        self.collide_with_walls('y')

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, color = GREEN):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class TileBase(pg.sprite.Sprite):
    def __init__(self, game, co, case): # Relative Coordinates
        self.groups = game.all_sprites, game.tiles
        pg.sprite.Sprite.__init__(self, self.groups)
        
        self.x = co[0]
        self.y = co[1]

        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        
        self.orient = 0

        OpenPath = {"0": [0,0,0,0], "1": [0,0,1,0], "2s": [1,0,1,0], "2c": [0,0,1,1], "3": [1,0,1,1], "4": [1,1,1,1]}
        self.open = OpenPath[case]

    def img(self, game, tile, case):
        self.image = game.img_set(tile, case)
        self.rect = self.image.get_rect()
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
    
    def updatepos(self, co): # co = 
        if co == 'x':
            self.x += 1
            self.rect.x = self.x * TILESIZE
        elif co == 'y':
            self.y += 1
            self.rect.y = self.y * TILESIZE
        else:
            raise Exception('TILEBASE.updatepos err: ' + str(co))



    @property
    def pos(self):
        return ((self.x,self.y))

    def Rotate(self, rpt): #Clockwise
        for _ in rpt:
            self.open = self.open[-1:] + self.open[:-1]

class StartTile(TileBase):
    def __init__(self, game, co):
        super().__init__(game, co, '4')
        super().img('Start', '4')