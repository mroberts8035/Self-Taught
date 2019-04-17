import random

quote_list = {'author': ['"The first draft is just you telling yourself the story." -Terry Pratchett',
                         '"You can always edit a bad page, you can\'t edit a blank page." -Jodi Picoult',
                         '"Start writing, no matter what. The water does not flow until the faucet is turned on." -Louis L\'Amour',
                         '"There is no grater agony than bearing an untold story inside you." -Maya Angelou',
                         '"A professional writter is an amateur who didn\'t quit." -Richard Bach'],
              'musician': ['"The music is not in the notes, but in the silence between." -Wolfgang Amadeus Mozart',
                           '"Imagination creates reality." -Richard Wagner',
                           '"If everything was perfect, you would never learn and you would never grow." -Beyonce',
                           '"You can\'t knock on opportunity\'s door and not be ready." -Bruno Mars',
                           '"What\'s money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do." -Bob Dylan'],
              'entrepreneur': ['"You have to see failure as the beginning and the middle, but never entertain it as an end." -Jessica Herrin',
                               '"People are the most important thing. Business model and product will follow if you have the right people." -Adam Neumann',
                               '"Don\'t let others convince you that the idea is good when your gut tells you that it\'s bad" -Kevin Rose',
                               '"If you can offer a free tier that provides a lot of value, it will naturally help your product to spread much more rapidly." -Melanie Perkins,'
                               '"If we tried to think of a good idea, we wouldn\'t be able to think of a good idea. YOu just have to find the solution for a problem in your own life." -Brian Chesky']
              }


def quote():
    while True:
        selection = input('Here you can select a category to generate a quote from one of three categories.\n'
                          'please select "author", "musician", or "entrepreneur", select "q" to quit: ')
        if selection.lower() == 'q':
            print()
            print('Goodbye!')
            break
        elif selection in quote_list:
            print()
            print(quote_list[selection][random.randint(0, 4)])
            print()
        else:
            print()
            print('Please select a valid option')
            print()


quote()
