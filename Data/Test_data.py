import random
import string

class Data:
    def name_generator(access_token):
        first_name = ['Pranjal', 'Anuj', 'Saroj']
        last_name = ['Timsina','Pokhrel','Karki']
        full_name= f"{random.choice(first_name)} {random.choice(last_name)}"
        return full_name

    def description_generator(access_token):
        description= (random.choice(string.ascii_letters))
        return description