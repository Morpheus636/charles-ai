import wikipediaapi


spec = {
    "plugin": "wikipedia",
    "description": "Gets the summary of a wikipedia page. Use this plugin when you need more information than you know, or if the user asks you to look something up.",
    "args": {
        "page_name": "The title of the wikipedia page to get. Try guessing this based on context before explicitly asking the user for it."
    },
}


def run(**kwargs):
    wiki = wikipediaapi.Wikipedia("en")
    page = wiki.page(kwargs["page_name"])
    if page.exists():
        return page.summary
    else:
        return "The requested Wikipedia page does not exist. Try using a different page_name."
