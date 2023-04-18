from pathlib import Path


path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/partial_programs/reading_from_a_file/pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))