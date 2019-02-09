from config import Command, DEFAULT_MOVE
from skycrane.parser.parser import TwitchParser

# testing parser
tp = TwitchParser()

assert tp.parseLine("a:b:down") == (Command.DOWN, DEFAULT_MOVE)
assert tp.parseLine("a:b:down=50") == (Command.DOWN, 50)
assert tp.parseLine("a:b") == None
assert tp.parseLines(["a:b"]) == None
assert tp.parseLines(["a:b:down"]) == (Command.DOWN, DEFAULT_MOVE)