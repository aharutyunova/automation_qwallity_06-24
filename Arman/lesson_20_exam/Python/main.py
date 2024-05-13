from register_user import user_registration, registered_user_data
from user_data_equalness import check_data_equalness
from validate_user_data import validation_schema

user_data_file_path = r'C:\Users\arman.petrosyan\Desktop\Qwallity\Arman\lesson_20_exam\Python\data.json'

# Read the text from text.txt file
with open("text.txt", "r") as file:
    text = file.read()

# Open data.json file where stored user data
with open(user_data_file_path, "r+") as file:
    user_data = file.read()


def main():
    user_registration(user_data)
    validation_schema.load(registered_user_data['0'])
    check_data_equalness(user_data, registered_user_data)


if __name__ == "__main__":
    main()
