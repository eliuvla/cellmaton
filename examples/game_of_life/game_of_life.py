import scene

def global_rule(self = scene.Scene() ):

    c = self.configuration
    print(c.shape)
    self.orbit.append(self.configuration.copy())
    for i in range(c.shape[0]):
        for j in range(c.shape[1]):
            local_rule(self,x=i,y=j)
    
def local_rule(self = scene.Scene(),x=0,y=0):
    num_alive = 0

    live = [255,255,255]
    death = [0,0,0]

    c = self.orbit[-1]
    max_x = c.shape[0]
    max_y = c.shape[1]
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if c[(x+i)%max_x, (y+j)%max_y][0] == 255:
                num_alive +=1
                
    
    

    if c[x][y][0] == 255:
        num_alive -= 1
        self.configuration[x][y] = death
        if num_alive== 2 or num_alive == 3:
            self.configuration[x][y] = live
    else:
        if num_alive == 3:
            self.configuration[x][y] = live
    

    