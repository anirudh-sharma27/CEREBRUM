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
    Expects event dict like:
    {
      "title": "Meeting with Kaushal",
      "date": "2025-09-07",
      "start_time": "09:00",
      "end_time": "10:00",
      "location": null
    }
    """

    # Build RFC3339 datetime strings
    start = f"{event['date']}T{event['starttime']}:00+05:30"
    end   = f"{event['date']}T{event['endtime']}:00+05:30"

    gcal_event = {
        "summary": event["event"],   # Required
        "start": {"dateTime": start, "timeZone": "Asia/Kolkata"},
        "end": {"dateTime": end, "timeZone": "Asia/Kolkata"},
    }

    # Add optional location if exists
    if event.get("location"):
        gcal_event["location"] = event["location"]

    # Debug: print before sending
    print(" Sending event:", json.dumps(gcal_event, indent=2))

    # Insert into calendar
    service.events().insert(calendarId="primary", body=gcal_event).execute()
    print(f"Added event: {event['event']} on {event['date']} at {event['starttime']}")

with open("events.json","r") as f:
    data = json.load(f)

for i in data:
    service = get_calendar_service()
    add_event(service,i)

