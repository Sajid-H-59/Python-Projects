names_string = input("Give me everybody's names. seperated by a coma ")

names = names_string.split(", ")

import random

unknown_name_count = random.random() * (int(len(names)))

x = int(unknown_name_count)


print(f"Today {names[x]} is going to pay for dinner")