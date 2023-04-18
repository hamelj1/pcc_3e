from pathlib import Path
import json


username = input("What is your name? ")

path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/storing_data/username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"We'll remember you when you come back, {username}!")