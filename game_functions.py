import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien
from star import Star
from random import randint


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reacts to the key hold"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fires a bullet if max limit is not reached"""
    # creating a new bullet and adding it in the group bullets
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    """Reacts to the key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False
    elif event.key == pygame.K_q:
        sys.exit()



def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
    """ Handles clicks and keyboard events """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)




def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
    """Starts a new game on Play button click"""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # settings reset
        ai_settings.initialize_dynamic_settings()
        # hide cursor
        pygame.mouse.set_visible(False)
        # stats reset
        stats.reset_stats()
        stats.game_active = True

        # cleans lists of aliens and bullets
        aliens.empty()
        bullets.empty()

        # creates new fleet and places new ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()



def create_stars(ai_settings, screen, stars):
    """Creates stars group"""
    num_stars = 20
    for _ in range(num_stars):
        star = Star(ai_settings, screen)
        star.rect.x = randint(0, ai_settings.screen_width)
        star.rect.y = randint(0, ai_settings.screen_height)
        stars.add(star)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, stars, play_button):
    """Updates images and screen """
    # with each iteration screen is redrawn
    screen.fill(ai_settings.bg_color)

    # all bullets are shown behind ship and ufo
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    stars.draw(screen)
    ship.blitme()
    aliens.draw(screen)

    # Play button displayed if game is inactive
    if not stats.game_active:
        play_button.draw_button()

    # demonstrating last screen
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """Updates bullets positions and deletes old bullets"""
    # updates bullet position
    bullets.update()

    # deleting bullets outside screen
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Checking collisions - if any, deletes bullet and alien"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # Deletes existing bullets and creates new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    """Calculates the number of aliens in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Defines number of rows on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creates an alien and places it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """Creates an aliens fleet """
    # Creating an alien and counting how many fit in a row
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Creating fleet
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Reacts to alien arriving to the screen edge"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Lowers fleet and changes direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, screen, stats, ship, aliens, bullets):
    """Handles ship-alien collision"""
    if stats.ships_left > 0:
        # reducing ships left
        stats.ships_left -= 1

        # cleans aliens and bullets lists
        aliens.empty()
        bullets.empty()

        # creates new fleet and puts ship in center
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # pause
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Checks if aliens reached bottom screen"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # same as ship collision happens
            ship_hit(ai_settings, screen, stats, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    Checks if fleet is at the screen edge
    and updates positions of all aliens
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # checking collisions ship-alien
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, screen, stats, ship, aliens, bullets)

    # checking aliens at bottom screen
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)