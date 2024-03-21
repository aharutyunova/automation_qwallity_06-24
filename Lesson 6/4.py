'''
4.	Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''

month_dict = [  {'name':'december', 'monthnumber': 12, 'days': 31, 'season': 'winter'},
                {'name':'january','monthnumber': 1, 'days': 31, 'season': 'winter'},
                {'name':'february','monthnumber': 2, 'days': 28, 'season': 'winter'},
                {'name':'march','monthnumber': 3, 'days': 31, 'season': 'spring'},
                {'name':'april','monthnumber': 4, 'days': 30, 'season': 'spring'},
                {'name':'may','monthnumber': 5, 'days': 31, 'season': 'spring'},
                {'name':'june','monthnumber': 6, 'days': 30, 'season': 'summer'},
                {'name':'july','monthnumber': 7, 'days': 31, 'season': 'summer'},
                {'name':'august','monthnumber': 8, 'days': 31, 'season': 'summer'},
                {'name':'september','monthnumber': 9, 'days': 30, 'season': 'autumn'},
                {'name':'october','monthnumber': 10, 'days': 31, 'season': 'autumn'},
                {'name':'november', 'monthnumber': 11,'days': 30, 'season': 'autumn'}] 
print('\n','month: ', end = '')
month = int(input())
print(' day: ', end = '')
day = int(input())

if month not in range(1,13) or day not in range(1, 32):
    print('month or day number is not correct')

for month_i in month_dict:
    if month != month_i['monthnumber']:
        continue
    elif day in range(1,month_i['days']):
        print('season is:',month_i['season'])
    else:
        name = month_i['name'] 
        days = month_i['days'] 
        print(f'month {name} has {days} days')

# Anna - everything is almost correct, only month name is not printed. But general solutions is good enough