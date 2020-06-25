"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""

month = int (input("Введите номер месяца:"))
seasons_list = ('зима',
                'весна',
                'лето',
                'осень',
                )

seasons_dictionary = {'зима': (1, 2, 12),
                'весна': (3, 4, 5),
                'лето': (6, 7, 8),
                'осень': (9, 10, 11),
                }

season_idx = month // 3 % 4

for key, value in seasons_dictionary.items():
    if month in value:
        print(key)
        break

print(season_idx)
print(seasons_list[season_idx])