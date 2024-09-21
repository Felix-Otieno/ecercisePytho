a = "ABC123DEF456"

def answer(string):
    alphabet = ""
    result = 0
    for char in string:
        if char.isdigit():
            result += int(char)
        else:
            alphabet += char
    return(alphabet, result) 
print(answer(a))           