from config import Command, GRBL_CONFIG, GRBL_PORT, GRBL_BAUD
from serial import Serial


class TwitchController():
    def __init__(self):
        self.grbl = Serial(GRBL_PORT, GRBL_BAUD, timeout=3)
        for command in GRBL_CONFIG:
            self.send(command)

    def send(self, command):
        self.grbl.write((command + "\r\n").encode())
        # intentionally blocking to rate-limit
        if self.grbl.readline() != "ok":
            raise IOError("Grbl reported error!")

    def do(self, command, value):
        if command == Command.LEFT:
            self.send("G0 X" + str(value))
        elif command == Command.RIGHT:
            self.send("G0 X" + str(-value))
        elif command == Command.UP:
            self.send("G0 Y" + str(value))
        elif command == Command.DOWN:
            self.send("G0 Y" + str(-value))
        else:
            raise ValueError("Unrecognized command")

    def __del__(self):
        if self.grbl.is_open:
            self.grbl.close()
