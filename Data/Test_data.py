from faker import Faker

class Data:
    def name_generator(access_token):
        fake= Faker()
        full_name= fake.name()
        return full_name

    def description_generator(access_token):
        fake= Faker()
        full_name= fake.name()
        return full_name