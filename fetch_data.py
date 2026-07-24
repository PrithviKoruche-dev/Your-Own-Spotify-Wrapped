import os
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# 1. Authenticate using the cached token
load_dotenv()
scope = "user-top-read user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

print("Fetching your top artists from the last 6 months...\n")
top_artists = sp.current_user_top_artists(limit=50, time_range='medium_term')

# 2. Extract the relevant data
artist_list = []
for artist in top_artists['items']:
    artist_list.append({
        'Artist': artist['name'],
        'Popularity': artist['popularity'],
        'Genres': ", ".join(artist['genres'])
    })

# 3. Load into a DataFrame for analytics
df = pd.DataFrame(artist_list)

# 4. Calculate custom metrics
df['Obscurity Score'] = 100 - df['Popularity']
overall_obscurity = df['Obscurity Score'].mean()

# 5. Output the results
print(f"=== YOUR OVERALL OBSCURITY SCORE: {overall_obscurity:.1f} / 100 ===\n")

print("Your Top 5 Most Obscure Artists:")
obscure_df = df.sort_values(by='Obscurity Score', ascending=False).head(5)
print(obscure_df[['Artist', 'Obscurity Score', 'Genres']].to_string(index=False))