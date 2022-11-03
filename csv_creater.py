# заголовок таблицы (запущен 1 раз в начале)
def create_table():
    with open ('Phonebook.csv', 'w', encoding = 'utf-8') as file_csv:
        file_csv.write(f'Фамилия,Имя,Номер телефона,Описание\n')

# создать таблицу csv
def create_csv(data):
    s, n, p, d = data
    with open('Phonebook.csv', 'a', encoding = 'utf-8') as file_csv:
        file_csv.write(f'{s},{n},{p},{d}\n')
    return data

# формирование текста из таблицы csv
def read_csv_text():
    text = ''
    file_csv = open('Phonebook.csv', 'r', encoding = 'utf-8')
    for line in file_csv:       
            text += line
    file_csv.close()
    return text

        