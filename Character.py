import pygame
import random

from bullet import Bullet


class Player:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed
        self.bullets=[]

    def draw(self, window):

        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
        for bullet in self.bullets:
            bullet.draw(window)
            bullet.move()


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_e]:
            print(1)
            self.bullets.append(Bullet(self.hitbox.x, self.hitbox.y,15,30,"bullet.png",5))



class Enemy:
    def __init__(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed



    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))

    def move(self):
        self.hitbox.y += self.speed
        if self.hitbox.y > 500:
            self.hitbox.x = random.randint(0,700)
            self.hitbox.y = random.randint(0,10)