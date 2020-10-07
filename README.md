# PyMLX90614
Python library for MLX90614 infrared temperature sensors, using [smbus2](https://pypi.org/project/smbus2/). Compatible with Python 2 and 3.

You might need to enter this command on your Raspberry Pi:

`sudo su -c 'echo "Y" > /sys/module/i2c_bcm2708/parameters/combined'`

Consider putting it in `/etc/rc.local` so it's executed each bootup

## Usage

First, ensure the device is available on the i2c bus:

```
$ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- 5a -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```

Within Python, the device can be used like this:

```python
from smbus2 import SMBus
from mlx90614 import MLX90614

bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
print sensor.get_amb_temp()
print sensor.get_obj_temp()
bus.close()
```

## License

This project is licensed under the terms of the MIT license.