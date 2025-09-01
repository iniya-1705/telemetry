import serial
import time

# Adjust the serial port for your SX1262 USB dongle
# On Raspberry Pi, it is usually /dev/ttyUSB0 or /dev/ttyAMA0
PORT = "/dev/ttyUSB0"   # change if needed
BAUD = 9600             # must match the receiver dongle baudrate

try:
    ser = serial.Serial(PORT, BAUD, timeout=1)
    print(f"Transmitting on {PORT} at {BAUD} baud...")

    counter = 0
    while True:
        
        message = f"Hello LoRa {counter}"
        ser.write((message + "\n").encode("utf-8"))   # send with newline
        print(f"[TX] {message}")
        counter += 1
        time.sleep(2)  # send every 2 seconds

except Exception as e:
    print("Error:", e)
