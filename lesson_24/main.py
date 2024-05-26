import functions


functions.visibilty()
functions.progres_bar()
functions.input_text()

# Before putting it in the function it was working, now I get errors when
# running it.I don't know why

# Anna - you get error because you quit driver in each function, so after first function is executed connection is closed
# And other functions can't connect to the driver
# So if you close connection in each function, you should also open it


# Good solutions only for first task is_displayed is not correct checking
# As you remember i said that each button is hidden with specific condition, so displayed attribute not used for them
# And it is impossible to check for that elements solution with is_displayed argument
# You should find out how each element become hidden and check with that condition