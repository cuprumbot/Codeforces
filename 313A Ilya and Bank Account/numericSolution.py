num = int( input() )

if (num > 0):
    print(num)
else:
    num = num * -1

    # quitar el ultimo
    uno = num // 10
    uno = uno * -1

    # quitar el penultimo
    last = num % 10
    temp = num // 100
    temp = temp * 10
    dos = temp + last
    dos = dos * -1

    print( max(uno, dos) )
