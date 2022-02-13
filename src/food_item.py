from foods import Foods


class FoodItem:
    def __init__(self, food_type, calories, fat, taste_score):
        self.food_type = Foods[food_type]
        self.calories = int(calories)
        self.fat = int(fat)
        self.taste_score = int(taste_score)

    def __str__(self):
        return f"{self.food_type}, calories: {self.calories}, fat: {self.fat}, taste score: {self.taste_score}"

    def increment_calories(self, calories):
        self.calories += calories

    @staticmethod
    def get_most_caloric_food(food_items):
        if food_items.length == 0:
            return None

        most_caloric_food = food_items[0]
        for food in food_items:
            if food.calories > most_caloric_food.calories:
                most_caloric_food = food
        return most_caloric_food

    @staticmethod
    def get_least_fatty_food(food_items):
        if food_items.length == 0:
            return None

        least_fatty_food = food_items[0]
        for food in food_items:
            if food.fat < least_fatty_food.calories:
                least_fatty_food = food
        return least_fatty_food
