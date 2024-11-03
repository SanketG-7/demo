# Counts occurrences of each character in a string
word = "programming"
char_count = {char: word.count(char) for char in set(word)}
print(char_count)
