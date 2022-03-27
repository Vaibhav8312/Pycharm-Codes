from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

Client_ID = os.environ["Client_ID"]
Client_Secret = os.environ["Client_Secret"]
URI = "http://127.0.0.1:9090"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=URI,
        client_id=Client_ID,
        client_secret=Client_Secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
date = input("Which year do you want to travel to? Type the date in this format YYY-MM-DD: ")

response = requests.get(url="https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")
song_names_h3 = soup.select("h3.c-title.a-no-trucate")
song_names = [item.get_text().strip() for item in song_names_h3]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
print(song_uris)
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)











# import requests
# from bs4 import BeautifulSoup
#
#
# def remove_values_from_list(the_list, val):
#     return [value for value in the_list if value != val]
#
#
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
#
# URL = f"https://www.billboard.com/charts/hot-100/{date}/"
#
# response = requests.get(URL)
# response.raise_for_status()
# response_text = response.text
#
# soup = BeautifulSoup(response_text, "html.parser")
#
# top_100_songs_names = soup.find_all(name="h3", class_="u-letter-spacing-0021", id="title-of-a-story")
# top_100_songs_names = [song.text.strip() for song in top_100_songs_names]
# top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Songwriter(s):')
# top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Producer(s):')
# top_100_songs_names = remove_values_from_list(top_100_songs_names, 'Imprint/Promotion Label:')
#
# top_100_songs_artist = soup.find_all(name="span", class_="u-letter-spacing-0021")
# top_100_songs_artist = [artist.text.strip() for artist in top_100_songs_artist]
# print(top_100_songs_names)
# print(top_100_songs_artist)

# from bs4 import BeautifulSoup
# import requests
#
# date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
#
# response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup.prettify())
# h3_tag = soup.find_all(name="h3", id="title-of-a-story")
# song_list = [i.getText().strip() for i in h3_tag[6: -16: 4]]
# print(len(song_list))
# print(song_list)
