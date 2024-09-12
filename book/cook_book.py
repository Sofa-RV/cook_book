from pprint import pprint
def parse_cook_book(filename):
    cook_book = {}
    try:
        with open(filename, 'rt') as f:
            while True:
                try:
                    line = f.readline().strip()
                    if not line:
                        break
                    cook_name = line
                except:
                    print(f"Ошибка: Не удалось прочитать название рецепта в файле {filename}")
                    continue
                ingredients = []
                try:
                    ingredients_count = int(f.readline().strip())
                except ValueError:
                    print(f"Ошибка: Неверный формат количества ингредиентов в рецепте {cook_name}")
                    continue
                for _ in range(ingredients_count):
                    try:
                        ingredient_name, quantity, measure = f.readline().strip().split(' | ')
                        quantity = int(quantity)
                    except (ValueError, IndexError) as e:
                        print(f"Ошибка: Неверный формат ингредиента в рецепте {cook_name}: {e}")
                    else:
                        ingredients.append({
                            'ingredient_name': ingredient_name,
                            'quantity': quantity,
                            'measure': measure
                        })
                try:
                    f.readline()
                except:
                    print(f"Ошибка: Ожидалась пустая строка после рецепта {cook_name}")
                    continue
                cook_book[cook_name] = ingredients
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(f"Ошибка обработки файла {filename}: {e}")
    return cook_book
def get_shop_list_dishes(cook_book, person_count, dishes):
    dish_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] in dish_dict:
                    dish_dict[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
                else:
                    dish_dict[ingredient['ingredient_name']] = {
                        'measure': ingredient['measure'],
                        'quantity': ingredient['quantity'] * person_count
                    }
        else:
            print(f"Блюдо {dish} не найдено в книге рецептов.")
    return dish_dict
cook_book = parse_cook_book('recipes.txt')
pprint(cook_book)
pprint(get_shop_list_dishes(cook_book, 2, ['Омлет', 'Фахитос', 'Пирог']))