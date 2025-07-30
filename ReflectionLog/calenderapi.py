from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=0)
    service = build("calendar", "v3", credentials=creds)
    return service

def create_event(service, event):
    body = {
        "summary": event["title"],
        "description": event["description"],
        "location": event["location"],
        "start": {
            "dateTime": event["start"] if event["start"] else None,
            "timeZone": "Asia/Kolkata",
        },
        "end": {
            "dateTime": event["end"] if event["end"] else None,
            "timeZone": "Asia/Kolkata",
        }
    }

    # Fallback to all-day event if no start time
    if not event["start"] or not event["end"]:
        today = datetime.date.today().isoformat()
        body["start"] = {"date": today}
        body["end"] = {"date": today}

    created_event = service.events().insert(calendarId="primary", body=body).execute()
    print(f"✅ Created: {created_event.get('summary')} ({created_event.get('htmlLink')})")
