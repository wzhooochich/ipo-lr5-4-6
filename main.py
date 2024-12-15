# Инициализация списка
new_line = []

# Чтение файла по строкам
with open('example.txt', 'r') as file:
    for line in file:
        new_line.append(line[::-1])  # Переворачивает каждую строку и добавляет в список

# Запись в файл
with open('output.txt', 'w') as file:
    file.write(''.join(new_line))  # Объединяет список в строку и записывает в файл
