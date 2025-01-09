def print_info_pet(name, age):
    print(f"My dog {name} is {age} years old.")


my_pet = {"name": "Ultra", "age": 3}

print_info_pet(**my_pet)
