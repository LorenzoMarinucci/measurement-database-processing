from enum import Enum


class DatasetColumns(Enum):
    G_POA: str = "G_POA_norm"
    AIR_TEMP: str = "air_temp_norm"
    WIND_SPEED: str = "wind_s_norm"
    HUMIDITY: str = "humidity_norm"
    DECLINATION: str = "declination_norm"
    POWER: str = "power_norm"
    DATENUM: str = "datenum"
    DATETIME: str = "datetime"


class DatasetScale(Enum):
    G_POA: int = 2000
    AIR_TEMP: int = 50
    WIND_SPEED: int = 100
    HUMIDITY: int = 100
    DECLINATION: int = 30
    POWER: int = 2000


class DefaultValues(Enum):
    MAX_HOURS: str = '23:59:59'
    MIN_HOURS: str = '00:00:00'
