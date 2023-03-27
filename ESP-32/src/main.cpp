#include <Arduino.h>

void setup() {
  // put your setup code here, to run once:
  Serial.begin(921600);
  Serial.println("Hello world");
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.println("Hello world");
  delay(100);
}