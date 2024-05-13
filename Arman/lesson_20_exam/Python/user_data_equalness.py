import logging

from register_user import registered_user_data

log_file_path = r'C:\Users\arman.petrosyan\Desktop\Qwallity\Arman\lesson_20_exam\out.log'

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file_path,
    filemode='w+'
)

user_data_file_path = r'C:\Users\arman.petrosyan\Desktop\Qwallity\Arman\lesson_20_exam\Python\data.json'

# Open data.json file where stored user data
with open(user_data_file_path, "r+") as file:
    user_data = file.read()


def check_data_equalness(first_input_dict, second_input_dict):
    # Check if the length of the stored data matches the number of keys in the registered data
    if len(first_input_dict) == 1 and all(
            first_input_dict[0][key] == second_input_dict[key] for key in second_input_dict
    ):
        print("Data is equal")
    else:
        logging.error("Data is not equal")


print(user_data, registered_user_data)
