# python histogram equalization 

import numpy as np
import PIL.Image as Image
import sys
import matplotlib.pyplot as plt
from readimg import ReadImage

def HistEqMapping( hist, n ):
    lut=np.zeros(256)
    s = 0
    
    for i in range( 0, 256 ):
        s += hist[i]
        lut[i] = 255.*s/n
        
    lut = np.uint8(lut)

    return lut

def HistEq( f ):
    hist = f.histogram()

    size = f.size
    n = size[0]*size[1]

    lut = HistEqMapping( hist, n )

    #g = np.array( f )
    #g = g.ravel()
    #
    #for i in range( len(g) ):
    #    x = g[i]
    #    g[i] = lut[x]
    #
    #g = g.reshape( (size[0], size[1]) )
    g = np.array( f )
    g = lut[g]
    
    return g
        

def main( fn1, fn2):
    try:
        f= ReadImage( fn1, False )
    except:
        return
    
    g = HistEq( f )

    g = Image.fromarray(g)
    
    g.save( fn2 )



if __name__=='__main__':
    if len( sys.argv ) == 3:
        main(sys.argv[1], sys.argv[2])
    else:
        print('Usage: ', sys.argv[0], "[image file 1] [image file 2]" )



    
    
