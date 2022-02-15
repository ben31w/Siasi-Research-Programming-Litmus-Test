import csv
import os
import matplotlib.pyplot as plt

from food_item import FoodItem
from foods import Foods
from sort_helpers import _quicksort_food_by_calories, _quicksort_food_by_fat, _quicksort_food_by_taste_score


def total_calories(list_of_foods):
    """Return the total calories from a list of food items."""
    total = 0
    for food in list_of_foods:
        total += food.calories
    return total


def avg_calories(list_of_foods):
    """Return the average calories from a list of food items."""
    sum = total_calories(list_of_foods)
    return sum / len(list_of_foods)


def sort_food(list_of_foods, sort_by):
    """
        Sort the given list of foods by the given sort by parameter.
        Can sort by calories, fat, or taste score.
    """
    if sort_by.lower() == 'calories':
        _quicksort_food_by_calories( list_of_foods, 0, len(list_of_foods) - 1 )
    elif sort_by.lower() == 'fat':
        print()
    elif sort_by.lower() == 'taste score' or sort_by.lower() == 'taste_score':
        print()


if __name__ == '__main__':
    # Open CSV file and create a list of all the food in the file.
    food_items = []
    filepath = os.path.join('..', 'resources', 'FoodInputData.csv')
    with open(filepath, 'rt') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)  # skip the header line

        for line in reader:
            food = FoodItem(line[0], line[2], line[3], line[4])
            food_items.append(food)

    # Create some variables for the bar graph.
    pizza_items = [food for food in food_items if food.food_type == Foods.PIZZA]
    soup_items = [food for food in food_items if food.food_type == Foods.SOUP]
    fruit_items = [food for food in food_items if food.food_type == Foods.FRUIT]
    salad_items = [food for food in food_items if food.food_type == Foods.SALAD]
    sandwich_items = [food for food in food_items if food.food_type == Foods.SANDWICH]

    pizza_avg_calories = avg_calories(pizza_items)
    soup_avg_calories = avg_calories(soup_items)
    fruit_avg_calories = avg_calories(fruit_items)
    salad_avg_calories = avg_calories(salad_items)
    sandwich_avg_calories = avg_calories(sandwich_items)

    food_types = ['PIZZA', 'SOUP', 'FRUIT', 'SALAD', 'SANDWICH']
    averages = [pizza_avg_calories, soup_avg_calories, fruit_avg_calories, salad_avg_calories, sandwich_avg_calories]

    # Create and display bar graph.
    fig = plt.figure()
    plt.bar(food_types, averages)
    # This line would display the total calories of each food type:
    # plt.bar([food.food_type.name for food in food_items], [food.calories for food in food_items])
    plt.xlabel('Food')
    plt.ylabel('Average calories')
    plt.show()
    fig.savefig(os.path.join('..', 'graphs', 'average_calories.png'))

    # Demonstrating a sort function...
    for food in food_items:
        print(food, end=' ;; ')
    print("\n\n")
    sort_food(food_items, sort_by='calories')
    for food in food_items:
        print(food, end=' ;; ')

