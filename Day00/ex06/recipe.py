cookbook = {
            'sandwich': {'ingredients': ['bread', 'ham', 'cheese', 'tomatoes'],
                         'meal': 'lunch', 'prep_time': '10'},
            'cake': {'ingredients': ['flour', 'sugar', 'eggs'],
                     'meal': 'dessert', 'prep_time': '60'},
            'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes',
                      'spinach'], 'meal': 'lunch', 'prep_time': '15'},
            }


def menu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def aff_recip(recipe):
    print("Recipe for %s:" % recipe)
    print("Ingredients list: %s" % cookbook[recipe]['ingredients'])
    print("To be eaten for: %s" % cookbook[recipe]['meal'])
    print("Takes %s minutes of cooking" % cookbook[recipe]['prep_time'])


def aff_dico():
    for recipe in cookbook:
        aff_recip(recipe)


def del_recip(recipe):
    cookbook.pop(recipe)


def add_recip(recipe, ingredients, meal, prep_time):
    cookbook[recipe] = {'ingredients': ingredients, 'meal': meal,
                        'prep_time': prep_time}


def main():
    menu()
    value = 0
    while value != 5:
        value = input("Please select an option:")
        if value == '1':
            ingr = []
            name = input("Please enter the name of the new recipe:")
            nbingr = input("Please enter the number of ingredients:")
            if nbingr.isdigit() == 1:
                for i in range(int(nbingr)):
                    ingr.append(input("Please enter the ingredients:"))
                meal = input("Please enter the type of meal:")
                prep_time = input("Please enter the time required to cook:")
                add_recip(name, ingr, meal, prep_time)
            else:
                print("please enter a number and try again")
        elif value == '2':
            recipe = input("Please choose a recipe to delete:")
            del_recip(recipe)
        elif value == '3':
            recipe = input("Please choose a recipe to print:")
            aff_recip(recipe)
        elif value == '4':
            aff_dico()
        elif value == '5':
            print("Goodbye !")
            return
        else:
            print("This is not an existing option")


main()
