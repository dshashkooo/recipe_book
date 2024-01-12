import os
import pprint

with open('cook_book.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for i in range(ingredients_count):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        cook_book[dish_name] = ingredients
        file.readline()

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for meal in dishes:
        if meal in cook_book:
            for ingredient in cook_book[meal]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {'measure': ingredient['measure'], 'quantity': ingredient['quantity'] * person_count}
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list

pprint.pprint(get_shop_list_by_dishes(['Фахитос','Омлет'], 2))