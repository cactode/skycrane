from config import Command, GRBL_CONFIG, GRBL_PORT, GRBL_BAUD
from serial import Serial
from time import sleep


class TwitchController():

    def __init__(self):
        self.grbl = Serial(GRBL_PORT, GRBL_BAUD, timeout=3)
        # need to let grbl initialize before configuring
        sleep(3)
        self.grbl.reset_input_buffer()
        for command in GRBL_CONFIG:
            self.send(command)

    def send(self, command):
        self.grbl.write((command + "\n").encode())
        # intentionally blocking to rate-limit
        response = self.grbl.readline().decode().strip()
        if response != "ok":
            raise IOError("Grbl error! Responded with: " +
                          (response or "nothing."))
        print("Sent command", command)

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
