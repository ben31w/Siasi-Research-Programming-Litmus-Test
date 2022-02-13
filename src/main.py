import csv

from food_item import FoodItem


if __name__ == '__main__':
    foods = []
    filepath = '../resources/FoodInputData.csv'
    with open(filepath, 'rt') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader, None)  # skip the header line

        for line in reader:
            food = FoodItem(line[0], line[2], line[3], line[4])
            print(food)
            foods.append(food)



