cant = int( input() )
coins = input().split()
coins = [int(c) for c in coins]

coins.sort(reverse = True)

theirCoins = 0
for n in coins:
    theirCoins = theirCoins + n

myCoins = 0
for index, c in enumerate(coins):
    myCoins = myCoins + c
    theirCoins = theirCoins - c

    if myCoins > theirCoins:
        print(index + 1)
        break
