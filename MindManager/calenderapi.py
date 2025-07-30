# calendar_api.py

import datetime
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from event_extractor import extract_events_from_llm_output

SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def create_event(service, event):
    title = event["title"]
    start = event["start"]
    end = event["end"]
    location = event["location"]
    description = event["description"]

    today = datetime.date.today().isoformat()
    all_day = False
    recurring = False

    if not start:
        start = today
        end = today
        all_day = True
        recurring = True
    elif "T" not in start:
        all_day = True
        end = start

    if all_day:
        calendar_event = {
            'summary': title,
            'location': location,
            'description': description,
            'start': {'date': start, 'timeZone': 'Asia/Kolkata'},
            'end': {'date': end, 'timeZone': 'Asia/Kolkata'},
        }
    else:
        calendar_event = {
            'summary': title,
            'location': location,
            'description': description,
            'start': {'dateTime': start, 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': end, 'timeZone': 'Asia/Kolkata'},
        }

    if recurring:
        calendar_event['recurrence'] = ['RRULE:FREQ=DAILY']

    created_event = service.events().insert(calendarId='primary', body=calendar_event).execute()
    print(f"✅ Created: {title} ({created_event.get('htmlLink')})")

def main():
    service = authenticate_google()

    print("📝 Enter your full reflection:")
    reflection = input("You: ")

    print("\n🤖 Paste LLM output (CREATE_EVENT lines, one per line):")
    lines = []
    while True:
        line = input()
        if line.strip().lower() in ['done', '']:
            break
        lines.append(line)
    llm_output = "\n".join(lines)

    events = extract_events_from_llm_output(llm_output)

    if not events:
        print("⚠️ No valid events detected.")
        return

    for e in events:
        try:
            create_event(service, e)
        except Exception as err:
            print(f"❌ Failed to create event: {e['title']}")
            print("   ↳", err)

if __name__ == "__main__":
    main()
