import pygame


class Player:
    def init(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed


    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.hitbox.y -= self.speed
        if keys[pygame.K_s]:
            self.hitbox.y += self.speed
        if keys[pygame.K_a]:
            self.hitbox.x -= self.speed
        if keys[pygame.K_d]:
            self.hitbox.x += self.speed


class Enemy:
    def init(self, x, y, w, h, img, speed):
        self.photo = pygame.transform.scale(pygame.image.load(img), (w, h))
        self.hitbox = self.photo.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        self.speed = speed



    def draw(self, window):
        #pygame.draw.rect(window, (0,0,255), self.hitbox)
        window.blit(self.photo, (self.hitbox.x, self.hitbox.y))
