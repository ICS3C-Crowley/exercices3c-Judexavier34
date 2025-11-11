try:
    import pygame
    print("✅ Pygame est bien installé!")
    
    pygame.init()
    print("✅ Pygame est initialisé correctement!")
    
    # Test de création de fenêtre
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Test Pygame")
    print("✅ La fenêtre s'ouvre correctement!")
    
    # Attendre 3 secondes
    pygame.time.wait(3000)
    
    pygame.quit()
    print("✅ Test terminé avec succès!")

except ImportError:
    print("❌ ERREUR: Pygame n'est pas installé")
    print("➡️ Tapez cette commande pour l'installer:")
    print("   pip install pygame")
except Exception as e:
    print(f"❌ ERREUR: {e}")
