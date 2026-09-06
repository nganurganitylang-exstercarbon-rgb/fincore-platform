from datetime import datetime
from typing import Optional


def surge_multiplier(now: Optional[datetime] = None) -> float:
       """Peak hours (9-11am, 5-7pm) apply a 1.25x multiplier; otherwise 1.0x."""
       now = now or datetime.now()
       hour = now.hour
       if 9 <= hour < 11 or 17 <= hour < 19:
           return 1.25
       return 1.0
