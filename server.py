# -*-encoding:Utf-8-*-

import socket
import time

class Server():
    """This class represent the connexion to an IRC server.
    It manages the nick, status, and other informations.
    This class contains also the functions and events that
    are related to the whole server.
    """

    def __init__(self, server, port=6667, autoconnect=True, nick="Anonymous"):
        self.socket = socket.socket()
        self.socket.connect((server, port))
        self.sockfl = self.socket.makefile()
        for line in self.sockfl :
            print(line.strip())


    def nick(nick):
        pass

    def join(channel, password=""):
        pass
