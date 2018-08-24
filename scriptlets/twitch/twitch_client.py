import sys
import irc.bot
import requests
import logging

class TwitchClient(irc.bot.SingleServerIRCBot):
    def __init__(self, machine, username, password, channel):
        self.log = logging.getLogger('TwitchClient') 
        self.machine = machine
        self.password = password
        self.channel = '#' + channel

        # Create IRC bot connection
        server = 'irc.chat.twitch.tv'
        port = 6667
        self.log.info('Connecting to ' + server + ' on port ' + str(port) + '...')
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port, 'oauth:' + password)], username, username)
        # self.connection.add_global_handler("all_events", self.on_all_events, -100)

    def on_welcome(self, c, e):
        self.log.info('Joining ' + self.channel)

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
            user = e.source.split('!')[0]
            message = 'Chat: [' + user + '] ' + e.arguments[0] + ' : ' + str(e)
            self.log.info(message.replace(self.password, 'XXXXX'))
            tags = self.build_tag_dict(e.tags)
            bits = tags.get('bits')
            message_type = tags.get('msg-id')
            if message_type == 'sub' or message_type == 'resub':
                months = tags.get('msg-param-months', 1)
                subscriber_message = tags.get('message', '')
                self.machine.events.post('twitch_subscription', user=user, message=e.arguments[0], months=int(months), subscriber_message=subscriber_message)
            elif bits is not None:
                self.machine.set_machine_var('twitch_last_bits_user', user)
                self.machine.set_machine_var('twitch_last_bits_amount', bits)
                self.machine.events.post('twitch_bit_donation', user=user, message=e.arguments[0], bits=int(bits))
            else:
                self.machine.set_machine_var('twitch_last_chat_user', user)
                self.machine.set_machine_var('twitch_last_chat_message', e.arguments[0])
                self.machine.events.post('twitch_new_chat_message', user=user, message=e.arguments[0])

    def on_privmsg(self, c, e):
        user = e.source.split('!')[0]
        self.log.info('Private chat: [' + user + '] ' + e.arguments[0])

    def on_all_events(self, c, e):
        message = 'All Events: ' + e
        self.log.info(message.replace(self.password, 'XXXXX'))

    def do_command(self, e, cmd):
        user = e.source.split('!')[0]
        self.log.info('Received command: [' + user + '] ' + cmd)

    def is_connected(self):
        return self.connection.is_connected()

    def build_tag_dict(self, seq):
        return dict((d['key'], d['value']) for (index, d) in enumerate(seq))
