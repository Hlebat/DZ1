f = open('diary.txt', 'w', encoding='utf-8') # Создаем файл и записываем первые три записи
f.write('Сегодня мы работали с файлами Python.\n')
f.write('Научились сохранять текст.\n')
f.write('Узнали, как читать данные обратно.\n')
f.close()
f = open('diary.txt', 'a', encoding='utf-8') # Добавляем четвертую запись
f.write('Следующее занятие – CSV и JSON\n')
f.close()
f = open('diary.txt', 'r', encoding='utf-8') # Читаем файл и выводим содержимое
lines = f.readlines()
f.close()
print('Содержимое дневника:')
for line in lines:
    print(line.strip())
print('Количество записей:', len(lines))