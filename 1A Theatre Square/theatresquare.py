from math import ceil

data = input().split()

n = int( data[0] )
m = int( data[1] )
a = int( data[2] )

nn = ceil( n / a )
mm = ceil( m / a )
print(nn * mm)