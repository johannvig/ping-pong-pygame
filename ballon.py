import pygame
import random

class Ballon:

    def __init__(self,x,y,size, direction):

        self.x = x
        self.y = y
        self.size = size
        self.direction = direction
        self.rect = pygame.Rect(self.x,self.y,self.size[-1],self.size[1])
        self.speed_random_y = random.randint(1,4)

    def mouvement(self, speed_x, speed_y):
        self.rect.x = (self.rect.x + self.direction * speed_x)
        self.rect.y += self.vitesse_aleatoire_y * speed_y

    def show(self, space):

        pygame.draw.rect(space, (230,230,230), self.rect)
