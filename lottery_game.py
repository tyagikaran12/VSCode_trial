import random
lucky_number = random.randint(1,30)
print("lucky number = {}".format(lucky_number))
result = {}
a = input("ENTER YOUR NAME HERE: ")
randomlist = []
n = int(input("ENTER NUMBER OF TRIES: "))
price_ticket = 10*n
for i in range(0,n):
    n = random.randint(1,30)
    randomlist.append(n)
print("{}'S LOTTERY LIST IS ={}".format(a,randomlist))
print("PLEASE PAY PRICE = {}".format(price_ticket))
for i in randomlist:
    if i == lucky_number:
        result = 1
        break
    else:
        result = 0
if result == 1:
    print("CONGRATULATIONS! {} HAS WON THE LOTTERY".format(a))
else:
    print("SORRY! PLEASE TRY AGAIN!")
