#!/usr/bin/python

from argparse import ArgumentParser
from destiny_bot import DestinyBot


def parse_arguments():
    """
    Creates an ArgumentParser instance that is used to parse command line arguments when the
    application is run.

    These command line arguments should consist of the following:

    -a | --auth : The \"authentication.json\" file that is required containing API tokens
    -h | --help : Display this help text

    :return: args
    """

    description_text = 'A Discord bot that is used to server Destiny API requests.'
    help_text = 'The \"authorisation.json\" file containing API tokens.'

    argument_parser = ArgumentParser(description=description_text)
    argument_parser.add_argument('-a', '--auth', help=help_text, required=True)
    args = argument_parser.parse_args()

    return args


if __name__ == '__main__':
    """
    The main method of the bot program. Called when run directly via the command line 
    as opposed to being imported as a module. 
    
    Parses the command line arguments(which is expected to contain the \"authorisation.json\"
    file containing the API tokens. Then creates the DestinyBot instance and passes in the
    arguments. The file is read within the bot in order to obtain the token.
    """

    parsed_args = parse_arguments()

    while True:

        try:
            discord_bot = DestinyBot(parsed_args)
            discord_bot.start()

        except ConnectionResetError:
            print('The connection was reset...')
