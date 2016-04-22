# soundcloud-fillset

Take one of your existing playlists in SoundCloud, make a new, huge one using the *related tracks* functionality.


## Dependencies

You'll need Python 3.4 installed in your machine. On Ubuntu, run:

    sudo apt-get install python3.4 python3.4-venv

Then create a virtual environment and install the Python dependencies, by running `source .env`.


## Configuration

First, create an app using <http://soundcloud.com/you/apps/new>. Create a `settings.py` file (you can copy `settings.example.py` if you want), and fill it with your client id and secret.

Obtain an access token running:

```bash
source .env  # not necessary if you already ran it in this same console.
python get_access_token.py
```

And following the instructions.


## Usage

```bash
source .env  # not necessary if you already ran it in this same console.
python fillset.py
```
