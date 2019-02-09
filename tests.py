from config import Command, DEFAULT_MOVE
from skycrane.twitch.twitch import TwitchSocket
from skycrane.parser.parser import TwitchParser
from skycrane.controller.controller import TwitchController

from time import sleep

# testing twitch
ts = TwitchSocket()

# testing parser
tp = TwitchParser()

assert tp.parse_line("a:b:down") == (Command.DOWN, DEFAULT_MOVE)
assert tp.parse_line("a:b:down=50") == (Command.DOWN, 50)
assert tp.parse_line("a:b") == None
assert tp.parse_lines(["a:b"]) == None
assert tp.parse_lines(["a:b:down"]) == (Command.DOWN, DEFAULT_MOVE)

# testing controller
cl = TwitchController()

cl.do(Command.DOWN, DEFAULT_MOVE)
cl.do(Command.LEFT, DEFAULT_MOVE)
cl.do(Command.RIGHT, DEFAULT_MOVE)
cl.do(Command.UP, DEFAULT_MOVE)