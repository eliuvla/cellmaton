import scene
import numpy as np


empty = [255,255,255]
wall = [0,0,0]
path = [0,0,255] #azul
goal = [0,255,0] #verde


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

    num_wall = 0
    num_empty = 0
    num_path = 0
    num_goal = 0


    for i in [-1,1]:
        if (c[(x+i)%max_x, y] == empty).all():
            num_empty += 1
        if (c[(x+i)%max_x, y] == wall).all():
            num_wall += 1
        if (c[(x+i)%max_x, y] == path).all():
            num_path += 1
        if (c[(x+i)%max_x, y] == goal).all():
            num_goal += 1
    for j in [-1,1]:
        if (c[x, (y+j)%max_y] == empty).all():
            num_empty += 1
        if (c[x, (y+j)%max_y] == wall).all():
            num_wall += 1
        if (c[x, (y+j)%max_y] == path).all():
            num_path += 1
        if (c[x, (y+j)%max_y] == goal).all():
            num_goal += 1

    if (c[x,y] == empty).all():
        if num_path !=0:
            self.configuration[x][y] = path
    
    if (c[x,y] == path).all():
        if num_goal !=0:
            self.configuration[x][y] = goal

        if num_wall >= 3:
            self.configuration[x][y] = wall

            




    
