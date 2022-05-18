import hid
from time import time
from datetime import datetime

VENDOR_ID = 0x04d9
PRODUCT_ID = 0xa052

CODE_TAMB = 0x42  # Ambient Temperature
CODE_CNTR = 0x50  # Relative Concentration of CO2

EXPECTED_POINT = 0x0d  # Unexpected data from device
BYTES_READ = 8


def celsium(kelvin):
    return kelvin * 0.0625 - 273.15


def get_data(debug: bool = False):
    co2 = hid.device()
    co2.open(VENDOR_ID, PRODUCT_ID)
    try:
        result = {}

        while len(result) < 2:
            data = co2.read(BYTES_READ, 1000)

            if debug:
                print(data, len(data))

            if len(data) == 0:
                # hack for initialize device
                co2.send_feature_report(co2.get_feature_report(0,4))
                continue

            code = data[0]
            value = (data[1] << 8) + data[2]
            check_sum = sum(data[:3]) % 256
            check_value = data[3]
            point = data[4]

            if code not in (CODE_TAMB, CODE_CNTR):
                pass

            if check_sum != check_value:
                if debug:
                    print(f"Checksum error: {data} | {check_sum=} | {check_value=}")
                continue

            if point != EXPECTED_POINT:
                if debug:
                    print(f"Unexpected data from device: {data}")
                continue

            if code == CODE_TAMB:
                result["temp"] = round(celsium(value), 1)

            if code == CODE_CNTR:
                result["co2"] = value

    except Exception as e:
        raise e
    finally:
        co2.close()

    result['time'] = datetime.fromtimestamp(time())
    return result
