# desciption

mini library for MT8057s

# dependens
 - https://github.com/trezor/cython-hidapi

# install
```
sudo apt-get install python-dev libusb-1.0-0-dev libudev-dev
sudo pip install --upgrade setuptools
sudo pip install hidapi
```

# Push metric in database

```
$ cp config.py.example config.py

$ sudo python3.8 monitoring_co2.py
```

# using

```
>>> get_data()
{'temp': 25.4, 'co2': 574, 'time': datetime.datetime(2022, 4, 29, 20, 32, 35, 190915)}
```

with debug:
```
>>> get_data(True)
[66, 18, 169, 253, 13, 0, 0, 0] 8
[109, 13, 10, 132, 13, 0, 0, 0] 8
[110, 73, 25, 208, 13, 0, 0, 0] 8
[113, 2, 54, 169, 13, 0, 0, 0] 8
[80, 2, 62, 144, 13, 0, 0, 0] 8
{'temp': 25.4, 'co2': 574, 'time': datetime.datetime(2022, 4, 29, 20, 32, 35, 190915)}
```

# note
pooling time = 10s

# some analog
 - https://github.com/dmage/co2mon