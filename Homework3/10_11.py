# Name: Vu Tran
# Student ID: 2233511

class FoodItem:
    def __init__(self, food_name="None", food_fat=0.0, food_carbs=0.0, food_protein=0.0, food_serving=0.0, ):
        # Initialize a FoodItem object with a name, fat content,
        # carbohydrate content, protein content, and serving size.

        # The default values are "None" for the name, and 0.0 for the rest of the properties.
        self.name = food_name
        self.fat = food_fat
        self.carbs = food_carbs
        self.protein = food_protein
        self.serving = food_serving

    def get_calories(self, number_servings):
        # Calculate the total number of calories for a given number of servings based on the fat, carbohydrate,
        # and protein content of the food item.
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * number_servings
        return calories

    def print_info(self):
        # Print out the nutritional information of the food item.
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == "__main__":
    # Create a FoodItem object with default values for food_item1.
    food_item1 = FoodItem()

    # Prompt the user to enter the name, fat content, carbohydrate content, and protein content for food_item2.
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)

    # Prompt the user to enter the number of servings.
    num_servings = float(input())

    # Print out the nutritional information and calorie information for food_item1 and food_item2.
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    food_item1.get_calories(num_servings)))
    print()
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,
                                                                    food_item2.get_calories(num_servings)))