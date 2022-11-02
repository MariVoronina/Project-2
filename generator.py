from faker import Faker
from faker.providers import BaseProvider
import pandas as pd


class Cottage:
    def __init__(self, code):
        self.code = code
        self.square = None
        self.address = None
        self.rooms = None
        self.price = None
        self.floors = None
        self.year = None
        self.electricity = None
        self.heating = None
        self.sewerage = None
        self.ws = None

    def __str__(self):
        info: str = f"Cottage ID: {self.code} \n" \
                    f"Cottage square: {self.square} \n" \
                    f"Number of rooms: {self.rooms} \n" \
                    f"Number of floors: {self.floors} \n" \
                    f"Year of building: {self.year} \n" \
                    f"Address: {self.address} \n" \
                    f"Price: {self.price} \n" \
                    f"Electricity: {self.electricity} \n" \
                    f"Heating: {self.heating} \n" \
                    f"Sewerage: {self.sewerage} \n" \
                    f"Water Supplying: {self.ws} \n"
        return info


class CottageProvider(BaseProvider):
    ADDRESSES = ["'Emerald Village', Московская область, Рузский городской округ",
                 "'Ренессанс Парк', Московская обл., городской округ Истра, д. Чесноково",
                 "'Березки. River Village', Московская обл., Одинцовский район, Горки-8",
                 "'Довиль', Московская обл., г. Одинцово-2, пос. Довиль",
                 "'Папушево', Московская область, Одинцовский район, д. Папушево",
                 "'Новое Аристово', Московская область, городской округ Солнечногорск, д. Юрлово",
                 "'Изумрудный город', Ломоносовский район, локация «Ропшинское шоссе», деревня Райкузи",
                 "'Приветное', Выборгский район СПб, посёлок Приветнинское",
                 "'Онегин Парк', Пушкинский район СПб",
                 "'ПриЛЕСный 2.0', Всеволожский район СПб",
                 "'Елагино',  Ломоносовский район СПб, деревня Оржицы",
                 "'Honkanova Concept Residence', Курортный район СПб, посёлок Солнечное, Колхозная улица"]

    HEATING = ["Газовое", "Электрическое", "Дровяное", "Солнечная энергия"]

    ELECTRICITY = ["Нет", "Да"]

    SEWERAGE = ["Нет", "Да"]

    WS = ["Нет", "Да"]

    fake_code = Faker("ru_RU")

    def create_fake_cottage(self):
        cottage = Cottage(self.fake_code.bothify(text="???-###"))
        cottage.square = self.random_int(150, 500)
        cottage.address = self.random_element(self.ADDRESSES)
        cottage.rooms = self.random_int(10, 25)
        cottage.price = self.random_int(30000000, 200000000)
        cottage.floors = self.random_int(2, 4)
        cottage.year = self.random_int(2015, 2022)
        cottage.electricity = self.random_element(self.ELECTRICITY)
        cottage.heating = self.random_element(self.HEATING)
        cottage.sewerage = self.random_element(self.SEWERAGE)
        cottage.ws = self.random_element(self.WS)
        return cottage


my_faker = Faker()
my_faker.add_provider(CottageProvider)
data = []
for i in range(10):
    fak = my_faker.create_fake_cottage()
    dat = {"Cottage ID": fak.code,
           "Cottage square": fak.square,
           "Cottage address": fak.address,
           "Number of rooms": fak.rooms,
           "Cottage price": fak.price,
           "Number of floors": fak.floors,
           "Year of building": fak.year,
           "Electricity": fak.electricity,
           "Heating": fak.heating,
           "Sewerage": fak.sewerage,
           "Water supplying": fak.ws}
    data.append(dat)

df = pd.DataFrame(data=data)
print(df)
