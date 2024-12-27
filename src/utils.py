from datetime import datetime, timezone

def parse_date(date_string):
    """Parse an ISO 8601 date string and return a localized datetime object."""
    return datetime.fromisoformat(date_string.replace("Z", "+00:00"))

def format_datetime(dt):
    """Format a datetime object into a readable string."""
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def is_future_date(date_string):
    """Check if a given ISO 8601 date string is in the future."""
    now = datetime.now(timezone.utc)
    game_date = parse_date(date_string)
    return game_date > now
