from machine import Pin
from time import sleep

reedswitch_pin = 0

switch = Pin(reedswitch_pin, Pin.IN)

count = 0

previous = switch

while True:
    print(f"switch is {switch.value()}")
    if switch.value() != previous:
        count += 1
        print(f"count: {count}")
        previous = switch.value()
    sleep(0.5)