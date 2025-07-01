
from datetime import datetime

def calculate_lunar_phase(birthdate: datetime) -> str:
    days_since_new = (birthdate - datetime(2001, 1, 1)).days % 29.53
    if days_since_new < 1.84566:
        return "New Moon"
    elif days_since_new < 5.53699:
        return "Waxing Crescent"
    elif days_since_new < 9.22831:
        return "First Quarter"
    elif days_since_new < 12.91963:
        return "Waxing Gibbous"
    elif days_since_new < 16.61096:
        return "Full Moon"
    elif days_since_new < 20.30228:
        return "Waning Gibbous"
    elif days_since_new < 23.99361:
        return "Last Quarter"
    elif days_since_new < 27.68493:
        return "Waning Crescent"
    else:
        return "New Moon"
