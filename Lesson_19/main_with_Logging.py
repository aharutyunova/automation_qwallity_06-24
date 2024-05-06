from login import login
from get_adv_course import get_advanced_courses
from write_json import write_json
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='my_log.log',
                    filemode='w+',
                    encoding='utf-8')


def Courses():
    try:
        if __name__ == "__main__":
            token = login()
            if token:
                logging.info("Login successful. Token: ", token)
                random_ten_courses = get_advanced_courses(token)
                if random_ten_courses:
                    write_json(random_ten_courses)
    except Exception as error:
        logging.error("Failed to retrieve advanced courses. Error: ", error)
    except Exception as e:
        logging.e("Login failed. Error: ", e)


Courses()