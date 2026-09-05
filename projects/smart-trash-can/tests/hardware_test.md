# Hardware test checklist

- [ ] With no object in front of the IR sensor, the lid stays closed.
- [ ] A detected object moves the servo to 95°.
- [ ] The lid remains open for approximately 1.8 seconds.
- [ ] The servo returns to 10° after the open interval.
- [ ] The mechanism waits approximately 0.4 seconds before accepting the next cycle.
- [ ] Servo power is stable under load and shares a common ground with the Arduino.

## Boundary / reliability checks

1. Trigger the sensor repeatedly and confirm the servo returns to the closed position.
2. Test different object distances and lighting conditions because IR sensors can be sensitive to ambient light.
3. Confirm the lid moves freely before increasing servo load.
