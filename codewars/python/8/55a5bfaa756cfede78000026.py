def problem(a):
    return a*50+6 if type(a)!=str else "Error"

print( problem(12) )
print( problem("Value") )