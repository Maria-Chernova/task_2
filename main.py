cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            ingredient_name = ingredient['ingredient_name']
            quantity = ingredient['quantity'] * person_count
            measure = ingredient['measure']

            if ingredient_name not in shop_list:
                shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}
            else:
                shop_list[ingredient_name]['quantity'] += quantity

    return shop_list



print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


files = ['1.txt', '2.txt']
output_file = "output.txt"

file_info = []
for filename in files:
    with open(filename, 'r') as file:
        lines = file.readlines()
        file_info.append((filename, len(lines), lines))

file_info.sort(key=lambda x: x[1])

with open(output_file, 'w') as output:
    for file_data in file_info:
        output.write(file_data[0] + '\n')
        output.write(str(file_data[1]) + '\n')
        for line in file_data[2]:
            output.write(line)

print("Готово! Результат записан в файл", output_file)
