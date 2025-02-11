from datetime import datetime, timedelta, timezone

def get_date_days_ago_ms(days, years):
    date_seven_years_ago = datetime.now(timezone.utc) - timedelta(days=days*years)
    date_miliseconds = int(date_seven_years_ago.timestamp() * 1000)
    return date_miliseconds