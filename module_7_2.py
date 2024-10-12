def custom_write(file_name, strings):
    strings_positions = {}

    with open(file_name, 'w', encoding='utf-8') as file:
        for i, string in enumerate(strings, 1):  # Нумерация строк начинается с 1
            position = file.tell()  # Получаем текущую позицию курсора в файле
            file.write(string + '\n')  # Записываем строку в файл
            strings_positions[(i, position)] = string  # Сохраняем номер строки и позицию

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)


