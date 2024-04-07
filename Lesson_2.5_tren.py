#логические операторы
user_login = "adam" 
user_password = "Qwerty123456" 
login = input("Login: ") 
password = input("Password: ")
if (login == user_login) and (password == user_password):
     print("Добро пожаловать") 
else: 
     print("Неверный логин или пароль")