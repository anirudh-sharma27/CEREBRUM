#All of this needs revision ok

import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these SCOPES, delete token.json
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google():
    creds = None
    # Load credentials from token.json if available
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If no valid credentials
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return build('calendar', 'v3', credentials=creds)

def create_event(service, summary, start_time_str, duration_minutes=60):
    start_time = datetime.datetime.fromisoformat(start_time_str)
    end_time = start_time + datetime.timedelta(minutes=duration_minutes)

    event = {
        'summary': summary,
        'start': {'dateTime': start_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
        'end': {'dateTime': end_time.isoformat(), 'timeZone': 'Asia/Kolkata'},
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created:', created_event.get('htmlLink'))



from event_extractor import extract_goal_and_date

if __name__ == '__main__':
    service = authenticate_google()

    user_input = "remember the year is 2025"+input("Type your reflection: ")

    goal, date_str = extract_goal_and_date(user_input)

    if goal and date_str:
        print(f"\n📌 Detected goal: {goal}")
        print(f"📅 Detected deadline: {date_str}")

        confirm = input("Would you like me to add this to your calendar? (yes/no): ").lower()
        if confirm == "yes":
            create_event(service, goal, date_str)
        else:
            print("Okay, not added.")
    else:
        print("No clear goal or date found in your input.")

