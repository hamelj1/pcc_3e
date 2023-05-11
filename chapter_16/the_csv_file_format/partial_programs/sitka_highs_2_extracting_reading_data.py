from pathlib import Path
import csv


path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_16/the_csv_file_format/partial_programs/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

print(highs)
