# Install the Library : pyspellchecker using cmd = "pip install pyspellchecker"

from spellchecker import SpellChecker

spell = SpellChecker()

input_file = open("data.txt", "r")

list_of_word_lists = []
for line in input_file:
    stripped_line = line.strip()
    line_list = stripped_line.split()
    list_of_word_lists.append(line_list)

input_file.close()

# find those words that may be misspelled
count = 0

for word_list in list_of_word_lists:
    misspelled = spell.unknown(word_list)
    for word in misspelled:
        count += 1
        print(f'{word} : {spell.correction(word)}')

        # most likely words near to misspelled one.
        print(f'Recommended Word List for misspelled one : {spell.candidates(word)}')


print("\n Total misspelled words = ", count)
