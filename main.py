#!/usr/bin/env python3
# -*-coding:utf-8 -*


from time import sleep

from irsensors import IRSensorSet


if __name__ == "__main__":
    sensor = IRSensorSet()
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
