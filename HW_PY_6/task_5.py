# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
s = input()
filter_ = 'абв'


def find_letters(text):
    text = text.split(' ')
    func = lambda word: 'абв' not in word
    return ' '.join(list(filter(func, text)))

print(find_letters(s))