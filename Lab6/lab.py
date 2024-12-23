class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password  # приватный атрибут

    def set_password(self, new_password):
        self.__password = new_password
        print("Пароль изменён успешно.")

    def check_password(self, password):
        return self.__password == password


# Создание объекта класса UserAccount
user = UserAccount(input("Name:"), input("Email:"), input("Password:"))

# Изменение пароля
user.set_password("new_secure_password")

# Проверка пароля
is_correct = user.check_password("new_secure_password")
print("Пароль верный:", is_correct)
