userInput =input("Enter your message you wish to save:")

with open('file/data.txt', 'w') as file:
    file.write(userInput)
