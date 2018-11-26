
name = input ("Enter your name:")
letter = ""

for x in range (len(name)):
    char = name[x]

    if char == "A":
        letter +="b"
    elif char == "B":
        letter += "c"
    elif char == "C":
        letter += "D"
    elif char == "d":
        letter += "E"
    elif char == "e":
        letter+= "F"
    elif char == "f":
        letter += "G"
    elif char == "g":
        letter += "H"
    elif char == "h":
        letter += "I"
    elif char == "i":
        letter += "J"
    elif char == "j":
        letter += "G"
    elif char == "g":
        letter += "K"
    elif char == "k":
        letter += "L"
    elif char == "l":
        letter += "M"
    elif char == "M":
        letter+= "N"
    elif char == "n":
        letter += "O"
    elif char == "o":
        letter += "P"
    elif char == "p":
        letter += "Q"
    elif char == "q":
        letter += "R"
    elif char == "r":
        letter += "S"
    elif char == "s":
        letter += "T"
    elif char == "t":
        letter += "U"
    elif char == "u":
        letter += "V"
    elif char == "v":
        letter += "W"
    elif char == "w":
        letter += "X"
    elif char == "x":
        letter += "Y"
    elif char == "y":
        letter += "Z"
    elif char == "z":
        letter += "a"
    else:
        letter += char
print (letter)
