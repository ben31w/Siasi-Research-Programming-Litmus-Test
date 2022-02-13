from foods import Foods


class FoodItem:
    def __init__(self, food_type, calories, fat, taste_score):
        self.food_type = Foods[food_type]
        self.calories = int(calories)
        self.fat = int(fat)
        self.taste_score = int(taste_score)

    def __str__(self):
        return f"{self.food_type}, calories: {self.calories}, fat: {self.fat}, taste score: {self.taste_score}"
