with open("user_input.txt", "a") as file:
    for i in range(3):
        file.write(input() + "\n")
