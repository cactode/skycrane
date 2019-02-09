#!/usr/bin/python3
from skycrane.skycrane import SkyCrane
from time import sleep

POLLING_PERIOD = 3

crane = SkyCrane()
while True:
    crane.run()
    sleep(POLLING_PERIOD)

