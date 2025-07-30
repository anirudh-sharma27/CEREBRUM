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
# event_extractor.py

def clean(text):
    for prefix in ["i have to:", "i need to:", "i must:", "I have to:", "I need to:", "I must:"]:
        if text.lower().startswith(prefix):
            return text[len(prefix):].strip()
    return text.strip()

def extract_events_from_llm_output(llm_output: str):
    """
    Parses LLM output into a list of structured event dictionaries.
    Each line should follow:
    CREATE_EVENT|title|start|end|location|description
    """
    events = []
    lines = llm_output.strip().split("\n")
    for line in lines:
        if not line.strip().startswith("CREATE_EVENT"):
            continue
        try:
            _, title, start, end, location, description = line.strip().split("|")
            events.append({
                "title": clean(title),
                "start": start.strip(),
                "end": end.strip(),
                "location": clean(location),
                "description": clean(description)
            })
        except ValueError:
            print(f"⚠️ Skipping invalid line: {line}")
    return events
