import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load the environment variables from your .env file
load_dotenv()

# 'scope' tells Spotify exactly what data we are asking permission to see.
scope = "user-top-read user-read-recently-played"

# Initialize the Spotify client and trigger the OAuth flow
print("Attempting to connect to Spotify...")
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# Test the connection by fetching your basic profile info
try:
    user_profile = sp.current_user()
    print(f"\nSuccess! Authenticated as: {user_profile['display_name']}")
except Exception as e:
    print(f"\nUh oh, something went wrong: {e}")