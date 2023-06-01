def are_you_playing_banjo(name):
    return f"{name} " + "plays banjo" if name[0].lower()=='r' else "doesnt play"

print( are_you_playing_banjo("Rafa") )