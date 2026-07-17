from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo

from app.core.config import settings

def utc_now() -> datetime:
    """Get the current UTC time."""

    return datetime.now(timezone.utc)

def get_timezone() -> ZoneInfo:
    """Get the timezone from settings."""

    return ZoneInfo(settings.APP_TIMEZONE)

def local_now() -> datetime:
    """Get the current local time based on the configured timezone."""

    return utc_now().astimezone(get_timezone())

def to_app_timezone(value: datetime) -> datetime:
    """Convert a UTC datetime to the application's configured timezone."""

    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)

    return value.astimezone(get_timezone())

def add_minutes(value: datetime, minutes: int) -> datetime:
    """Add minutes to a datetime object."""

    return value + timedelta(minutes=minutes)

def add_days(value: datetime, days: int) -> datetime:
    """Add days to a datetime object."""

    return value + timedelta(days=days)
