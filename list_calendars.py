from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
CREDENTIALS_FILE = "goalmine-eb217a5e03d2.json"
CALENDAR_ID = "4166e51bea32a731aa853a6a2d5b1580b3a2f3b9679155f4c86312721ea8dcf2@group.calendar.google.com"  # Use your calendar ID

def list_specific_calendar():
    """Fetch and display details of the specific calendar."""
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)

    try:
        calendar = service.calendars().get(calendarId=CALENDAR_ID).execute()
        print(f"✅ Calendar Found: {calendar['summary']} (ID: {calendar['id']})")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    list_specific_calendar()
