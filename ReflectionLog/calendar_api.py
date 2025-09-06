import os
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# --- Google Calendar Setup ---
SCOPES = ["https://www.googleapis.com/auth/calendar"]

def get_calendar_service():
    creds = None
    # token.json stores the user's access/refresh tokens
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    service = build("calendar", "v3", credentials=creds)
    return service

# --- Add Events to Calendar ---
def add_event(service, event):
    """
    Expects event dict with:
    {
      "title": "...",
      "date": "YYYY-MM-DD",
      "start_time": "HH:MM",
      "end_time": "HH:MM",
      "location": null or "place"
    }
    """
    start = f"{event['date']}T{event['start_time']}:00+05:30"
    end   = f"{event['date']}T{event['end_time']}:00+05:30"

    gcal_event = {
        "summary": event["title"],
        "start": {"dateTime": start, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end, "timeZone": "Asia/Kolkata"},
    }

    if event.get("location"):
        gcal_event["location"] = event["location"]

    service.events().insert(calendarId="primary", body=gcal_event).execute()
    print(f"✅ Added event: {event['title']} on {event['date']} at {event['start_time']}")

# --- Main ---
if __name__ == "__main__":
    # Example: events extracted from LLM
    reflection_events = """
    [
      {"title": "Buy 5 eggs", "date": "2025-09-07", "start_time": "09:00", "end_time": "21:00", "location": null},
      {"title": "Finish Cerebrum project", "date": "2025-09-09", "start_time": "09:00", "end_time": "21:00", "location": null},
      {"title": "Meeting with Kaushal", "date": "2025-09-06", "start_time": "21:00", "end_time": "22:00", "location": null}
    ]
    """

    events = json.loads(reflection_events)
    service = get_calendar_service()

    for e in events:
        add_event(service, e)
