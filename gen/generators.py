def Count_to(n):
    count  = 1
    while count <= n:
        yield count
        count  += 1



number = int(input("enter a number  : "))



for n in Count_to(number):
    print(n)