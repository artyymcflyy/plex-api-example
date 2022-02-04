from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
from plexapi import (CONFIG)
import sys

##Config set in ~/.config/plexapi/config.ini
#https://python-plexapi.readthedocs.io/en/latest/configuration.html

#Setup MyPlex (Object)
account = MyPlexAccount()

# Setup a connection to devices
remote_plex_server = PlexServer(token=CONFIG.get('auth.remote_server_token'))
my_plex_server = PlexServer(baseurl=CONFIG.get('auth.client_baseurl'), token=CONFIG.get('auth.server_token'))
my_client = my_plex_server.client(CONFIG.get('header.device_name'))


# Search the remote plex server for a movie (aladdin)
movie_title = (sys.argv[1] if len(sys.argv) > 1 else 'Aladdin')
found_movie = remote_plex_server.library.section('Movies').search(movie_title)

# Create a PlayQueue on the server you want to play content from 
# in order to play media from a remote server
remote_play_queue = remote_plex_server.createPlayQueue(item=found_movie)

# Use the client to play media in the playQueue on the specified remote server
my_client.playMedia(media=remote_play_queue, token=remote_plex_server.createToken(), machineIdentifier=remote_plex_server.machineIdentifier)

print(f'now playing media: {remote_play_queue.selectedItem.title}')
