# In one python file wtite functions which will get any 10 of advanced courses id and title
# Add schema validation for check returned data
# Open file and add json data there if validation pass
# Create second .py file and organize code run there
# create bat file to call second .py
#  create task scheduler (if have time)

from get_advanced_courses import courses_list

from write_json import write_json


if __name__ == "__main__":
    advanced_courses_data = courses_list

    write_json(courses_list)


# Anna - everything works, bat file also.
# As you write some parts of code in functionas and some part directly in teh module, it was a bit confusing, but generally everything is correct
# Also Json file path was hardcoded
# Good Job