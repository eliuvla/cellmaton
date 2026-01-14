import scene

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

    for i in [-1,0,1]:
        for j in [-1,0,1]:
            r += c[(x+i)%max_x, (y+j)%max_y][0]
            g += c[(x+i)%max_x, (y+j)%max_y][1]
            b += c[(x+i)%max_x, (y+j)%max_y][2]

    r = r/9
    g = g/9
    b = b/9

    self.configuration[x][y] = [r,g,b]


    

    