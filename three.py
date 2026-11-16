import json
p = {"Имя": "Алексей", "Группа": "КБ-101", "Навыки": ["Python", "Excel"], "Уведомления": True} # создаём словарь профиля
with open('participant.json', 'w', encoding='utf-8') as f: # сохраняем в json
    json.dump(p, f, ensure_ascii=False)
with open('participant.json', 'r', encoding='utf-8') as f: # читаем обратно
    p = json.load(f)
p["Навыки"].append("CSV") # добавляем навык и отключаем уведомления
p["Уведомления"] = False
with open('participant.json', 'w', encoding='utf-8') as f: # сохраняем и выводим
    json.dump(p, f, ensure_ascii=False)
with open('participant.json', 'r', encoding='utf-8') as f:
    p = json.load(f)
print("Имя:", p["Имя"])
print("Группа:", p["Группа"])
print("Навыки:", p["Навыки"])
print("Уведомления:", p["Уведомления"])