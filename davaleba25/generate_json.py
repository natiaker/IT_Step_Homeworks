import random
import json
from faker import Faker

fake = Faker()


# function to write randomly generated information about a person into a file
def generate_json(file_name):
    data_list = []

    with open(file_name, 'w') as file:
        for i in range(100):
            person = {"name": fake.name(), "age": random.randint(1, 100), "address": fake.address()}
            data_list.append(person)
        json.dump(data_list, file, indent=4)


file_names = ["file1.json", "file2.json", "file3.json"]
# generate JSON for every file
for name in file_names:
    generate_json(name)

