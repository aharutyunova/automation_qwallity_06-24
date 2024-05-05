login_url = 'https://qwallity-prod.onrender.com/login/api'
add_course_url = 'https://qwallity-prod.onrender.com/add_course/api'
get_fundamental_courses_url = 'https://qwallity-prod.onrender.com/courses/fundamental/api'
update_course_url = 'https://qwallity-prod.onrender.com/course/{}/update/'
delete_course_url = 'https://qwallity-prod.onrender.com/courses/course/{}'

add_course_body = {
  "title": "course_RPA",
  "body": "body_RPA",
  "coursetype": "1",
  "author": "RPA",
  "price": 500
}
update_add_course_body = {
  "title": "course_RPA_updated",
  "body": "body_RPAupdated",
  "coursetype": "1",
  "author": "RPA",
  "price": 1000
}