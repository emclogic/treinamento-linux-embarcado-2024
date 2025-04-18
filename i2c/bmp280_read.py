#!/bin/env python3

import board
import busio
import adafruit_bmp280

# Inicializa bus
i2c = busio.I2C(board.SCL, board.SDA)

# Inicializa o sensor BMP280 no endereço I2C 0x76
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Configuração opcional: ajuste a pressão do nível do mar para sua localização (em hPa)
bmp280.sea_level_pressure = 1013.25  # Padrão para o nível do mar

print(f"Temperatura: {bmp280.temperature:.2f} °C")
print(f"Pressão: {bmp280.pressure:.2f} hPa")
print(f"Altitude: {bmp280.altitude:.2f} metros")
