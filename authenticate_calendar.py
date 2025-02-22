from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define the scope for Google Calendar API
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Path to your downloaded credentials.json file
CREDENTIALS_FILE = "goalmine-eb217a5e03d2.json"

def authenticate_google_calendar():
    """Authenticates Google Calendar API and returns the service object."""
    creds = service_account.Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=creds)
    print("✅ Google Calendar API authenticated successfully!")
    return service

if __name__ == "__main__":
    authenticate_google_calendar()
