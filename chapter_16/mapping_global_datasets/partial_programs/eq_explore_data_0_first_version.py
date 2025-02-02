from pathlib import Path
import json


# Read data as a string and convert to a Python object.
path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_16/mapping_global_datasets/partial_programs/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_16/mapping_global_datasets/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)