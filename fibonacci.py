# n = int(input("Enter your input:... "))
# first = 0
# second = 1

# for i  in range(n):
#     print(first)
#     result = first
#     first = second
#     second = result + second



def fib(n):
    a = 0
    b = 1

    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c

        print(c)
        

fib(int(input("input here.... ")))