# soundcloud-fillset

Take one of your existing playlists in SoundCloud, make a new, huge one using the *related tracks* functionality.


## Dependencies

You'll need Python 3 installed in your machine. On Ubuntu, run:

```bash
sudo apt-get install python3 python3-venv python3-wheel
```

Then create a virtual environment and install the Python dependencies, by running `source .pyenv`.

If alternatively you have [direnv](https://direnv.net/) installed in your machine, `cd` and follow the instructions.


## Configuration

First, create an app using <http://soundcloud.com/you/apps/new>; create a `settings.py` file (you can copy `settings.example.py` if you want), and fill it with your client id and secret. Obtain an access token with:

```bash
source .pyenv  # not necessary if you already ran it in this same console or if you use direnv
python get_access_token.py
```


## Usage

```bash
source .pyenv  # not necessary if you already ran it in this same console or if you use direnv
python fillset.py
```
