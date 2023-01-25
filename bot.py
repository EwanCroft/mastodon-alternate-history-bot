import random
import json
import configparser
import os
from mastodon import Mastodon
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
country_list = os.path.join(ROOT_DIR, "countries.json")
year = 1900

if not os.path.exists(rf'{ROOT_DIR}\config.ini'):
    url = input("Enter the URL of your Mastodon instance:\n")
    email = input("Enter your email address:\n")
    password = input("Enter your password:\n")
    
    app_info = Mastodon.create_app(
        "Alternate History bot",
        api_base_url = f"{url}"
    )
    client_id, client_secret = app_info

    mastodon = Mastodon(client_id=client_id, client_secret=client_secret, api_base_url=url)
    access_token = mastodon.log_in(email, password)

    config = configparser.ConfigParser()
    
    if not config.has_section('MASTODON'):
        config.add_section('MASTODON')
        config['MASTODON'] = {
            'url': url,
            'email': email,
            'password': password,
            'client_id': client_id,
            'client_secret': client_secret,
            'access_token': access_token
        }
    if not config.has_section('YEAR'):
        config.add_section('YEAR')
        config['YEAR'] = {
            'YEAR': year
        }

    with open(rf'{ROOT_DIR}\config.ini', 'w') as configfile:
        config.write(configfile)

config = configparser.ConfigParser()
config.read(rf'{ROOT_DIR}\config.ini')
url = config['MASTODON']['url']
email = config['MASTODON']['email']
password = config['MASTODON']['password']
client_id_str = config['MASTODON']['client_id']
client_secret_str = config['MASTODON']['client_secret']
access_token_str = config['MASTODON']['access_token']
year = config['YEAR']['YEAR']

with open(country_list, 'r') as f:
    data = json.load(f)

mastodon = Mastodon(client_id=client_id_str, client_secret=client_secret_str, access_token=access_token_str, api_base_url=url)

country_a = ""
country_b = ""

while True:
    while True:
        continent = random.choice(["Africa", "Europe", "North America", "South America", "Antartica", "Oceania", "Asia"])
            
        if continent == "Africa":
            while True:
                country_a = random.choice(data["Africa"])
                country_b = random.choice(data["Africa"])
                
                print(country_a, country_b)
                
                if country_b == country_a:
                    continue
                else:
                    break
            
        elif continent == "Europe":
            while True:
                country_a = random.choice(data["Europe"])
                country_b = random.choice(data["Europe"])
                
                print(country_a, country_b)
                
                if country_b == country_a:
                    continue
                else:
                    break
            
        elif continent == "North America":
            while True:
                country_a = random.choice(data["North America"])
                country_b = random.choice(data["North America"])
                
                print(country_a, country_b)
                    
                if country_b == country_a:
                    continue
                else:
                    break
            
        elif continent == "South America":
            while True:
                country_a = random.choice(data["South America"])
                country_b = random.choice(data["South America"])
                
                print(country_a, country_b)
                
                if country_b == country_a:
                    continue
                else:
                    break

        elif continent == "Asia":
            while True:
                country_a = random.choice(data["Asia"])
                country_b = random.choice(data["Asia"])
                
                print(country_a, country_b)
                    
                if country_b == country_a:
                    continue
                else:
                    break

        elif continent == "Oceania":
            while True:
                country_a = random.choice(data["Oceania"])
                country_b = random.choice(data["Oceania"])
                
                print(country_a, country_b)
                    
                if country_b == country_a:
                    continue
                else:
                    break
        
        break
    
    with open(rf"{ROOT_DIR}\scenarios.json", "r") as f:
        data = json.load(f)

    nature_of_action = ["peaceful", "hostile"]
    nature = random.choice(nature_of_action)
    scenario = str(random.choice(data[nature]))

    scenario = scenario.replace("{{country_a}}", country_a).replace("{{country_b}}", country_b)
    post_text = f"{year}:\n{scenario}\n\n#AlternateHistory"

    try:
        mastodon.status_post(spoiler_text = "Alternate history scenario", status = post_text)
    except Exception as e:
        print(e)
    
    config = configparser.ConfigParser()
    config.read(rf'{ROOT_DIR}\config.ini')
    year = int(config.get('YEAR', 'YEAR')) + 1
    config.set('YEAR', 'YEAR', str(year))

    with open(rf'{ROOT_DIR}\config.ini', 'w') as configfile:
        config.write(configfile)

    
    time.sleep(3600)