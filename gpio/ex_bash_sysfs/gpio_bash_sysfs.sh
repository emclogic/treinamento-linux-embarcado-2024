#!/bin/bash

GPIO_NUMBER=29

echo $GPIO_NUMBER >>  /sys/class/gpio/export
echo "out" >> /sys/class/gpio/gpio29/direction

echo 1 > /sys/class/gpio/gpio29/value
echo "LED $GPIO_NUMBER HIGH"
sleep 1

echo 0 > /sys/class/gpio/gpio29/value
echo "LED $GPIO_NUMBER LOW"
sleep 1

echo $GPIO_NUMBER >> /sys/class/gpio/unexport