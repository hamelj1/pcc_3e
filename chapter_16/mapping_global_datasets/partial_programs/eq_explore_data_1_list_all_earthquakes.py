from pathlib import Path
import json


# Read data as a string and convert to a Python object.
path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_16/mapping_global_datasets/partial_programs/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)

# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))
