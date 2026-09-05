# Hardware test checklist

These checks are intended for a real Arduino + sensor bench test.

- [ ] DHT11 returns valid temperature and humidity values.
- [ ] Fan relay switches ON at or above 30°C.
- [ ] Fan relay switches OFF below 30°C.
- [ ] Soil value at or above 650 turns the pump relay ON.
- [ ] Soil value below 650 turns the pump relay OFF.
- [ ] A DHT11 read failure does not activate outputs unexpectedly.
- [ ] Serial output reports temperature, humidity, soil value, fan state and pump state.

## Boundary cases

| Input | Expected result |
|---|---|
| 29.9°C | Fan OFF |
| 30.0°C | Fan ON |
| Soil 649 | Pump OFF |
| Soil 650 | Pump ON |
| DHT read failure | Print error and return |
