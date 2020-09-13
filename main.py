from person import Person
from functions import *


def game_over():
    print('You lose, try again.')
    exit()


if __name__ == '__main__':
    player = Person(input("What is your name: "))

    instructions()
    read_formatted_file(player, 'begin')
    decision = input("Do you light the TORCH(T), STICK(S), or NOTHING(N): ")
    decision = decision.lower()

    while(True):
        if decision == 'torch' or decision == 't':
            read_formatted_file(player, 'torch')
            game_over()
        elif decision == 'stick' or decision == 's':
            read_formatted_file(player, 'stick')
            break
        elif decision == 'nothing' or decision == 'n':
            nothing(player)
            decision = input("Do you light the TORCH(T), STICK(S), or NOTHING(N): ")
            decision = decision.lower()
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            print('You must chose what do to!\n')
            decision = input("Do you light the TORCH(T), STICK(S), or NOTHING(N): ")
            decision = decision.lower()

    read_formatted_file(player, 'pit')
    decision = input('SWING(S) on the brittle rope, or risk the WALK(W) on the rotting planks: ')
    decision = decision.lower()
    while(True):
        if decision == 'swing' or decision == 's':
            read_formatted_file(player, 'swing')
            game_over()
        elif decision == 'walk' or decision == 'w':
            read_formatted_file(player, 'walk')
            break
        elif decision == 'quit':
            print('Good Bye')
            game_over()
        else:
            decision = input('You must chose SWING(S) or WALK(W): ')

    read_formatted_file(player, 'continuing')
    decision = input("CONTINUE(C) or QUIT(Q)")
    decision = decision.lower()

    while(True):
        if decision == 'give up' or decision == 'g':
            print("Way to give up... You just sit down to die.")
            game_over()
        elif decision == 'continue' or decision == 'c':
            read_formatted_file(player, 'continuing')
            break
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must pick something! CONTINUE(C) or GIVE UP(G): ')
            decision = decision.lower()

    read_formatted_file(player, 'cont')
    read_formatted_file(player, 'tee')
    decision = input("Choose wisely: ")
    decision = decision.lower()
    while(True):
        if decision == 'left' or decision == 'l':
            left(player)
            break
        elif decision == 'right' or decision == 'r':
            read_formatted_file(player, 'right')
            break
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must chose LEFT(L) or RIGHT(R): ')
            decision = decision.lower()

    decision = input("Do you keep going FORWARD(F) or TURN(T) back and go the other way: ")
    decision = decision.lower()
    while(True):
        if decision == 'forward' or decision == 'f':
            read_formatted_file(player, 'keep_going')
            break
        elif decision == 'turn' or decision == 't':
            left(player)
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must chose FORWARD(F) or TURN(T) back: ')
            decision = decision.lower()

    read_formatted_file(player, 'keep_going')
    decision = input("Do you start filling your pockets with TREASURE(T) or begin to\n"
                     "make your way up the CLIFF(C): ")
    decision = decision.lower()
    while(True):
        if decision == 'treasure' or decision == 't':
            read_formatted_file(player, 'greedy')
            game_over()
        elif decision == 'cliff' or decision == 'c':
            read_formatted_file(player, 'cliff')
            break
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must chose TREASURE(T) or CLIFF(C) back: ')
            decision = decision.lower()

    decision = input("Do you climb back DOWN(D) and get your matches or keep going UP(U): ")
    decision = decision.lower()
    while(True):
        if decision == 'down' or decision == 'd':
            read_formatted_file(player, 'down')
            break
        elif decision == 'up' or decision == 'u':
            player.set_matches_zero()
            read_formatted_file(player, 'up')
            break
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must chose DOWN(D) or UP(U): ')
            decision = decision.lower()


