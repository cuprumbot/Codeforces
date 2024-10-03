first  = list( input() )
second = list( input() )
third  = list( input() )

first.sort()
second.sort()
third.sort()

answer = "NO"
pos = 0
for letter in third:
    if (len(first) > 0 and first[0] == letter):
        first.pop(0)
    elif (len(second) > 0 and second[0] == letter):
        second.pop(0)
    else:
        answer = "NO"
        break

    pos = pos + 1

# terminamos de consumir el primero y segundo
if ( (len(first) == 0) and (len(second) == 0) ):

    # tambien terminamos de consumir el tercero
    if (len(third) == pos):
        answer = "YES"
    else:
        answer = "NO"

elif ( len(third) < ( len(first) + len(second) ) ):
    answer = "NO"

print(answer)