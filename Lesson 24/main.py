"""
Navigate to "http://www.uitestingplayground.com/"
1. Go to Visibility, click the Hide button. Check in your program that buttons are hidden.
2. Go to Progress Bar, click the Start button, then stop it.  Print Duration.
3. Go to Text Input, enter any text, click the button and check if the button text is the same as the entered text.
"""

import method_1, method_3, method_2

def run_methods():
    method_1.method_one()
    method_2.method_two()
    method_3.method_three()

if __name__ == "__main__":
    run_methods()


# First task very good organized, you get the root. Overlapped button is visible in your solution, 
# because you should check style not for button itself, but for ovelap element
# When you click hide, in element which overlap our button added style(id=hidingLayer), 
# and you should check style of that element

# Task 2 and Task 3 are correct
# Good job :) I liked solution especially for first task