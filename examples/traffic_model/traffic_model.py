import scene
import numpy as np


#Nagel–Schreckenberg model

v_3 = [255,0,0]
v_2 = [255,255,0]
v_1 = [0,255,0]
empty = [0,0,0] #no car


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

    neighborhood = np.empty((7,3),"uint8") #3 elementos a la izquierda de la posición
    velocity = 0

    for i in [-3,-2,-1,0,1,2,3]:
        neighborhood[i+3] = c[(x+i)%max_x, y]


     

    for i in [2,1,0]:
        if not (neighborhood[i] == empty).all():
            #print(neighborhood[i])
            if (neighborhood[i] == v_1).all():
                velocity = 1
            if (neighborhood[i] == v_2).all():
                velocity = 2
            if (neighborhood[i] == v_3).all():
                velocity = 3

            
            if not (neighborhood[3] == empty).all():
                velocity =  min(velocity,3-i)    
                if velocity == 3-i:
                    if velocity == 1:
                        self.configuration[x][y] = v_1
                    if velocity == 2:
                        self.configuration[x][y] = v_2
                    if velocity == 3:
                        self.configuration[x][y] = v_3
                else:
                    self.configuration[x][y] = empty
            else:
                if velocity == 3-i:
                    if velocity == 1:
                        self.configuration[x][y] = v_2
                    if velocity == 2:
                        self.configuration[x][y] = v_3
                    if velocity == 3:
                        self.configuration[x][y] = v_3
                else:
                    self.configuration[x][y] = empty

            break

        else:
            self.configuration[x][y] = empty
                

            
        
