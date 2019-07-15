sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()# spliting words
lengthof_words = [len(word) for word in words]
not_the = [len(word) for word in words if word != "the"]

print(words)
print(lengthof_words)
print(not_the)

print()

numbers = [34.6,-203.4,44.9,68.3,-12.2, 44.6, 12.7]
print([ number for number in numbers if number>=0])

print()

numbers = [12, 54, 33, 67, 24, 89, 11, 24, 47]
print([even_number for even_number in numbers if even_number % 2 == 0])
print()

words = ["hello", "my", "name", "is", "Sam"]
print([(word.upper(),len(word)) for word in words])