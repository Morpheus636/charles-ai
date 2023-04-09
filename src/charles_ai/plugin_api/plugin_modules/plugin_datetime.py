import datetime


spec = {
    "plugin": "datetime",
    "description": "Fetches the current date and time.",
    "args": {
        "timezone_offset": "Signed integer representing the conversion from UTC to the requested timezone."
    },
}


def run(**kwargs):
    tz_offset = kwargs.get("timezone_offset")
    if not tz_offset:
        tz_offset = 0
    tzinfo = datetime.timezone(datetime.timedelta(hours=int(tz_offset)))
    return (
        f"Current date and time: {datetime.datetime.now(tzinfo).strftime('%I:%M %p on %B %d, %Y')}"
    )
