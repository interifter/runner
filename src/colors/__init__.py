import colors.red

COLORS = {
    'RED':red.ride
}

WRITERS = {
    'RED':red.write
}

MIXERS = {
    'RED':red.mix
}

class ColorException(Exception):
    """Color exception
    
    Arguments:
        Exception {[type]} -- [description]
    """
    pass