

'''
Write a Python program that reads two integers representing a month and day and prints the season for that month and day.  
Expected Output:
Month: July(7)                   
Day: 31 
Season: Summer                                                    
'''


day_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 26, 27, 28,
             30, 31]
day_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
             16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 26, 27, 28]

month_1 = 1
month_2 = 2
month_3 = 3
month_4 = 4
month_5 = 5 
month_6 = 6
month_7 = 7
month_8 = 8
month_9 = 9
month_10 = 10
month_11 = 11
month_12 = 12

month_name_1 = "January(1)"
month_name_2 = 'February(2)'
month_name_3 = 'March(3)'
month_name_4 = 'April(4)'
month_name_5 = 'May(5)'
month_name_6 = 'June(6)'
month_name_7 = 'July(7)'
month_name_8 = 'August(8)'
month_name_9 = 'September(9)'
month_name_10 = 'October(10)'
month_name_11 = 'November(11)'
month_name_12 = 'December(12)'


season_1 = 'spring'
season_2 = 'summer'
season_3 = 'autumn'
season_4 = 'winter'



def myfunction(month, day):
    return month, day


month = int(input("please enter month with digit"))
day = int(input("Please enter the day"))

if day in day_list_2 and month == month_2:
        print(month_name_2, season_4)
elif day in day_list_1 and month == month_1:
        print(month_name_1, season_4) 
elif day == day_list_1 and month == month_12:
        print((month_name_12), end='\n'(season_4)) 
elif day == day_list_1 and month == month_3:
        print((month_name_3), end='\n'(season_1)) 
elif day == day_list_1 and month == month_4:
        print((month_name_4), end='\n'(season_1)) 
elif day == day_list_1 and month == month_5:
        print((month_name_5), end='\n'(season_1)) 
elif day == day_list_1 and month == month_6:
        print((month_name_6), end='\n'(season_2)) 
elif day == day_list_1 and month == month_7:
        print((month_name_7), end='\n'(season_2)) 
elif day == day_list_1 and month == month_8:
        print((month_name_8), end='\n'(season_2)) 
elif day == day_list_1 and month == month_9:
        print((month_name_9), end='\n'(season_3)) 
elif day == day_list_1 and month == month_10:
        print((month_name_10), end='\n'(season_3)) 
elif day == day_list_1 and month == month_11:
        print((month_name_11), end='\n'(season_3))    
        
else:
        print("No such a date")
      


# Some notes here
#  1. You should convert day and month inputed to int, as you compare with integer
#  2. In case you whant check day in the list, you should check day in list  not day==list, 
# because as day you get int and compare it with the list
#3. When print end='\n' is the last parameter of the print function, it is default '\n'.
        #  You can't take it between printed values - I changed for the first 2 prints
# After this changes program works

# Anyway, even code didn't work it is very good you tru build your own algorithm to solve this task
