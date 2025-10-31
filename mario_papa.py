import sys 
import pygame
import os

# Initialize Pygame
pygame.init()

# Game constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
GROUND_HEIGHT = 500
GRAVITY = 0.8
JUMP_FORCE = -15
MOVE_SPEED = 5

    # Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Super Mario Game")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, GROUND_HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vel_y = 0
        self.jumping = False

    def move(self, dx):
        self.rect.x += dx
        # Keep player in bounds
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_FORCE
            self.jumping = True

    def update(self):
        # Apply gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Check ground collision
        if self.rect.bottom > GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.vel_y = 5
            self.jumping = False  
            if key[pygame .KRIGHT]:
                self.rest.X=+5   

def game_loop():
    player = Player()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                if event.key == pygame.K_ESCAPE:
                    return

        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-MOVE_SPEED)
        if keys[pygame.K_RIGHT]:
            player.move(MOVE_SPEED)

        # Update game state
        player.update()

        # Draw
        screen.fill((135, 206, 235))  # Sky blue background
        pygame.draw.rect(screen, GREEN, (0, GROUND_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT - GROUND_HEIGHT))
        pygame.draw.rect(screen, RED, player.rect)
        
        pygame.display.flip()
        clock.tick(60)

def main_menu():
    while True:
        print("\nSuper Mario Game")
        print("1. Play NEW GAME")
        print("2. Play AGAIN?")
        print("3. Options")
        print("4. Exit\n")

        choice = input("Enter your choice > ")

        if choice == "4":
            pygame.quit()
            sys.exit(0)
        elif choice == "3":
            print("Menu options... coming soon")
        elif choice == "2":
            print("No save file found")
        elif choice == "1":
            print("Loading game...")
            game_loop()
            pygame.display.quit()


class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image=pygame.image.load( "goomba.png ")
        self.rect=self.image.get_rect(topleft=(x,y))
        self.direction=1 
        self.speed=2 


    def update(self):
        self.rect.x += self.direction * self.speed
    
        if self.rect.left < 0 or self.rect.right >800:
            self.direction *= -1
    
    def action(self):
        print("action")

if __name__ == "__main__":
    main_menu()   