def GetFirstNumbersFromString(string):
    num_string = ""
    for word in list(string):
        if word.isdigit() or word == ".":
            num_string += word
        elif num_string != "" :
            break
    return num_string
