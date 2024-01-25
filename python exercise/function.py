def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet(pet_name="Harry", animal_type="hamster")



def make_pizza(*toppings):
    print("Making a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni', 'green peppers', 'extra cheese')