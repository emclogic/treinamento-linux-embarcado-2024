#!/bin/bash

GPIO_BASE=512
GPIO_NUMBER=29
GPIO_PIN=$( expr $GPIO_BASE + $GPIO_NUMBER)

echo $GPIO_PIN >>  /sys/class/gpio/export
echo "out" >> /sys/class/gpio/gpio$GPIO_PIN/direction

echo 1 > /sys/class/gpio/gpio$GPIO_PIN/value
echo "LED $GPIO_NUMBER HIGH"
sleep 1

echo 0 > /sys/class/gpio/gpio$GPIO_PIN/value
echo "LED $GPIO_NUMBER LOW"
sleep 1

echo $GPIO_PIN >> /sys/class/gpio/unexport