class GameStats():
    """Отслеживание статистики для игры"""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Игра запускается в активном состоянии
        self.game_active = False
        self.high_score = self.check_rec()

    def reset_stats(self):
        """Инициализирует статистику изменяющуюся в ходе игры"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        
    def check_rec(self):
        try:
            with open('record.txt') as file_object:
                content = file_object.readline()
                if content:
                    return int(content)
                else:
                    return 0
        except FileNotFoundError:
            return 0
    
