# Hall Effect Sensor Reader for Raspberry Pi Pico
from machine import Pin, ADC
from time import sleep

# Configure ADC on GPIO26
hall_sensor = ADC(Pin(26))

# Optional: Configure internal pull-down (if your sensor needs it)
# Note: ADC pins don't have configurable pulls on RP2040, so this won't work:
# Pin(26, Pin.IN, Pin.PULL_DOWN)

def read_hall_sensor():
    """Read and return averaged ADC value to reduce noise"""
    samples = []
    for _ in range(10):
        samples.append(hall_sensor.read_u16())
        sleep(0.001)  # 1ms between samples
    return sum(samples) // len(samples)

def convert_to_voltage(adc_value):
    """Convert 16-bit ADC value to voltage (0-3.3V)"""
    return (adc_value / 65535) * 3.3

print("Hall Effect Sensor Reader")
print("Press Ctrl+C to exit\n")

try:
    while True:
        # Read averaged value
        raw_value = read_hall_sensor()
        voltage = convert_to_voltage(raw_value)
        
        print(f"Raw: {raw_value:5d} | Voltage: {voltage:.3f}V")
        sleep(0.5)
        
except KeyboardInterrupt:
    print("\nProgram stopped")