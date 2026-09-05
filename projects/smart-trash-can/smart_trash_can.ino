#include <Servo.h>

const byte IR_PIN = 2;
const byte SERVO_PIN = 9;
const int CLOSED_ANGLE = 10;
const int OPEN_ANGLE = 95;
const unsigned long OPEN_TIME = 1800;

Servo lid;

void setup() {
  pinMode(IR_PIN, INPUT);
  lid.attach(SERVO_PIN);
  lid.write(CLOSED_ANGLE);
}

void loop() {
  bool detected = digitalRead(IR_PIN) == LOW;
  if (detected) {
    lid.write(OPEN_ANGLE);
    delay(OPEN_TIME);
    lid.write(CLOSED_ANGLE);
    delay(400);
  }
  delay(50);
}
