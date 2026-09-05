# Arduino Radar 📡

A simple ultrasonic radar that measures distance and streams angle/distance pairs to a computer over Serial.

## Hardware
- Arduino Uno
- HC-SR04 ultrasonic sensor
- SG90/MG90S-compatible servo

## Wiring
| HC-SR04 | Arduino |
|---|---|
| VCC | 5V |
| GND | GND |
| TRIG | D10 |
| ECHO | D11 |

Servo signal → D9.

## Protocol
The Arduino prints one measurement per line as:
`angle,distance_cm`

This format makes it easy to build a Python/Processing visualizer later.
