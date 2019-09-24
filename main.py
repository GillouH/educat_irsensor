#!/usr/bin/env python3
# -*-coding:utf-8 -*


from time import sleep

from irsensors import IRSensorSet


if __name__ == "__main__":
    sensor = IRSensorSet("COM22", [3, 1, 2, 0])
    try:
        sensor.start()

        while True:
            print(sensor)
            sleep(0.1)

    except KeyboardInterrupt:
        pass

    finally:
        sensor.stop()
        del sensor
