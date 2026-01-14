import pygame
from PIL import Image
import numpy as np
import random
import importlib
import sys 
import os 






class Scene:
    def __init__(self, screen_size = (480,480), automaton_name = "empty"):
        pygame.init()

        img = pygame.image.load("icon.png")

        pygame.display.set_caption("cellmaton: "+automaton_name)
        pygame.display.set_icon(img)

        self.screen_size = screen_size        
        #self.screen = pygame.display.set_mode(self.screen_size, pygame.FULLSCREEN)
        self.screen = pygame.display.set_mode(self.screen_size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0
        self.scale = 1
        self.automaton_name = automaton_name
        self.automaton_path = "examples\\"+automaton_name+"\\"

        self.y = 0
        self.x = 0

        self.configuration = np.empty((1,1,3),"uint8")
        self.orbit = []
        #Scene.rule = None
        if self.automaton_name != "empty":
            self.load_automaton()

        self.events = pygame.event.get()
        self.iteration = 0
        
    def global_rule(self):
        pass

    def load_automaton(self):
        string_import = "examples."+self.automaton_name+"."+self.automaton_name

        self.automaton_module = importlib.import_module(string_import)
        Scene.global_rule = self.automaton_module.global_rule
        img = Image.open(self.automaton_path+"configuration.png")
        img = img.convert("RGB")
        res = np.asarray(img)


        #transpose the array
        configuration = np.empty((res.shape[1],res.shape[0],res.shape[2]),"uint8")

        for i in range(res.shape[0]):
            for j in range(res.shape[1]):
                configuration[j][i] = res[i][j]

        self.configuration = configuration
        
        
    
    def render(self):
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()


        # fill the screen with a color to wipe away anything from last frame
        self.screen.fill("black")
        self.draw()
        
        


        # flip() the display to put your work on screen
        pygame.display.flip()  
        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        self.dt = self.clock.tick(60) / 1000
        print(self.clock.get_fps())
        

    def draw(self):
        image_surface = pygame.pixelcopy.make_surface(self.configuration)
        #image_surface = pygame.transform.rotate(image_surface,-90)
        #image_surface = pygame.transform.flip(image_surface,1,0)
        image_surface = pygame.transform.scale_by(image_surface,self.scale)
        self.screen.blit(image_surface)
        pass

    def save_img(self):

        

        folder_name = self.automaton_path+"export/"
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)
            print(f"Folder '{folder_name}' created.")

        self.iteration +=1

        c = self.configuration

        export = np.empty((c.shape[1],c.shape[0],c.shape[2]),"uint8")

        for i in range(c.shape[0]):
            for j in range(c.shape[1]):
                export[j][i] = c[i][j]


        img = Image.fromarray(export)
        img.save(folder_name+str(self.iteration)+'.png')

    def update(self):

        self.save_img()

        self.global_rule()

        keys = pygame.key.get_pressed()
        self.events = pygame.event.get()

        if keys[pygame.K_w]:
            self.y -= self.screen_size[1]/(100*self.scale)
        if keys[pygame.K_s]:
            self.y += self.screen_size[1]/(100*self.scale)
        if keys[pygame.K_a]:
            self.x -= self.screen_size[0]/(100*self.scale)
        if keys[pygame.K_d]:
            self.x += self.screen_size[0]/(100*self.scale)

        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.scale += 1 
                if event.key == pygame.K_DOWN:
                    self.scale -= 1
        if self.scale<1:
            self.scale = 1
        
        

