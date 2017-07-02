#!/usr/bin/python

import discord
import utilities


class DestinyBot:
    """
    Main DestinyBot logic.

    This handles authentication of the Discord bot service and method handlers on the API in
    order to handle various commands that may be input by a user.
    """

    def __init__(self, arguments):

        self.discord_secret = utilities.get_discord_secret(arguments)
        self.client = discord.Client()

        @self.client.event
        async def on_ready():
            """
            Called when the bot has completed its login procedure.
            Outputs a message to state that it has logged in succesfully.

            :return:    None
            """

            print('Successfully logged in as:')
            print('{} (ID: {})'.format(self.client.user.name, self.client.user.id))

        @self.client.event
        async def on_message(message):
            if message.content.startswith('!hello'):
                await self.client.send_message(message.channel, 'Hello World')

    def start(self):
        """
        Starts the Discord Client instance running.
        Once the bot is up and running, further commands can be serviced by the bot instance.
        Note. This MUST be the final method called due to its blocking nature.

        :return:    None
        """

        self.client.run(self.discord_secret)
