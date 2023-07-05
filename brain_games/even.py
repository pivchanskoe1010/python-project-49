#!/usr/bin/python3

import prompt
from random import randint


random_number = randint(1, 1000)
even_check = random_number % 2


def greet():
    print('Welcome to the Brain Games!')


def even_or_not():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: ' + str(random_number))
    user_answer = prompt.string('Your answer: ')
    if even_check == 0 and user_answer == 'yes':
        print('Correct!')
    elif even_check == 0 and user_answer != 'yes':
        print(f"""'{user_answer}' is wrong answer ;(. Correct answer was 'yes'.
Let's try again, {name}""")
    elif even_check == 1 and user_answer == 'no':
        print('Correct!')
    elif even_check == 1 and user_answer != 'no':
        print(f"""'{user_answer}' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}""")

