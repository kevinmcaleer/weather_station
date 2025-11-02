# Reed Switch Counter for Raspberry Pi Pico
from machine import Pin
from time import sleep, ticks_ms, ticks_diff

reedswitch_pin = 0

# Configure reed switch with internal pull-up
switch = Pin(reedswitch_pin, Pin.IN, Pin.PULL_UP)

count = 0
previous_state = switch.value()  # Store the VALUE, not the Pin object
last_change_time = ticks_ms()
debounce_delay = 50  # 50ms debounce time

print("Reed Switch Counter")
print("Press Ctrl+C to exit\n")

try:
    while True:
        current_state = switch.value()
        current_time = ticks_ms()
        
        # Check if state changed AND enough time has passed (debouncing)
        if current_state != previous_state:
            if ticks_diff(current_time, last_change_time) > debounce_delay:
                # Count on the closing event (switch goes LOW with pull-up)
                if current_state == 0:
                    count += 1
                    print(f"Count: {count} | Switch CLOSED")
                else:
                    print(f"Count: {count} | Switch OPEN")
                
                previous_state = current_state
                last_change_time = current_time
        
        sleep(0.01)  # Check every 10ms
        
except KeyboardInterrupt:
    print(f"\nFinal count: {count}")
    print("Program stopped")