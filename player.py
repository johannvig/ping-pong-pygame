import pygame


class Player:

    def __init__(self,x,y,size):

        self.x = x
        self.y = y
        self.size = size
        self.rect = pygame.Rect(self.x,self.y,self.size[0],self.size[1])



    def mouvement(self, speed):

        self.rect.y += speed

    def show(self, space):

        pygame.draw.rect(space, (200,200,200), self.rect)
