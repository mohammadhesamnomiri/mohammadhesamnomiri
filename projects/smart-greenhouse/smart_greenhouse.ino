#include <DHT.h>

#define DHT_PIN 2
#define DHT_TYPE DHT11
#define SOIL_PIN A0
#define FAN_RELAY 8
#define PUMP_RELAY 9

const float MAX_TEMP = 30.0;
const int DRY_SOIL = 650;

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(FAN_RELAY, OUTPUT);
  pinMode(PUMP_RELAY, OUTPUT);
  digitalWrite(FAN_RELAY, LOW);
  digitalWrite(PUMP_RELAY, LOW);
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  int soil = analogRead(SOIL_PIN);

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("DHT11 read error");
    delay(2000);
    return;
  }

  bool hot = temperature >= MAX_TEMP;
  bool dry = soil >= DRY_SOIL;
  digitalWrite(FAN_RELAY, hot ? HIGH : LOW);
  digitalWrite(PUMP_RELAY, dry ? HIGH : LOW);

  Serial.print("Temp: "); Serial.print(temperature, 1);
  Serial.print(" C | Humidity: "); Serial.print(humidity, 1);
  Serial.print(" % | Soil: "); Serial.print(soil);
  Serial.print(" | Fan: "); Serial.print(hot ? "ON" : "OFF");
  Serial.print(" | Pump: "); Serial.println(dry ? "ON" : "OFF");

  delay(2000);
}
