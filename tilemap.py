import pygame as pg
from settings import *

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Grid:

    direction = {'n': [1, 0, 0, 0], 'e': [0, 1, 0, 0],'s': [0, 0, 1, 0],'w': [0, 0, 0, 1]}

    def __init__(self, edge):
        self.edge = edge
        self.adjust()
        self.gridconnect = {}
        self.gridbase = [[(x, y) for x in range(self.edge[3],self.edge[1]+1)] for y in range(self.edge[0],self.edge[2]-1,-1)]
        self.griddata = {(x, y): None for x in range(self.edge[3],self.edge[1]+1) for y in range(self.edge[0],self.edge[2]-1,-1)}
        self.gridopen = {(x, y): [0, 0, 0, 0] for x in range(self.edge[3],self.edge[1]+1) for y in range(self.edge[0],self.edge[2]-1,-1)}

    def adjust(self, x = None):
        edge = self.edge if x == None else x
        self.gridcol = edge[0] - edge[2]
        self.gridrow = edge[1] - edge[3]
        self.offset = (self.edge[3], - self.edge[0])
        self.gridwidth = self.gridcol * TILESIZE
        self.gridheight = self.gridrow * TILESIZE



    def tempadd(self, game, wall):
        # [5, 7, -2, -3]
        for i in self.gridbase:
            for j in i:
                if j[0] in (2, 4, 7):
                    x, y = j[0], j[1]
                    wall(game, x, y)
        

    def add(self, game, tile, co):
        direc_lkp = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}
        relpos = self.convert_r(tile.pos)
        pass
        
    def oldadd(self, tile, direction = None, starttile = False):
        self.griddata[tile.pos] = tile
        self.gridconnect[tile.pos] = []
        if not starttile:
            if tile.open != [1,1,1,1]:
                if direction == None:
                    raise Exception('no direc given on non-4 tile')
                direc_lkp = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}
                origin = direc_lkp[direction]
                tile.Rotate(self.TileDirection(tile, origin))
            for i,j in enumerate(tile.open):
                if j == 1:                  
                    if (i in (0, 2)) and (self.griddata[(tile.x, tile.y + 1 - i)] != None):
                        if self.gridopen[(tile.x, tile.y + 1 - i)][i - 2] == 1:
                            self.gridconnect[(tile.x, tile.y + 1 - i)].append(tile.pos)
                            self.gridconnect[tile.pos].append((tile.x, tile.y + 1 - i))
                    elif (i in (1, 3)) and (self.griddata[(tile.x + 2 - i, tile.y)] != None):
                        if self.gridopen[(tile.x + 2 - i, tile.y)][i - 2] == 1:
                            self.gridconnect[(tile.x + 2 - i, tile.y)].append(tile.pos)
                            self.gridconnect[tile.pos].append((tile.x + 2 - i, tile.y))
        else:
            self.gridopen[tile.pos] = tile.open

class Camera:
    def __init__(self, width, height, tg):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
        x = -tg.rect.centerx
        y = -tg.rect.centery
        self.dp = (x, y)
        self.op = (0, 0)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def update(self, ip, np):
        # x = -target.rect.centerx + int(WIDTH / 2)
        # y = -target.rect.centery + int(HEIGHT / 2)

        # # limit scrolling to map size
        # x = min(0, x)  # left
        # y = min(0, y)  # top
        # x = max(-(self.width - WIDTH), x)  # right
        # y = max(-(self.height - HEIGHT), y)  # bottom
        if ip != None:
            self.dp = (self.op[0] + np[0] - ip[0], self.op[1] + np[1] - ip[1])
            print('1')
        else:
            print('2' + str(self.dp))
            self.op = self.dp
        x = self.dp[0] + int(WIDTH / 2)
        y = self.dp[1] + int(HEIGHT / 2)
        self.camera = pg.Rect(x, y, self.width, self.height)