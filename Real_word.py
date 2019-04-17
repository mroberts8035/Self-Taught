import enchant

check = enchant.Dict('en_US')

print('This program will check to see if a word as you spelled it is in the United States English Dictionary.')

def word():
    while True:
        word = input('Type a word or press "q" to quit: ')
        if word.lower() != 'q':
            real = check.check(word)
            if real == True:
                print(f'{word} is a real word')

            else:
                print(f'{word} is not a real word, please try again')

        else:
            break
word()
