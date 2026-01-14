import pygame
from scene import * 




scene = Scene(automaton_name = "water")


scene.render()

while scene.running:
    scene.update()
    scene.render()
    
    