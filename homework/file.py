def info_pet(name, age):
    print(f"My dog {name} is {age} years old.")


pet = {"name": "Ultra", "age": 3}

info_pet(**pet)
