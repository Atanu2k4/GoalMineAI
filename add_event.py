from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Define the scope for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path to credentials.json
CREDENTIALS_FILE = "goalmine-eb217a5e03d2.json"  # Ensure this file exists

# Use your correct Calendar ID
CALENDAR_ID = "4166e51bea32a731aa853a6a2d5b1580b3a2f3b9679155f4c86312721ea8dcf2@group.calendar.google.com"

def add_event(summary, start_time, duration=1, description=""):
    """Adds an event to Google Calendar."""
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)

    # Convert start_time to RFC3339 format (Google Calendar standard)
    start_datetime = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
    end_datetime = start_datetime + timedelta(hours=duration)

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_datetime.isoformat(),
            'timeZone': 'Asia/Kolkata',  # Change based on your timezone
        },
        'end': {
            'dateTime': end_datetime.isoformat(),
            'timeZone': 'Asia/Kolkata',
        }
    }

    # Insert event into Google Calendar
    event_result = service.events().insert(calendarId=CALENDAR_ID, body=event).execute()

    print(f"✅ Event added successfully! View it here: {event_result.get('htmlLink')}")

if __name__ == "__main__":
    # Example: Add an event for testing
    add_event(
        summary="AI Project Meeting",
        start_time="2025-02-25 17:00",  # Format: YYYY-MM-DD HH:MM (24-hour format)
        duration=2, #How much time required in hour
        description="Discussion on AI assistant development"
    )
