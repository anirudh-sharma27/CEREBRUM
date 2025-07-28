import re
from datetime import datetime
from dateutil import parser as date_parser

def extract_goal_and_date(text):
    """
    Very basic rule-based extraction using regex and dateutil parser.
    Returns a tuple (goal, date) or (None, None)
    """
    # Try to extract date
    try:
        date = date_parser.parse(text, fuzzy=True)
    except:
        date = None

    # make this the way you talk
    goal_phrases = ["I will", "I have to", "I plan to", "I'm going to", "I want to"]
    for phrase in goal_phrases:
        if phrase in text:
            idx = text.find(phrase)
            goal = text[idx:]
            goal = re.split(r'\bby\b|\bon\b|\bat\b|\bbefore\b', goal)[0].strip()
            return goal, date.strftime("%Y-%m-%dT%H:%M:%S") if date else None

    return None, None
