# File: lora_tx.py
import time
from sx126x import SX126x

# Initialize SX1262 on Raspberry Pi (adjust GPIO pins if needed)
LoRa = SX126x(
    freq=868E6,              # Frequency (set same on Tx & Rx)
    bw=125E3,                # Bandwidth
    sf=7,                    # Spreading Factor (6–12)
    cr=5,                    # Coding Rate (4/5)
    syncWord=0x12,           # Sync word (must match Rx)
    txPower=22,              # Power in dBm
    preamble=8,              # Preamble length
    implicitHeader=False,    # Explicit header
    gpio=[7, 25, 8],         # [DIO1, BUSY, RESET] pins
    spi_bus=0,
    spi_cs=0
)

print("SX1262 LoRa HAT - Transmitter Started")

try:
    counter = 0
    while True:
        msg = f"Hello from Raspberry Pi! Packet #{counter}"
        LoRa.send(bytes(msg, "utf-8"))
        print(f"[TX] {msg}")
        counter += 1
        time.sleep(2)  # send every 2 sec
except KeyboardInterrupt:
    print("\n[TX] Transmission stopped.")
