
phrase = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
          "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

words = phrase.split()

print(words)

for word in words:
    new_words = []
    word_ing = word.strip(',.') + 'ing'
    new_words.append(word_ing)
    new_phrase = ' '.join(new_words)

    print(new_phrase, end=' ')
