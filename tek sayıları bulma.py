number = int(input("Enter a number: "))

i = 0

for i in range(1, number):
    if(i % 2 == 1):
        print(i, end=' ')

