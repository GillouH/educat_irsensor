#!/usr/bin/env python3
# -*-coding:utf-8 -*


from time import sleep

from irsensors import IRSensorSet


#ID_LIST = [3, 1, 2, 0]
ID_LIST = [3]


if __name__ == "__main__":
    sensor = IRSensorSet(id_sensors=ID_LIST)
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
