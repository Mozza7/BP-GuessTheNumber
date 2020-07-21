import random
import sys


def menu():
    main = input('1: Start\n2: Help\n3: Exit\n')
    if int(main) == 1:
        def menu_2():
            difficulty = input('Set difficulty:\n1: 1-10\n2: 1-50\n3: 1-100\n4: 1-250\n5: 1-500\n6: Custom\n')
            num1 = 1
            if int(difficulty) == 1:
                num2 = 10
            elif int(difficulty) == 2:
                num2 = 50
            elif int(difficulty) == 3:
                num2 = 100
            elif int(difficulty) == 4:
                num2 = 250
            elif int(difficulty) == 5:
                num2 = 500
            elif int(difficulty) == 6:
                num1 = int(input('Enter minimum number: '))
                num2 = int(input('Enter maximum number: '))
            else:
                print('Please select an option (1-6).')
                menu_2()
            generate_number(num1, num2)
        menu_2()
    elif int(main) == 2:
        help_()
    elif int(main) == 3:
        sys.exit()
    else:
        print('Please select an option (1-3).')
        menu()


def generate_number(num1, num2):
    rand_num = random.randint(num1, num2)
    start_game(rand_num, num1, num2)


def help_():
    print('Help page')
    menu()


def start_game(rand_num, num1, num2):
    while True:
        guess_input = input('Enter your guess, or type exit to exit: ')
        if guess_input.isdigit():
            if int(guess_input) == rand_num:
                print(f'Congratulations! You were correct with your guess {rand_num}!\n')
                break
            elif int(guess_input) > num2:
                print(f'You guessed outside of the maximum limit of {num2}!')
            elif int(guess_input) < num1:
                print(f'You guessed below of the minimum limit of {num1}!')
            elif int(guess_input) < rand_num:
                print('You guessed too low!')
            elif int(guess_input) > rand_num:
                print('You guessed too high!')
            else:
                print('Whoops! we didn\'t understand that.. Please try again')
        else:
            if str(guess_input).casefold() == 'exit':
                print('Exiting..')
                sys.exit()
            else:
                print('Whoops! we didn\'t understand that.. Please try again')
    menu()


if __name__ == '__main__':
    menu()
