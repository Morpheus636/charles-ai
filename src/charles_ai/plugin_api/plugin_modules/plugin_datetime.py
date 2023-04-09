import datetime


spec = {"plugin": "datetime", "description": "Fetches the current date and time.", "args": {}}


def run(**kwargs):
    return f"Current date and time: {datetime.datetime.now().strftime('%I:%M %p on %B %d, %Y')}"
