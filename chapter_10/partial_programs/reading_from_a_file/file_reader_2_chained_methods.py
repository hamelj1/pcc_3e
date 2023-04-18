from pathlib import Path

pathname = 'C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/partial_programs/reading_from_a_file/pi_digits.txt'
path = Path(pathname)
contents = path.read_text().rstrip()
print(contents)