from pathlib import Path
import json


numbers = [2, 3, 5, 7, 11, 13]

path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/storing_data/numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)