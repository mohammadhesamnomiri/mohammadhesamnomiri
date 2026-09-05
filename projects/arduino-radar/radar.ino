#include <Servo.h>

const byte TRIG = 10;
const byte ECHO = 11;
const byte SERVO_PIN = 9;
Servo scanner;

float readDistanceCm() {
  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  unsigned long duration = pulseIn(ECHO, HIGH, 30000UL);
  if (duration == 0) return -1;
  return duration * 0.0343f / 2.0f;
}

void sendMeasurement(int angle) {
  scanner.write(angle);
  delay(35);
  float distance = readDistanceCm();
  Serial.print(angle);
  Serial.print(',');
  Serial.println(distance, 1);
}

void setup() {
  Serial.begin(115200);
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  scanner.attach(SERVO_PIN);
}

void loop() {
  for (int angle = 15; angle <= 165; angle += 2) sendMeasurement(angle);
  for (int angle = 165; angle >= 15; angle -= 2) sendMeasurement(angle);
}
