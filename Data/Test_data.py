from faker import Faker

class Data:
    def name_generator(self):
        fake= Faker()
        full_name= fake.name()
        return full_name

    def description_generator(self):
        fake= Faker()
        description= fake.name()
        return description

    def date_generator(self):
        fake = Faker()
        date = fake.date()
        return date
