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
    :param list_of_foods: list of FoodItem objects to sort
    :param sort_by: the criteria to sort by. Can be 'calories', 'fat', or 'taste score'.
    :return:
    """
    if sort_by.lower() == 'calories':
        _quicksort_food_by_calories( list_of_foods, 0, len(list_of_foods) - 1 )
    elif sort_by.lower() == 'fat':
        _quicksort_food_by_fat( list_of_foods, 0, len(list_of_foods) - 1 )
    elif sort_by.lower() == 'taste score' or sort_by.lower() == 'taste_score':
        _quicksort_food_by_taste_score( list_of_foods, 0, len(list_of_foods) - 1 )


def graph_avg_calories(list_of_foods):
    """
        Read in a list of foods, and create a MatPlotLib bar graph displaying the
        average calories of each food type in the list.
        items and
        :param list_of_foods: a list of FoodItem objects
        :return: None
    """
    # Create some variables for the bar graph.
    pizza_items = [food for food in list_of_foods if food.food_type == Foods.PIZZA]
    soup_items = [food for food in list_of_foods if food.food_type == Foods.SOUP]
    fruit_items = [food for food in list_of_foods if food.food_type == Foods.FRUIT]
    salad_items = [food for food in list_of_foods if food.food_type == Foods.SALAD]
    sandwich_items = [food for food in list_of_foods if food.food_type == Foods.SANDWICH]

    pizza_avg_calories = avg_calories(pizza_items)
    soup_avg_calories = avg_calories(soup_items)
    fruit_avg_calories = avg_calories(fruit_items)
    salad_avg_calories = avg_calories(salad_items)
    sandwich_avg_calories = avg_calories(sandwich_items)

    # x-/y-axis
    food_types = ['PIZZA', 'SOUP', 'FRUIT', 'SALAD', 'SANDWICH']
    averages = [pizza_avg_calories, soup_avg_calories, fruit_avg_calories, salad_avg_calories, sandwich_avg_calories]

    # Display and save bar graph.
    fig = plt.figure()
    plt.bar(food_types, averages)
    plt.xlabel('Food')
    plt.ylabel('Average calories')
    plt.show()
    fig.savefig(os.path.join('..', 'data', 'average_calories.png'))


def write_food_to_file(list_of_foods, output_filepath):
    """Given a list of foods and an output file, write the foods to the file."""
    with open(output_filepath, 'wt') as f:
        writer = csv.writer(f)
        for food in food_items:
            writer.writerow([food])


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

    # Display bar graph.
    graph_avg_calories(food_items)

    # Sort the food items by calories, fat, and taste score.
    # Write the sorted lists to text files.
    filepath_1 = os.path.join('..', 'data', 'unsorted_foods.txt')
    filepath_2 = os.path.join('..', 'data', 'sorted_by_calories.txt')
    filepath_3 = os.path.join('..', 'data', 'sorted_by_fat.txt')
    filepath_4 = os.path.join('..', 'data', 'sorted_by_taste_score.txt')

    write_food_to_file(food_items, filepath_1)
    sort_food(food_items, 'calories')
    write_food_to_file(food_items, filepath_2)
    sort_food(food_items, 'fat')
    write_food_to_file(food_items, filepath_3)
    sort_food(food_items, 'taste score')
    write_food_to_file(food_items, filepath_4)
