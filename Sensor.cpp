/*

Read in pressure values and do boxcar averager 

*/

#include "Arduino.h"
#include "Sensor.h"

Sensor::Sensor(int pin) {
	pinMode(pin, INPUT);
	_pin = pin;
	unsigned long startTime;
	unsigned long testTime = 0;
	int maxVal = 0;
	int maxPress = 0;
}

void Pump::TurnOn() {
	startTime = millis() // time that testing starts
}

void Pump::ReadIn() {
	while (testTime < (7500 + startTime))
		testTime = millis();
		tempVal = analogRead(pin)
		tempVolt = (((float)tempVal)*(5.0/1023)-0.13); // P --> V conversion
		maxVal = max(maxVal,tempVolt)
}

void Pump::V_to_P() {
	maxPress = (maxVal*24.7078)
}