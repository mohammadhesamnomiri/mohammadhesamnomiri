# Hardware test checklist

- [ ] HC-SR04 returns stable distance readings.
- [ ] Servo sweeps through the configured angle range.
- [ ] Serial output follows `angle,distance` format.
- [ ] Invalid serial lines are ignored by the Python parser.
- [ ] Distances above the configured maximum are ignored.
- [ ] The Python visualizer closes the serial port cleanly when the window exits.

## Manual calibration

Place a flat target at known distances (for example 20 cm, 50 cm and 100 cm) and compare the serial reading with the reference distance. Record the measured values in the README or an experiment log rather than claiming a fixed accuracy without measurements.
