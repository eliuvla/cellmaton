import scene
import numpy as np


def global_rule(self = scene.Scene() ):

    c = self.configuration
    self.orbit.append(self.configuration.copy())
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            local_rule(self,x=i,y=j)
    
def local_rule(self = scene.Scene(),x=0,y=0):
    
    c = self.orbit[-1]
    max_x = c.shape[0]
    max_y = c.shape[1]

    r = 0
    g = 0
    b = 0

    delta = 1/25 
    conv = np.array([[0,-delta,0], [-delta,1+4*delta,-delta], [0,-delta,0]])
    
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            r += conv[i+1][j+1]*c[(x+i)%max_x, (y+j)%max_y][0]
            g += conv[i+1][j+1]*c[(x+i)%max_x, (y+j)%max_y][1]
            b += conv[i+1][j+1]*c[(x+i)%max_x, (y+j)%max_y][2]
    
    r = min(max(r,0),255)
    g = min(max(g,0),255)
    b = min(max(b,0),255)

    self.configuration[x][y] = [r,g,b]


    

    