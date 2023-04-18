from pathlib import Path
import json


path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/storing_data/username.json')
contents = path.read_text()
username = json.loads(contents)

print(f"Welcome back, {username}!")