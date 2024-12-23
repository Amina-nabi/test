def read_file(file_name):
    try:
        with open("2example.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Файл не найден.")
read_file("C: New folder 3_main.py")
