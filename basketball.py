import pygame
import sys
import random

# Initialisation
pygame.init()

# Constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
BALL_RADIUS = 10
BASKET_WIDTH = 60
BASKET_HEIGHT = 20

GRAVITY = 1
MOVE_SPEED = 10
THROW_FORCE = 30

# Couleurs
SKY_BLUE = (135, 206, 235)
GROUND_COLOR = (139, 69, 19)
PLAYER_COLOR = (255, 100, 0)
BALL_COLOR = (255, 165, 0)
BASKET_COLOR = (200, 50, 50)
TEXT_COLOR = (0, 0, 0)

# Ajout : paliers de motivation et paramètres d'affichage
MOTIVATIONS = {
    3: "Bravo ! 3 paniers — continue !",
    5: "Super ! 5 paniers marqués !",
    10: "Incroyable — 10 paniers !"
}
MOTIVATION_DURATION_MS = 2000  # durée d'affichage en ms
PLAYER_COLOR_FLASH = (255, 215, 0)
BASKET_COLOR_FLASH = (255, 120, 120)
FLASH_BG_COLOR = (255, 255, 255, 80)  # blanc semi-transparent pour le flash

class Player:
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2 - PLAYER_WIDTH // 2, WINDOW_HEIGHT - 150, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.has_ball = True
        
    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
    
    def throw_ball(self):
        if self.has_ball:
            ball_x = self.rect.centerx
            ball_y = self.rect.top
            self.has_ball = False
            return Ball(ball_x, ball_y, -THROW_FORCE, -THROW_FORCE)
        return None

class Ball:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = float(x)
        self.y = float(y)
        self.vel_x = vel_x
        self.vel_y = vel_y
    
    def update(self):
        self.vel_y += GRAVITY
        self.x += self.vel_x
        self.y += self.vel_y
        
        # Rebond sur les murs
        if self.x - BALL_RADIUS < 0 or self.x + BALL_RADIUS > WINDOW_WIDTH:
            self.vel_x *= -0.8
        
        # Si le ballon tombe au sol
        if self.y + BALL_RADIUS > WINDOW_HEIGHT - 50:
            return False  # Ballon perdu
        
        return True
    
    def get_rect(self):
        return pygame.Rect(self.x - BALL_RADIUS, self.y - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)

class Basket:
    def __init__(self):
        self.x = random.randint(BASKET_WIDTH, WINDOW_WIDTH - BASKET_WIDTH)
        self.y = 150
        self.direction = random.choice([-1, 1])
        self.speed = 2
    
    def update(self):
        self.x += self.direction * self.speed
        if self.x - BASKET_WIDTH // 2 < 0 or self.x + BASKET_WIDTH // 2 > WINDOW_WIDTH:
            self.direction *= -1
    
    def get_rect(self):
        return pygame.Rect(self.x - BASKET_WIDTH // 2, self.y, BASKET_WIDTH, BASKET_HEIGHT)
    
    def check_score(self, ball_rect):
        basket_rect = self.get_rect()
        return ball_rect.colliderect(basket_rect)

def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Basketball Game")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)
    
    player = Player()
    basket = Basket()
    ball = None
    score = 0
    attempts = 0

    # Variables de motivation
    motiv_message = ""
    motiv_end_ms = 0
    flash_end_ms = 0
    seen_milestones = set()
    player_color_current = PLAYER_COLOR
    basket_color_current = BASKET_COLOR

    running = True
    while running:
        clock.tick(FPS)
        now_ms = pygame.time.get_ticks()

        # Événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE and player.has_ball:
                    ball = player.throw_ball()
                    attempts += 1
                elif event.key == pygame.K_r:
                    # Redémarrer
                    player = Player()
                    basket = Basket()
                    ball = None
                    score = 0
                    attempts = 0
                    motiv_message = ""
                    motiv_end_ms = 0
                    flash_end_ms = 0
                    seen_milestones.clear()
                    player_color_current = PLAYER_COLOR
                    basket_color_current = BASKET_COLOR
        
        # Contrôles continus
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-MOVE_SPEED)
        if keys[pygame.K_RIGHT]:
            player.move(MOVE_SPEED)
        
        # Mise à jour
        basket.update()
        
        # mise à jour du score / détection de panier
        if ball:
            if ball.update():
                if basket.check_score(ball.get_rect()):
                    score += 1
                    ball = None
                    player.has_ball = True

                    # déclencher motivation une seule fois par palier
                    if score in MOTIVATIONS and score not in seen_milestones:
                        seen_milestones.add(score)
                        motiv_message = MOTIVATIONS[score]
                        motiv_end_ms = now_ms + MOTIVATION_DURATION_MS
                        flash_end_ms = now_ms + MOTIVATION_DURATION_MS
                        player_color_current = PLAYER_COLOR_FLASH
                        basket_color_current = BASKET_COLOR_FLASH
            else:
                ball = None
                player.has_ball = True

        # rétablir état après la durée
        if now_ms >= motiv_end_ms:
            motiv_message = ""
        if now_ms >= flash_end_ms:
            player_color_current = PLAYER_COLOR
            basket_color_current = BASKET_COLOR
        
        # Dessin
        screen.fill(SKY_BLUE)
        pygame.draw.rect(screen, GROUND_COLOR, (0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50))
        
        # Dessiner le panier
        basket_rect = basket.get_rect()
        pygame.draw.rect(screen, basket_color_current, basket_rect)
        
        # Dessiner le joueur
        pygame.draw.rect(screen, player_color_current, player.rect)
        
        # Dessiner le ballon
        if ball:
            pygame.draw.circle(screen, BALL_COLOR, (int(ball.x), int(ball.y)), BALL_RADIUS)
        elif player.has_ball:
            pygame.draw.circle(screen, BALL_COLOR, (player.rect.centerx, player.rect.top - 15), BALL_RADIUS)
        
        # Afficher le score
        score_text = font.render(f"Score: {score} | Tentatives: {attempts}", True, TEXT_COLOR)
        screen.blit(score_text, (10, 10))
        
        instr_text = font.render("← → Bouger  |  ESPACE Lancer  |  R Recommencer  |  Échap Quitter", True, TEXT_COLOR)
        screen.blit(instr_text, (10, 50))

        # Flash d'écran semi-transparent si activé
        if now_ms < flash_end_ms:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
            overlay.fill(FLASH_BG_COLOR)
            screen.blit(overlay, (0, 0))

        # Afficher message de motivation (centré) si présent
        if motiv_message:
            motiv_surf = font.render(motiv_message, True, TEXT_COLOR)
            mx = (WINDOW_WIDTH - motiv_surf.get_width()) // 2
            screen.blit(motiv_surf, (mx, 100))
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()