import re

text3 = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
 Sed 55 55 55 55 consequat nisl sed quam consequat, ac +37495656565 venenatis 95-12-12-21 justo vehicula.
   Nulla facilisi. Maecenas a nisi eget justo congue suscipit.
     Integer euismod 095121515 mauris id dui malesuada, nec lobortis risus consequat. 
       ABC    """


pattern = r'\+?\d+[\s,-]?\d+[\s,-]?\d+[\s, -]?\d+'

result = re.findall(pattern, text3)
print(result)
