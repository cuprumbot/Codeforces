text = input()

if ( int(text) >= 0 ):
    print(text)
else:
    ultimo = int( text[ : -1] )
    penultimo = int( text[ : -2] + text[-1] )

    print( max(ultimo, penultimo) )