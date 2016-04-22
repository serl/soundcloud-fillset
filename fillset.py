import soundcloud
import random
import time
try:
    import settings
    client = soundcloud.Client(access_token=settings.access_token)
except:
    print('Did you create settings.py from settings.example.py? Did you then run get_access_token.py?')
    raise


def main(include_original_songs=False):
    all_playlists = client.get('/me/playlists')
    playlists = [p for p in all_playlists if not p.title.endswith(' fillset')]

    for i, p in enumerate(playlists, start=1):
        print('{}: {p.title} ({} tracks, {p.sharing})'.format(i, len(p.tracks), p=p))
    print()

    playlist = None
    while playlist is None:
        pl_id = input('Select a playlist (1-{}): '.format(len(playlists)))
        try:
            playlist = playlists[int(pl_id) - 1]
            break
        except (ValueError, IndexError):
            print("Sorry, I didn't get it...")

    playlist_auto_search = [p for p in all_playlists if p.title == playlist.title + ' fillset']
    if len(playlist_auto_search) > 0:
        print("Playlist already existing.")
        playlist_auto = playlist_auto_search[0]
        playlist_auto_tracks = [t['id'] for t in playlist_auto.tracks]
    else:
        print('Creating a new playlist...')
        playlist_auto = client.post('/playlists', playlist={'sharing': 'private', 'title': '{} fillset'.format(playlist.title)})
        playlist_auto_tracks = []

    for i, track in enumerate(playlist.tracks, start=1):
        print('Fetching related tracks... {}/{}'.format(i, len(playlist.tracks)), end='\r')
        playlist_auto_tracks.append(track['id'])
        related_tracks = client.get('/tracks/{}/related'.format(track['id']))
        for rel_track in related_tracks:
            playlist_auto_tracks.append(rel_track.id)
        time.sleep(.2)
    print('Fetching related tracks... completed.')
    # remove duplicates
    playlist_auto_tracks = set(playlist_auto_tracks)
    if not include_original_songs:
        playlist_auto_tracks -= set([t['id'] for t in playlist.tracks])
    # limit to 500 or explode the API
    playlist_auto_tracks = list(playlist_auto_tracks)[:500]
    random.shuffle(playlist_auto_tracks)
    print('Adding {} tracks to the playlist...'.format(len(playlist_auto_tracks)), end='', flush=True)
    client.put(playlist_auto.uri, playlist={'tracks': [{'id': x} for x in playlist_auto_tracks]})
    print(' done.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting...')
