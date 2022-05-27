import pygame
from player import Player
from ballon import Ballon
import random
import math

class ping_pong:

    def __init__(self):

        #define the size of the screen
        self.ecran = pygame.display.set_mode((900, 500))

        #name the game "ping pong"
        pygame.display.set_caption("ping pong")


        # for the loop
        # allows you to play continuously
        self.jeu_en_cours =True


        self.player_1_x, self.player_1_y = 20,250
        self.player_2_x, self.player_2_y = 860, 250
        self.player_size = [20,80]
        self.speed_y_1, self.speed_y_2= 0,0


        self.player_1 = Player(self.player_1_x, self.player_1_y, self.player_size)
        self.player_2 = Player(self.player_2_x, self.player_2_y, self.player_size)

        self.rect = pygame.Rect(0,0,900,500)


        self.ballon_direction = [-1,1]
        self.ballon = Ballon(450,250,[10,10], random.choice(self.ballon_direction))
        self.ballon_shoot = False
        self.ballon_speed_x, self.ballon_speed_y = 15, 2
        
        self.score_1, self.score_2 = 0, 0


    def main(self):

        while self.jeu_en_cours:

                
                # event processing
                for event in pygame.event.get():

                    # allow to leave the game
                    if event.type == pygame.QUIT:
                        self.jeu_en_cours = False


                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            self.speed_y_1 -= 1
                        if event.key == pygame.K_DOWN:
                            self.speed_y_1 += 1
                        if event.key == pygame.K_w:
                            self.speed_y_2 -= 1
                        if event.key == pygame.K_s:
                            self.speed_y_2 += 1
                        if event.key == pygame.K_SPACE:
                            self.ballon_shoot = True

                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            self.speed_y_1 = 0
                        if event.key == pygame.K_DOWN:
                            self.speed_y_1 = 0
                        if event.key == pygame.K_w:
                            self.speed_y_2 = 0
                        if event.key == pygame.K_s:
                            self.speed_y_2 = 0


                self.player_1.mouvement(self.speed_y_1)
                self.player_2.mouvement(self.speed_y_2)

                self.player_1.rect.clamp_ip(self.rect)
                self.player_2.rect.clamp_ip(self.rect)

                if self.ballon_shoot:
                    self.ballon.mouvement(self.ballon_speed_x, self.ballon_speed_y)

                if self.player_1.rect.colliderect(self.ballon.rect) or self.player_2.rect.colliderect(self.ballon.rect):

                    self.ballon_speed_x = self.change_direction_ballon(self.ballon_speed_x, 0)
                    self.ballon_speed_y = self.change_direction_ballon(self.ballon_speed_y, 60)
                    #self.ballon.speed_random_y = random.randint(1, 3)



                if self.ballon.rect.top <= 0 or self.ballon.rect.bottom >= 500:

                    self.ballon_speed_y  =  self.change_direction_ballon(self.ballon_speed_y,0)
                    
                if self.balle.rect.right >= 915:
                    
                    self.balle.rect.x, self.balle.rect.y = 450, 250 
                    self.score_1 += 1
                    self.balle_shoot = False
                if self.balle.rect.left <= -15:
                    
                    self.balle.rect.x, self.balle.rect.y = 450, 250 
                    self.score_2 += 1 
                    self.balle_shoot = False



                self.ballon.rect.clamp_ip(self.rect)


                # color of the screen
                self.ecran.fill((0, 0, 0))
                
                
                self.creer_message('big', f"Jeu Pong", [300, 50, 20, 20], (255, 255, 255))
                self.creer_message('big', f" { self.score_1 }", [300, 200, 50, 50], (255, 255, 255))
                self.creer_message('big', f" { self.score_2 }", [485, 200, 50, 50], (255, 255, 255))
                if self.balle_shoot is False:
                  self.creer_message('small', f" Appuyer Sur Espace Pour Commencer Le Jeu", [30, 100, 300, 50], (255, 255, 255))

                self.ballon.show(self.ecran)
                self.player_1.show(self.ecran)
                self.player_2.show(self.ecran)
                
                


                # update the screen
                pygame.display.flip()

    def change_direction_ballon(self, speed, angle):

        speed = - (speed * math.cos(angle))

        return speed





    def show_message(self,font, message, color,message_rectangle):

        if font == "small":

            font= pygame.font.SysFont('impact', 20, False)

        if font == "medium":

            font= pygame.font.SysFont('impact', 30, False)

        if font == "big":

            font= pygame.font.SysFont('arial', 40, True)

        message = font.render(message, True, color)

        self.ecran.blit(message, message_rectangle)




if __name__ == '__main__':
    pygame.init()
    ping_pong().main()
    pygame.quit()
