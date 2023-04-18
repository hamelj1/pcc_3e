from pathlib import Path


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('C:/Users/jhamel/Documents/GitHub/pcc_3e/chapter_10/writing_to_a_file/programming.txt')
path.write_text(contents)