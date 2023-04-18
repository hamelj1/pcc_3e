from pathlib import Path


path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/partial_programs/reading_from_a_file/pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)