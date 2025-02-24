from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Define the scope for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path to credentials.json
CREDENTIALS_FILE =  "goalmine-eb217a5e03d2.json"

def get_upcoming_events():
    """Fetches upcoming events from Google Calendar."""
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)

    # Get the current time
    now = datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    print("Fetching upcoming events...")

    # Fetch events from the primary calendar
    events_result = service.events().list(
        calendarId="4166e51bea32a731aa853a6a2d5b1580b3a2f3b9679155f4c86312721ea8dcf2@group.calendar.google.com", timeMin=now,
        maxResults=10, singleEvents=True,
        orderBy='startTime').execute()

    events = events_result.get('items', [])

    if not events:
        print("❌ No upcoming events found.")
        return

    print("✅ Upcoming Events:")
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f"- {start}: {event['summary']}")

if __name__ == "__main__":
    get_upcoming_events()
