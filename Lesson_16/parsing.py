import re
import logging
import os

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', 
                    filename='my_log_lesson16.log', 
                    filemode='w+', 
                    encoding='utf-8')

def parsing(file):
      try:
            path = os.getcwd()
            full_path = os.path.join(path, 'Lesson_16')
            os.chdir(full_path)

            with open(file, 'r+') as f:
                  lines = f.readlines()
                  print(lines)
            dict = {}

            for l in lines:
                  position = re.search('#',l)
                  if position != None:
                        index = position.span()[0]
                        if index == 0:
                              pass
                        else:
                              l = l[0:index-1]
                              x = re.findall(r'(\w+)\s*=\s*(\d+)',l)
                              dict.update({x[0][0]: x[0][1]}) 
                    
                  else:
                        x = re.findall(r'(\w+)\s*=\s*(\d+)',l)
                        dict.update({x[0][0]: x[0][1]})
      except Exception as err:
            logging.error(err)
            
      return dict
      
print(parsing('config.ini'))

# Ann jan please also check 14 and 15, sorry for late homework((