def Reveal(ins, param):
    '''
    Parameters:
    Reveal Direction
    Tile Orientation
    '''
    direction_lookup = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}
    parameter = direction_lookup[param]
    place = (ins.attr['pos'][i] + parameter[i] for i in (0, 1))
    if ins.main_ins.grid.griddata[place] == None:
        pop = ins.main_ins.extract.tilestack.pop(0)
        tileinfo = ins.main_ins.extract.tile[pop[0]](place, pop[1])
    else:
        raise Exception('grid occupied at ' + str(place))
    tile = ins.main_ins.extract.tile[tileinfo[0]](place, tileinfo[1])
    ins.main_ins.grid.TileAdd(tile, param)

def Move(ins, param):
    '''
    Parameters:
    Move Direction
    '''
    direction_lookup = {'n': (0, 1), 'e': (1, 0), 's': (0, -1), 'w': (-1, 0)}
    parameter = direction_lookup[param]
    mve = (ins.attr['pos'][i] + parameter[i] for i in (0, 1))
    if (ins.main_ins.grid.griddata[mve] != None) and ():
        pass
    else:
        raise Exception('no tile at ' + str(mve))
    
    pass

def Explore(ins, param):
    '''
    Parameters:

    '''
    pass

def Run(ins, param):
    '''
    Parameters:

    '''
    pass

def Heal(ins, param):
    '''
    Parameters:

    '''
    pass


def Swim(ins, param):
    '''
    Parameters:

    '''
    pass

def Dig(ins, param):
    '''
    Parameters:

    '''
    pass

def Hide(ins, param):
    '''
    Parameters:

    '''
    pass

def Squeeze(ins, param):
    '''
    Parameters:

    '''
    pass

def PlaceRope(ins, param):
    '''
    Parameters:

    '''
    pass