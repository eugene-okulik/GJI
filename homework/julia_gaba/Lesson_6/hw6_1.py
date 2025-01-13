
text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel."
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")

print(type(text))
words = text.split()

print(words)

new_text = []
for word in words:

    word_ing = word.strip(',.') + 'ing'

    if word.endswith(','):
        word_ing += ','
    elif word.endswith('.'):
        word_ing += '.'

    new_text.append(word_ing)

new_text = ' '.join(new_text)

print(new_text)
