import csv
# 01 Создаём файл purchases.csv
with open('purchases.csv', 'w', newline='', encoding='utf-8') as f: #  создали файл
    w = csv.writer(f)
    w.writerow(['Товар', 'Цена за штуку', 'Количество'])
    w.writerow(['Тетрадь', 2.50, 4])
    w.writerow(['Ручка', 1.20, 3])
    w.writerow(['Папка', 4.00, 2])
    w.writerow(['Маркер', 3.30, 1])
t = 0  # общая сумма
with open('purchases.csv', 'r', encoding='utf-8') as f: #Читает CSV-файл
    r = csv.reader(f)
    h = next(r)  # пропускает заголовок
    for p in r: # Выводим данные и считаем
        n = p[0]
        c = float(p[1])
        q = int(p[2])
        s = c * q
        t += s
        print(f'{n}: цена {c}, количество {q}, стоимость {s:.2f}')
print(f'Общая сумма: {t:.2f}')