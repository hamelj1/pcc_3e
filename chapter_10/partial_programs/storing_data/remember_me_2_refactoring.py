from pathlib import Path
import json


def greet_user():
    """Greet the user by name."""
    path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/storing_data/username.json')
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        contents = json.dumps(username)
        path.write_text(contents)
        print(f"We'll remember you when you come back, {username}!")

greet_user()