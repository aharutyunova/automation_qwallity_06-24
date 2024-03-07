def Fibonacci(n):
    first_member = 0
    second_member = 1
    if n <= 0:
        print("Invalid n value")
    else:
        print("The Fibonacci sequence is:", first_member, end=" ")
        for i in range(1, n):
            print(second_member, end=" ")
            next_member = first_member + second_member
            first_member = second_member
            second_member = next_member


Fibonacci(int(input("Enter n value: ")))

