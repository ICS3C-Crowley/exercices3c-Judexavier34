import sys
import pygame
import random

# Initialisation de base
pygame.init()
print("1. Pygame initialisé")

# Constantes
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GROUND_HEIGHT = 500
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
GRAVITY = 0.8
JUMP_FORCE = -15
MOVE_SPEED = 5
TERMINAL_VELOCITY = 18
ENEMY_WIDTH = 40
ENEMY_HEIGHT = 40
ENEMY_SPEED = 3

# Couleurs
SKY_BLUE = (135, 206, 235)
GREEN = (34, 139, 34)
RED = (200, 30, 30)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# Ajout : paliers de motivation (secondes -> message)
MOTIVATIONS = {
    10: "Bien joué — continue !",
    20: "Super travail !",
    30: "Incroyable, tu tiens bon !",
    60: "Maître du jeu !"
}

class Player:
    def __init__(self, x=100, y=None):
        if y is None:
            y = GROUND_HEIGHT - PLAYER_HEIGHT
        self.rect = pygame.Rect(x, y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.vel_y = 0.0
        self.jumping = False

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_FORCE
            self.jumping = True

    def update(self):
        # appliquer gravité
        self.vel_y += GRAVITY
        if self.vel_y > TERMINAL_VELOCITY:
            self.vel_y = TERMINAL_VELOCITY
        self.rect.y += self.vel_y

        # collision avec le sol
        if self.rect.bottom >= GROUND_HEIGHT:
            self.rect.bottom = GROUND_HEIGHT
            self.vel_y = 0.0
            self.jumping = False

class Enemy:
    def __init__(self, x=None, y=None):
        if x is None:
            x = random.randint(0, WINDOW_WIDTH - ENEMY_WIDTH)
        if y is None:
            y = GROUND_HEIGHT - ENEMY_HEIGHT
        self.rect = pygame.Rect(x, y, ENEMY_WIDTH, ENEMY_HEIGHT)
        self.direction = random.choice([-1, 1])  # -1 = gauche, 1 = droite

    def update(self):
        # déplacement horizontal
        self.rect.x += self.direction * ENEMY_SPEED
        
        # rebondir aux limites
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.direction *= -1

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)
        # dessiner les yeux
        eye_y = self.rect.y + 10
        pygame.draw.circle(screen, BLACK, (self.rect.x + 10, eye_y), 3)
        pygame.draw.circle(screen, BLACK, (self.rect.x + 30, eye_y), 3)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Super Mario - Minimal")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 28)

    player = Player()
    score = 0.0
    enemies = []
    game_over = False

    # Variables pour la motivation visuelle
    player_color = RED
    milestone_end_ms = 0
    last_milestone = 0
    motiv_message = ""
    
    # Spawn initial d'ennemis
    for _ in range(3):
        enemies.append(Enemy())

    running = True
    while running:
        dt = clock.tick(60) / 1000.0  # secondes depuis la dernière frame
        now_ms = pygame.time.get_ticks()

        # événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    if not game_over:
                        player.jump()
                elif event.key == pygame.K_r and game_over:
                    # Redémarrer le jeu
                    player = Player()
                    enemies = [Enemy() for _ in range(3)]
                    score = 0.0
                    game_over = False
                    last_milestone = 0

        if not game_over:
            # entrée continue pour déplacement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move(-MOVE_SPEED)
            if keys[pygame.K_RIGHT]:
                player.move(MOVE_SPEED)

            # mise à jour
            player.update()
            score += dt  # score basé sur le temps joué
            score_int = int(score)

            # Mise à jour des ennemis
            for enemy in enemies:
                enemy.update()

            # Vérifier les collisions avec les ennemis
            for enemy in enemies:
                if player.rect.colliderect(enemy.rect):
                    # Si le joueur saute sur l'ennemi (y en haut)
                    if player.vel_y > 0 and player.rect.centery < enemy.rect.centery:
                        enemies.remove(enemy)
                        player.vel_y = JUMP_FORCE  # rebondir
                        score += 10
                    else:
                        game_over = True

            # Vérifier si un nouveau palier est atteint
            for thresh in sorted(MOTIVATIONS.keys()):
                if score_int >= thresh and thresh > last_milestone:
                    last_milestone = thresh
                    motiv_message = MOTIVATIONS[thresh]
                    milestone_end_ms = now_ms + 1500  # afficher et "flash" pendant 1.5s
                    player_color = (255, 165, 0)  # orange temporaire
                    break

            # Rétablir la couleur du joueur après le flash
            if now_ms >= milestone_end_ms:
                player_color = RED
                if now_ms >= milestone_end_ms and motiv_message and (now_ms - milestone_end_ms) > 1000:
                    motiv_message = ""

        # dessin
        screen.fill(SKY_BLUE)
        pygame.draw.rect(screen, GREEN, (0, GROUND_HEIGHT, WINDOW_WIDTH, WINDOW_HEIGHT - GROUND_HEIGHT))
        
        # Dessiner le joueur
        pygame.draw.rect(screen, player_color, player.rect)
        
        # Dessiner les ennemis
        for enemy in enemies:
            enemy.draw(screen)

        score_surf = font.render(f"Score: {int(score)}", True, BLACK)
        instr_surf = font.render("← → bouger  •  Espace sauter  •  Échap quitter", True, BLACK)
        screen.blit(score_surf, (10, 8))
        screen.blit(instr_surf, (10, 34))

        # Afficher le message de motivation si présent
        if motiv_message:
            motiv_surf = font.render(motiv_message, True, BLACK)
            # centrer horizontalement
            mx = (WINDOW_WIDTH - motiv_surf.get_width()) // 2
            screen.blit(motiv_surf, (mx, 60))

        # Afficher Game Over
        if game_over:
            go_surf = font.render("GAME OVER ! Appuie sur R pour recommencer", True, RED)
            mx = (WINDOW_WIDTH - go_surf.get_width()) // 2
            screen.blit(go_surf, (mx, WINDOW_HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()