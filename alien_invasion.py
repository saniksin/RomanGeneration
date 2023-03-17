import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from life import Live

def run_game():
    #Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)) 
    pygame.display.set_caption("Roman Generation")
    #Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Играть")
    #Cоздание экземпляра для хранения игровой статистики
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    #Cоздание корабля
    ship = Ship(ai_settings, screen)
    live = Live(ai_settings, screen)
    #Cоздание группы для хранения пуль
    bullets = Group()
    aliens = Group()
    #Cоздание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Запуск основного цикла игры.
    while True:
        #Отслеживание событий клавиатуры и мыши.
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            #Обновление и удаление пуль
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #Обновление позиции пришельца
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            #При каждом проходе цикла перерисовыется экран.
            #Отображение последнего прорисованого экрана.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                              bullets, play_button, live)
        

run_game()
