from pathlib import Path
import json

path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/storing_data/numbers.json')
contents = path.read_text()
numbers = json.loads(contents)

print(numbers)