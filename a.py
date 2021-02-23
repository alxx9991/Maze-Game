def pamper(cats):
    longest_string = 0
    output = ""
    for string in cats:
        print(f"{string} is being fed. {string} looks happy!")
        if len(string) > longest_string:
            longest_string = len(string)
            output = string
        else:
            pass
    if output == "":
        print("There are no cats here :(")
        return "No cats :("
    else:
		return output