departments = {
    'продажу': {
        'співробітники': ['Федорчук', 'Григоренко'],
        'менеджер': 'Григоренко',
        'завідувач': 'Федорчук'
    },
    'розробка': {
        'співробітники': ['Василенко', 'Валько', 'Бондаренко'],
        'менеджер': 'Валько',
        'завідувач': 'Бондаренко'
    }
}

# допиши виведення даних. Не забувай про тире перед прізвищем
print("Завідуючі відділів:")
for departament in departments:
    print("-", departments[departament]['завідувач'])
print("Проектні менеджери відділів:")
for departament in departments:
    print("-", departments[departament]['менеджер'])