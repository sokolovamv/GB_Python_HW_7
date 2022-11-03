# ввод фамилии с проверкой
def get_surname():
    surname = input("Введите фамилию: ")
    while not surname.isalpha():
        surname = input("Введите фамилию: ")
    return surname

# ввод имени с проверкой
def get_name():
    name = input("Введите имя: ")
    while not name.isalpha():
        name = input("Введите имя: ")
    return name

# ввод номера с проверкой
def get_phone_number():
    flag = False
    while not flag:
        phone_number = input("Введите номер телефона без кода страны (10 символов): ")
        if phone_number.isdigit() and len(phone_number) == 10:
            flag = True   
        else:
            print('Пожалуйста, введите номер телефона в правильном формате')
    return '+7' + phone_number

# ввод описания
def get_description():
    return input("Введите описание: ")


def data_collection():
    return(get_surname(), get_name(), get_phone_number(), get_description())
