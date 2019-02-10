from config import Command, GRBL_CONFIG, GRBL_PORT, GRBL_BAUD
from serial import Serial
import pigpio
from threading import Timer
from time import sleep


class TwitchController():

    def __init__(self):
        self.grbl = Serial(GRBL_PORT, GRBL_BAUD, timeout=3)
        # need to let grbl initialize before configuring
        sleep(3)
        self.grbl.reset_input_buffer()
        for command in GRBL_CONFIG:
            self.send(command)

        pi = pigpio.pi()
        pi.set_mode(3, pigpio.OUTPUT)
        pi.stop()

    def send(self, command):
        self.grbl.write((command + "\n").encode())
        # intentionally blocking to rate-limit
        response = self.grbl.readline().decode().strip()
        if response != "ok":
            raise IOError("Grbl error! Responded with: " +
                          (response or "nothing."))
        print("Sent command", command)

    # value should be between -300 and 300
    def pulse_motor(self, value):
        pulse_length = abs(value)/100
        pi = pigpio.pi()
        pi.set_servo_pulsewidth(3, 500 if value < 0 else 1500)
        Timer(pulse_length, self.turn_off_motor,
              kwargs={'pi': pi}).start()

    def turn_off_motor(self, pi):
        pi.set_servo_pulsewidth(3, 1500)
        pi.stop()

    def do(self, command, value):
        if command == Command.LEFT:
            self.send("G0 X" + str(value))
        elif command == Command.RIGHT:
            self.send("G0 X" + str(-value))
        elif command == Command.UP:
            self.send("G0 Y" + str(value))
        elif command == Command.DOWN:
            self.send("G0 Y" + str(-value))
        elif command == Command.RAISE:
            self.pulse_motor(value)
        elif command == Command.LOWER:
            self.pulse_motor(-value)
        else:
            raise ValueError("Unrecognized command")
