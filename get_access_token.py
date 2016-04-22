import sys
import soundcloud
from getpass import getpass
try:
    import settings
except:
    print('Did you create settings.py from settings.example.py?')
    raise

print('Enter your SoundCloud username and password, an access_token will be generated')
username = input('username: ')
password = getpass('password: ')
try:
    client = soundcloud.Client(client_id=settings.client_id, client_secret=settings.client_secret, username=username, password=password)
except Exception as e:
    print('Unable to login. {}'.format(e))
    sys.exit(1)

new_settings = ''
with open('./settings.py', 'r') as settings_file:
    for line in settings_file:
        kv = tuple((k.strip() for k in line.split('=')))
        if len(kv) != 2 or kv[0] != 'access_token':
            new_settings += line
        else:
            new_settings += "access_token = '{}'\n".format(client.token.access_token)
with open('./settings.py', 'w') as settings_file:
    settings_file.write(new_settings)

print('Token saved on settings.py. Now go and use the app!')
