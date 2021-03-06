from enum import Enum


# twitch settings
HOST = "irc.chat.twitch.tv"
PORT = 6667
NICK = "thehammieboyes"
PSWD = 'oauth:xyntph447nqmfluodyiqrxtl5dkdlu'

# grbl settings
GRBL_CONFIG = [
    "$21=0",  # hard limits
    "$24=6000",  # homing feed
    "$25=6000",  # homing seek
    "$100=3.14",  # x mm per step
    "$101=3.14",  # y mm per step
    "$110=6000",  # x max speed
    "$111=6000",  # y max speed
    "$120=100",  # x acceleration
    "$121=100",  # y acceleration
    "$130=10000",  # x size
    "$131=10000",  # y size
    "G91" # relative mode
]

# hardware settings
GRBL_PORT = "/dev/ttyACM0"
GRBL_BAUD = 115200

# command options
class Command(Enum):
    UP = "up"
    DOWN = "down"
    LEFT = "left"
    RIGHT = "right"
    RAISE = "raise"
    LOWER = "lower"
    RESET = "reset"

DEFAULT_MOVE = 100
MAX_MOVE = 300
