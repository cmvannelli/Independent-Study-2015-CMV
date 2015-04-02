#ifndef Sensor_h
#define Sensor_h

#include "Arduino.h"

class Sensor {
	public:
		Sensor(int pin);
		void TurnOn();
		void ReadIn();

	private:
		int _pin;
		int _pressure;
};

#endif