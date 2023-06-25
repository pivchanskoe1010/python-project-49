#!/usr/bin/env python3


from brain_games.even import even_check
from brain_games.even import welcome_user


def greet():
    print('Welcome to the Brain Games!')


def main():
    greet()
    welcome_user()
    even_check()


if __name__ == '__main__':
    main()
