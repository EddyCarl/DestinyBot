#!/usr/bin/python

import json


def get_discord_secret(in_args):
    """
    Used to read the file passed into the program in order to obtain the discord secret API
    token that the bot will require in order to access the service.

    :param      in_args: Parsed arguments from cmd line - Should contain filepath the the
                         authentication.json file where the discord token is stored
    :return:    discord_secret
    """

    try:
        with open(in_args.auth, 'r') as file_in:
            json_data = json.load(file_in)
            return json_data['discord_secret']

    except FileNotFoundError:
        error_code = -1
        error_text = (
            '''
            -------------------------------
            The input file does not exist. 
                Terminating program.
            -------------------------------
            ''')

        print(error_text)
        exit(error_code)
