'''
Copyright 2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"). You may not use this file except in compliance with the License. A copy of the License is located at

    http://aws.amazon.com/apache2.0/

or in the "license" file accompanying this file. This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
'''

import sys
import irc.bot
import requests

class TwitchClient(irc.bot.SingleServerIRCBot):
    def __init__(self, machine, username, password, channel):
        self.log = machine.logging.getLogger('TwitchClient') 
        self.machine = machine
        self.password = password
        self.channel = '#' + channel

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        self.log.log_info('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + password)], username, username)

    def on_welcome(self, c, e):
        self.log.log_info('Joining ' + self.channel)

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # If a chat message starts with ! or ?, try to run it as a command
        if e.arguments[0][:1] == '!' or e.arguments[0][:1] == '?':
            cmd = e.arguments[0].split(' ')[0][1:]
            self.do_command(e, cmd)
        else:
            self.log.log_info('Chat: [' + e.source + '] ' + e.arguments[0])

    def on_privmsg(self, c, e):
        self.log.log_info('Private Chat: [' + e.source + '] ' + e.arguments[0])

    def do_command(self, e, cmd):
        self.log.log_info('Received command: [' + e.source + '] ' + cmd)
