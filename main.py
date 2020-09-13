from person import Person, Old_man
from functions import *

from time import sleep

if __name__ == '__main__':
    player = Person(input("What is your name: "))
    instructions()
    header(player)

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

    header(player)
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

    header(player)
    read_formatted_file(player, 'continuing')
    decision = input("CONTINUE(C) or GIVE UP(G): ")
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

    header(player)
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

    header(player)
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

    header(player)
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

    header(player)
    decision = input("Do you climb back DOWN(D) and get your matches or keep going UP(U): ")
    decision = decision.lower()
    while (True):
        if decision == 'down' or decision == 'd':
            header(player)
            read_formatted_file(player, 'down')
            read_formatted_file(player, 'up_again')
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

    header(player)
    read_formatted_file(player, 'reached_the_top')
    sleep(3)
    read_formatted_file(player, 'old_man')
    sleep(2)
    decision = input("Do you APPROACH(A) him or KICK(K) him off the ledge: ")
    decision = decision.lower()
    while (True):
        if decision == 'approach' or decision == 'a':
            read_formatted_file(player, 'down')
            break
        elif decision == 'kick' or decision == 'k':
            read_formatted_file(player, 'kick')
            sleep(5)
            read_formatted_file(player, 'old_man_float')
            game_over()
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must chose! APPROACH(A) him or KICK(K) him off the ledge: ')
            decision = decision.lower()

    header(player)
    read_formatted_file(player, 'approach')
    decision = input("Do you DELIVER(D) the message or help him or HELP(H) him get out of here: ")
    decision = decision.lower()
    while (True):
        if decision == 'deliver' or decision == 'd':
            read_formatted_file(player, 'deliver')
            break
        elif decision == 'help' or decision == 'h':
            read_formatted_file(player, 'help')
            sleep(5)
            old_man = Old_man('Old Man')
            print('The man in now part of your team!')
            player.set_friends()
            break
        elif decision == 'quit':
            print('Good Bye')
            exit()
        else:
            decision = input('You must chose to DELIVER(D) the message or help him or HELP(H) him get out of here: ')
            decision = decision.lower()

    try:
        header_with_buddy(player, old_man)
    except NameError:
        header(player)

    read_formatted_file(player, 'exit_cave')
    if player.friends > 0:
        decision = input("Do you ask the Old Man to launch a fireball? YES(Y) or NO(N): ")
        decision = decision.lower()
        while (True):
         if decision == 'yes' or decision == 'y':
             print("The Old Man launches a fireball at the rock and an opening appears.")
             old_man.use_fireball()
             break
         elif decision == 'no' or decision == 'n':
             print("For some odd reason you sit at the exit for the rest of your life. Well done..")
             game_over()
         elif decision == 'quit':
             print('Good Bye')
             exit()
         else:
             decision = input(
                 'Do you ask the Old Man to launch a fireball? YES(Y) or NO(N): ')
             decision = decision.lower()
    else:
        print("You have no way to move the rock. Maybe that Old Man could have helped?"
              "\n You parish from lack of water.")
        game_over()

    try:
        header_with_buddy(player, old_man)
    except NameError:
        header(player)
    read_formatted_file(player, 'freedom')