from datetime import datetime
import re

def parse_datetime_or_default(dt_str):
    try:
        if dt_str:
            if "T" in dt_str:
                return dt_str  # full datetime
            else:
                # Only date provided, treat as all-day
                return dt_str
        else:
            return datetime.now().strftime("%Y-%m-%d")  # fallback to today
    except Exception:
        return datetime.now().strftime("%Y-%m-%d")

def extract_events_from_llm_output(llm_output):
    events = []
    for line in llm_output.strip().split("\n"):
        if not line.startswith("CREATE_EVENT"):
            continue
        try:
            _, title, start, end, location, description = line.split("|")
            start = parse_datetime_or_default(start.strip())
            end = parse_datetime_or_default(end.strip())
            event = {
                "title": title.strip(),
                "start": start,
                "end": end,
                "location": location.strip(),
                "description": description.strip(),
            }
            events.append(event)
        except Exception as e:
            print(f"⚠️ Skipping invalid line: {line}")
    return events
