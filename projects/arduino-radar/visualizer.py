import math
import sys
import serial
import matplotlib.pyplot as plt

PORT = sys.argv[1] if len(sys.argv) > 1 else "COM3"
BAUD = 115200
MAX_DISTANCE = 250

ser = serial.Serial(PORT, BAUD, timeout=0.2)
plt.ion()
fig = plt.figure(figsize=(9, 5))
ax = fig.add_subplot(111, projection="polar")
ax.set_ylim(0, MAX_DISTANCE)
ax.set_title("Arduino Radar")

try:
    while plt.fignum_exists(fig.number):
        raw = ser.readline().decode(errors="ignore").strip()
        if not raw or "," not in raw:
            continue
        try:
            angle, distance = map(float, raw.split(",", 1))
        except ValueError:
            continue
        if distance < 0 or distance > MAX_DISTANCE:
            continue
        ax.clear()
        ax.set_ylim(0, MAX_DISTANCE)
        ax.set_title(f"Arduino Radar — {angle:.0f}° / {distance:.1f} cm")
        ax.scatter([math.radians(angle)], [distance], s=45)
        plt.pause(0.001)
finally:
    ser.close()
