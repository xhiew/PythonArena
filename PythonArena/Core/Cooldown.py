from abc import ABC, abstractmethod
from datetime import datetime

class Cooldown(ABC):
    @property
    @abstractmethod
    def cooldown_time(self) -> float:
        """Thời gian hồi chiêu (giây)"""
        pass

    @property
    @abstractmethod
    def last_used_time(self) -> datetime | None:
        """Lần cuối dùng kỹ năng"""
        pass

    @property
    def is_skill_available(self) -> bool:
        return self.remaining_cooldown == 0

    @property
    def remaining_cooldown(self) -> float:
        if self.last_used_time is None:
            return 0.0
        elapsed = (datetime.now() - self.last_used_time).total_seconds()
        return max(0.0, self.cooldown_time - elapsed)