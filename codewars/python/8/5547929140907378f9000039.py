def shortcut( s ):
    string = ""
    for letter in s:
        if letter not in ['a','e','i','o','u']:
            string += letter
    return string

print( shortcut("HELLO") )