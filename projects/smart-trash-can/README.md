# Smart Trash Can 🗑️

An automatic Arduino trash can that detects a nearby hand/object with an IR sensor and opens the lid using a servo motor.

## Hardware
- Arduino Uno/Nano
- IR obstacle/proximity sensor
- Servo motor (SG90/MG90S)

## Wiring
| Component | Arduino |
|---|---|
| IR OUT | D2 |
| Servo signal | D9 |
| VCC | 5V |
| GND | GND |

The lid opens when the sensor detects an object, waits briefly, then closes automatically.
