# import sys
# import jump
# import time

import sys
import time
import pygame
import traceback

# Jeu "Jump" minimal — joueur saute sur des plateformes
# Contrôles : ← → pour bouger, ESPACE pour sauter, R pour rejouer, Échap pour quitter.
      
# --- Configuration ---
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
FPS = 60

PLAYER_W, PLAYER_H = 40, 60
MOVE_SPEED = 5
JUMP_FORCE = -14
GRAVITY = 0.8

SKY = (135, 206, 235)
GROUND_COLOR = (50, 160, 60)
PLAYER_COLOR = (200, 30, 30)
PLATFORM_COLOR = (100, 100, 100)
TEXT_COLOR = (10, 10, 10)

print("DEBUG: lancement de jump.py (vérifiez la console pour messages)")  # message de débogage

# --- Initialisation ---
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jump Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 26)

def make_platforms():
    # Liste de rectangles (x, y, w, h)
    plats = [
        pygame.Rect(0, WINDOW_HEIGHT - 40, WINDOW_WIDTH, 40),             # sol
        pygame.Rect(150, 450, 150, 16),
        pygame.Rect(360, 360, 120, 16),
        pygame.Rect(520, 290, 140, 16),
        pygame.Rect(80, 220, 120, 16),
        pygame.Rect(420, 140, 160, 16),
    ]
    return plats

class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, WINDOW_HEIGHT - 40 - PLAYER_H, PLAYER_W, PLAYER_H)
        self.vel_y = 0.0
        self.jumping = False

    def move_h(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH

    def jump(self):
        if not self.jumping:
            self.vel_y = JUMP_FORCE
            self.jumping = True

    def apply_gravity(self):
        self.vel_y += GRAVITY
        if self.vel_y > 30:
            self.vel_y = 30  # clamping vitesse de chute
        self.rect.y += self.vel_y

    def land_on(self, plat_rect):
        self.rect.bottom = plat_rect.top
        self.vel_y = 0.0
        self.jumping = False

def check_platform_collisions(player, platforms, prev_bottom):
    # n'atterrit que si le joueur descend (vel_y > 0)
    if player.vel_y <= 0:
        return False

    for plat in platforms:
        # condition stricte pour détecter le passage de prev_bottom vers bottom
        if prev_bottom < plat.top <= player.rect.bottom:
            # chevauchement horizontal ?
            if player.rect.right > plat.left + 2 and player.rect.left < plat.right - 2:
                player.land_on(plat)
                return True
    return False

def draw(screen, player, platforms, elapsed, message=""):
    screen.fill(SKY)
    # plateformes
    for p in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, p)
    # joueur
    pygame.draw.rect(screen, PLAYER_COLOR, player.rect)
    # UI
    score_surf = font.render(f"Temps: {int(elapsed)} s", True, TEXT_COLOR)
    instr_surf = font.render("← → : bouger   •   Espace : sauter   •   R : rejouer   •   Échap : quitter", True, TEXT_COLOR)
    screen.blit(score_surf, (10, 10))
    screen.blit(instr_surf, (10, 36))
    if message:
        m = font.render(message, True, TEXT_COLOR)
        screen.blit(m, ((WINDOW_WIDTH - m.get_width())//2, 70))
    pygame.display.flip()

def main():
    try:
        player = Player()
        platforms = make_platforms()
        running = True
        start_time = time.time()
        game_over = False
        message = ""

        while running:
            dt = clock.tick(FPS) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_r:
                        # reset
                        player = Player()
                        platforms = make_platforms()
                        start_time = time.time()
                        game_over = False
                        message = ""
                    elif event.key == pygame.K_SPACE:
                        if not game_over:
                            player.jump()

            keys = pygame.key.get_pressed()
            if not game_over:
                if keys[pygame.K_LEFT]:
                    player.move_h(-MOVE_SPEED)
                if keys[pygame.K_RIGHT]:
                    player.move_h(MOVE_SPEED)

                prev_bottom = player.rect.bottom
                player.apply_gravity()

                # détection d'atterrissage
                landed = check_platform_collisions(player, platforms, prev_bottom)
                # si pas atterri et en dessous du sol -> game over (tombe)
                if player.rect.top > WINDOW_HEIGHT:
                    game_over = True
                    message = "Tu as perdu ! Appuie sur R pour rejouer."
                # si aucune collision, continuer (possibilité d'être en l'air)
                if landed:
                    pass

            elapsed = time.time() - start_time
            draw(screen, player, platforms, elapsed, message)

    except Exception:
        print("ERREUR: une exception inattendue est survenue. Voir la trace ci‑dessous :")
        traceback.print_exc()
        # garantir une fermeture propre
        try:
            pygame.quit()
        except:
            pass
        sys.exit(1)

if __name__ == "__main__":
    main()
