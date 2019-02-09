from skycrane.twitch.twitch import TwitchSocket
from skycrane.parser.parser import TwitchParser
from skycrane.controller.controller import TwitchController


class SkyCrane():
    def __init__(self):
        self.t = TwitchSocket()
        self.p = TwitchParser()
        self.c = TwitchController()

    def run(self):
        lines = self.t.recv_lines()
        if not lines:
            return
        command = self.p.parse_lines(lines)
        if not command:
            return
        self.c.do(*command)
