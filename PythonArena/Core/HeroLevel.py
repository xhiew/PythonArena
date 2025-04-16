class HeroLevel:
    def __init__(self, level: int):
        self._level = min(max(level, 1), 15)

    @property
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value: int):
        self._level = min(max(value, 1), 15)