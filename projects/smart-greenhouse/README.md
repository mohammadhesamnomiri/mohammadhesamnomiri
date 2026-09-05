# Smart Greenhouse 🌱

An Arduino automation project that monitors temperature/humidity and soil moisture, then controls a fan and water pump.

## Hardware
- Arduino Uno
- DHT11
- Soil-moisture sensor
- Relay module
- DC fan / pump
- Optional LCD

## Behavior
- Dry soil → pump turns on
- High temperature → fan turns on
- Serial Monitor shows live sensor values

## Wiring
| Component | Pin |
|---|---|
| DHT11 data | D2 |
| Soil sensor | A0 |
| Fan relay | D8 |
| Pump relay | D9 |

Install the `DHT sensor library` before uploading.
