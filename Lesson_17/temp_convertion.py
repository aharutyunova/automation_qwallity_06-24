import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='temp_kelv_cels_log.log',
                    filemode='w+',
                    encoding='utf-8')


class Temp_Convertor:
    def kelvin_to_celsius(kelvin_temp):
        try:
            celsius_temp = round(kelvin_temp - 273.15)
            logging.error("Temperature is successfully converted from Kelvin to Celsius")
            return celsius_temp
        except Exception as e:
            logging.error(f"Error occurred while converting temperature: {e}")
            return None
