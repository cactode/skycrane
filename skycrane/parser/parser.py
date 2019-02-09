from config import Command, DEFAULT_MOVE, MAX_MOVE
from random import choice


class TwitchParser():
    def __init__(self):
        pass

    def parse_line(self, line):
        chunks = line.split(":")
        if len(chunks) != 3:
            return None
        command_value = chunks[2].lower().split("=")
        if len(command_value) not in [1, 2]:
            return None
        command = command_value[0]
        if command not in (c.value for c in Command):
            return None
        value = DEFAULT_MOVE
        if len(command_value) == 2:
            try:
                number = abs(int(command_value[1]))
                value = max(number, MAX_MOVE)
            except Exception as e:
                pass

        return (Command(command), value)

    def parse_lines(self, lines):
        commands = [l for l in (self.parse_line(line) for line in lines) if l]
        if commands:
            return choice(commands)
        else:
            return None
