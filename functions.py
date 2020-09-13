import random
from time import sleep


def read_formatted_file(self, file_name):
    print('\n' + '*' * 70)
    print()
    file = open('text_files/' + file_name + '.txt', 'r')
    myfile = f"{file.read()}".format(**locals())
    print(myfile)
    file.close()


def nothing(self):
    if self.matches < 1:
        print("You are out of matches. You sit in the dark and wonder why you just did that\n"
              "9 days pass and you die of dehydration.")
        exit()
    self.use_match()
    print(f"You sit and let the match burn out. Then you realize you should have done something.\n")
    if self.matches == 0:
        print('You have no matches left. You better choose wisely!')
    else:
        print(f"You only have {self.matches} matches left.")


def instructions():
    value = input('\nTo play, you can choose the words that are in CAPTIALS to make your decision.\n'
                  'Simply type the whole word OR just the first letter and press enter. Not case sensitive.\n'
                  'You can type QUIT(Q) at any time to quit the game.\n'
                  'Type YES(Y) if you understand or NO(N) if you do not:  ')
    value = value.lower()

    if value == 'yes':
        pass
    elif value == 'no':
        print("Well if you don't agree then you can't go on the adventure.")
        exit()
    elif value == 'quit':
        print('Good Bye')
        exit()
    else:
        print('invalid input, try again. you can chose from "quit", "yes", "no"')
        instructions()


def left(self):
    numbers = []
    read_formatted_file(self, 'left')
    numbers.append(int(input('Enter number one: ')))
    numbers.append(int(input('Enter number two: ')))
    numbers.append(int(input('Enter number three: ')))
    numbers.append(int(input('Enter number four: ')))
    numbers.append(int(input('Enter number five: ')))
    print('Your numbers are ' + ', '.join(str(x) for x in numbers))
    lottery_numbers = list(range(1, 11))
    random.shuffle(lottery_numbers)
    lottery_numbers = lottery_numbers[:5]
    print('The numbers in the lottery are:')
    num_matches = 0
    for i in range(5):
        print(lottery_numbers[i]);
        sleep(0.6)

    for j in numbers:
        if j in lottery_numbers:
            lottery_numbers.remove(j)
            num_matches += 1

    if num_matches == 1:
        print(f'You have {num_matches} match!')
    else:
        print(f'You have {num_matches} matches!')

    if num_matches >= 3:
        print(f"You head to the exit and escape this horrible smelling place.\n"
              f"never take life for granted and chase your dreams, {self.name}!!")
        exit()
    else:
        print('The place seems to be filling with a gass smell. You see a flash of light\n'
              'in the distance and before you can react you are engulfed in a fireball.')
        game_over()


def game_over():
    print('You lose, try again.')
    exit()
