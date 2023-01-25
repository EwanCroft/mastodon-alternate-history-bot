import random
import json
import configparser
import os
from mastodon import Mastodon

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if not os.path.exists(rf'{ROOT_DIR}\config.ini'):
    url = input("Enter the URL of your Mastodon instance:\n")
    email = input("Enter your email address:\n")
    password = input("Enter your password:\n")
    
    app_info = Mastodon.create_app(
        "Post Nuke",
        api_base_url = f"{url}"
    )
    client_id, client_secret = app_info

    mastodon = Mastodon(client_id=client_id, client_secret=client_secret, api_base_url=url)
    access_token = mastodon.log_in(email, password)

    config = configparser.ConfigParser()
    config['MASTODON'] = {'url': url,
                          'email': email,
                          'password': password,
                          'client_id': client_id,
                          'client_secret': client_secret,
                          'access_token': access_token}
    
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

config = configparser.ConfigParser()
config.read(rf'{ROOT_DIR}\config.ini')
url = config['MASTODON']['url']
email = config['MASTODON']['email']
password = config['MASTODON']['password']
client_id_str = config['MASTODON']['client_id']
client_secret_str = config['MASTODON']['client_secret']
access_token_str = config['MASTODON']['access_token']

mastodon = Mastodon(client_id=client_id_str, client_secret=client_secret_str, access_token=access_token_str, api_base_url=url)