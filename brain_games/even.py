#!/usr/bin/python3

import prompt
from random import randint

def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def even_check():
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    print('Question: ' + str(randint(1, 1000)))
    number = prompt.string('Your answer: ')

