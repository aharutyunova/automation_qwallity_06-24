
# General overview

This Python program do following flow:  1.Login to the system with admin_user account
                                        2.Add Fundamental Course                                       
                                        3.Get Fundamental Course and check your course is added
                                        4.Update Course by course_id
                                        5.Delete Course


Program Structure

- main.py - this file is for running logical flow described above
- login.py - this file contains login function which is for logging with given credentials and returns token for further requests
- add_course.py - this file contains add_course function which is for adding new fundamental course and redturns added course_id
- get_fundamental_courses.py - this file contains 2 functions: get_fundamental_courses function for getting all existing fundamental course ids
                                                    and check_course_existence function for checking added course existence in all fundamental courses
- update_course.py  -this file is contains update_course function which get course_id, update body for updateing it                                                   
- delete_course.py -this file contains delete_course function which get course_id for deleting it
- config.py - this file contain main credentials for authorization
- endpoints.py - this file contains all endpoints for executing requests and some bodys for creating and updateing courses

# Prerequisites

Before running the program, ensure that you have the following:
Used library:                       - os
                                    - requests

# Usage

To start the program run main.py
