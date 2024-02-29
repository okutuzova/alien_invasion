import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
import game_functions as gf




def run_game():
    """Initializes a game"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # creates Play button
    play_button = Button(ai_settings, screen, "Play")



    # creates a game statistics object
    stats = GameStats(ai_settings)

    # creating a ship
    ship = Ship(ai_settings, screen)
    # creating a group for bullets
    bullets = Group()
    # creating an alien fleet
    aliens = Group()
    stars = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.create_stars(ai_settings, screen, stars)


# Main game start


    while True:
        # following keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, stars, play_button)


run_game()
