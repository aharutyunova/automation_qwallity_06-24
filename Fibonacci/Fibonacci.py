def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        print("Incorrect input!")
    
    else:
        for i in range(n):
                
            if i == 0:
                print(0)
            else:
                c = a + b
                a = b
                b = c

            print(b)
    
(fibonacci(9))

# I didn't expect you write the code for this task, but it's good you try
# I edited a bit the code, but currenlty don't want we focus on it
#  Will discuss the code after a couple of lessons