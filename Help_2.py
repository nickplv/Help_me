DEFAULT_VALUE = int(100)
should_terminate = True

class Calculator:
    def  __init__(self, protein, fat, calories, carbohydrate, serving, DEFAULT_VALUE):
        self.protein = protein
        self.fat = fat
        self.calories = calories
        self.carbohydrate = carbohydrate
        self.serving = serving
        self.DEFAULT_VALUE = DEFAULT_VALUE


    def protein_per_serving(self):
        return round((self.protein * self.serving) / self.DEFAULT_VALUE, 2)


    def fat_per_serving(self):
        return round((self.fat * self.serving) / self.DEFAULT_VALUE, 2)


    def calories_per_serving(self):
        return round((self.calories * self.serving) / self.DEFAULT_VALUE, 2)


    def carbohydrate_per_serving(self):
        return round((self.carbohydrate * self.serving) / self.DEFAULT_VALUE, 2)
#
# def requirements():
#     serving = float(input("Please tell me the serving you are interested in: "))
#     calories = float(input("please tell me the amount of calories per 100 gr: "))
#     carbohydrate = float(input("please tell me the amount of carbohydrate per 100 gr: "))
#     fat = float(input("please tell me the amount of fat per 100 gr: "))
#     protein = float(input("please tell me the amount of protein per 100 gr: "))
#     return serving, calories, carbohydrate, fat, protein

def results():
    print(f"{user_input} has: \n"
          f"-CALORIES for your {serving}gr serving:", food.calories_per_serving(), "grams\n"
          f"-CARBOHYDRATE for your {serving}gr serving:",
          food.carbohydrate_per_serving(), "grams\n"
          f"-FAT for your {serving}gr serving:", food.fat_per_serving(), "grams\n"
          f"-PROTEIN for your {serving}gr serving:", food.protein_per_serving(), "grams\n")


while should_terminate:

    user_input = input("What food are you interested in? ").upper()
    Default_Value_Change = input("""Measures are based on tables using per 100 grams values. Are you ok? """)


    if "y" in Default_Value_Change:
        serving = float(input("Please tell me the serving you are intrested in: "))
        calories = float(input("please tell me the amount of calories per 100 gr: "))
        carbohydrate = float(input("please tell me the amount of carbohydrate per 100 gr: "))
        fat = float(input("please tell me the amount of fat per 100 gr: "))
        protein = float(input("please tell me the amount of protein per 100 gr: "))

        food = Calculator(protein, fat, calories, carbohydrate, serving, DEFAULT_VALUE)

        results()

    else:
        DEFAULT_VALUE = int(input("Please define in per what value is your table based? "))
        serving = float(input("Please tell me the serving you are intrested in: "))
        calories = float(input("please tell me the amount of calories per 100 gr: "))
        carbohydrate = float(input("please tell me the amount of carbohydrate per 100 gr: "))
        fat = float(input("please tell me the amount of fat per 100 gr: "))
        protein = float(input("please tell me the amount of protein per 100 gr: "))

        food = Calculator(protein, fat, calories, carbohydrate, serving, DEFAULT_VALUE)

        results()

    should_terminate = input("would you like to terminate the calculator? \n").lower()
    if "y" in should_terminate:
        print("Thank you for using calculator")
        should_terminate = False
        
        """κανονικά για πιο σωστό θα το έγραφα έτσι: DEFAULT_VALUE = int(input("Please define in per what value is your table based? "))
                                                     serving = float(input(f"Please tell me the serving you are interested in: "))
                                                     calories = float(input(f"please tell me the amount of calories per {DEFAULT_VALUE} gr: "))
                                                     carbohydrate = float(input(f"please tell me the amount of carbohydrate per {DEFAULT_VALUE} gr: "))
                                                     fat = float(input(f"please tell me the amount of fat per {DEFAULT_VALUE} gr: "))
                                                     protein = float(input(f"please tell me the amount of protein per {DEFAULT_VALUE} gr: "))γραμμές 64 - 69

Σκοπός μου όμως είναι να δω (πες οτι ήταν 100% ιδιες όπως τις έχω αφήσει εδώ) πως θα αποφύγω την επανάληψη?

με το function results το κατάφερα
με το class calculator το κατάφερα. 
με το function requirements Δεν το κατάφερα, ίσως θέλει άλλον τρόπο?? άλλη διαδικασία??"""

