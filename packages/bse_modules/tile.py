class TileBase():
    def __init__(self, co):
        if not isinstance(co, tuple): raise Exception('Tile Coordinate not tuple: ' + str(type(co))) 
        self._x = co[0]
        self._y = co[1]
        self._coordinate = co
        self.orient = 0

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def pos(self):
        return self._coordinate

class Tile(TileBase):
    def __init__(self, co, case):
        super().__init__(co)
        OpenPath = {"0": [0,0,0,0], "1": [0,0,1,0], "2s": [1,0,1,0], "2c": [0,0,1,1], "3": [1,0,1,1], "4": [1,1,1,1]}
        self.open = OpenPath[case]

    def Rotate(self, rpt): #Clockwise
        for _ in rpt:
            self.open = self.open[-1:] + self.open[:-1]

