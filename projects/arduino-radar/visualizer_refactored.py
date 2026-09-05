import math
import sys

import matplotlib.pyplot as plt
import serial

from radar_utils import parse_measurement

PORT = sys.argv[1] if len(sys.argv) > 1 else "COM3"
BAUD = 115200
MAX_DISTANCE = 250


def run():
    ser = serial.Serial(PORT, BAUD, timeout=0.2)
    plt.ion()
    fig = plt.figure(figsize=(9, 5))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_ylim(0, MAX_DISTANCE)
    ax.set_title("Arduino Radar")
    try:
        while plt.fignum_exists(fig.number):
            raw = ser.readline().decode(errors="ignore")
            measurement = parse_measurement(raw, MAX_DISTANCE)
            if measurement is None:
                continue
            angle, distance = measurement
            ax.clear()
            ax.set_ylim(0, MAX_DISTANCE)
            ax.set_title(f"Arduino Radar — {angle:.0f}° / {distance:.1f} cm")
            ax.scatter([math.radians(angle)], [distance], s=45)
            plt.pause(0.001)
    finally:
        ser.close()


if __name__ == "__main__":
    run()
