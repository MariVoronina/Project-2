from faker import Faker
from faker.providers import BaseProvider
import pandas as pd


sqr_list = ["150-200", "200-300", "300-400", "400-500"]
address_list = ["'Emerald Village', Московская область", "'Ренессанс Парк', Московская область",
                "'Березки. River Village', Московская область", "'Довиль', Московская область",
                "'Папушево', Московская область", "'Новое Аристово', Московская область",
                "'Изумрудный город', Ломоносовский район", "'Приветное', Выборгский район СПб",
                "'Онегин Парк', Пушкинский район СПб", "'ПриЛЕСный 2.0', Всеволожский район СПб",
                "'Елагино',  Ломоносовский район СПб", "'Honkanova Concept Residence', Курортный район СПб"]
price_list = ["10000000-50000000", "50000000-100000000", "100000000-150000000", "150000000-200000000"]
elec_list = ["Да", "Нет"]
heat_list = ["Газовое", "Электрическое", "Дровяное"]
ws_list = ["Да", "Нет"]


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
                 "'Ренессанс Парк', Московская область, городской округ Истра, д. Чесноково",
                 "'Березки. River Village', Московская область, Одинцовский район, Горки-8",
                 "'Довиль', Московская область, г. Одинцово-2, пос. Довиль",
                 "'Папушево', Московская область, Одинцовский район, д. Папушево",
                 "'Новое Аристово', Московская область, городской округ Солнечногорск, д. Юрлово",
                 "'Изумрудный город', Ломоносовский район, локация «Ропшинское шоссе», деревня Райкузи",
                 "'Приветное', Выборгский район СПб, посёлок Приветнинское",
                 "'Онегин Парк', Пушкинский район СПб",
                 "'ПриЛЕСный 2.0', Всеволожский район СПб",
                 "'Елагино',  Ломоносовский район СПб, деревня Оржицы",
                 "'Honkanova Concept Residence', Курортный район СПб, посёлок Солнечное, Колхозная улица"]

    HEATING = ["Газовое", "Электрическое", "Дровяное"]

    ELECTRICITY = ["Нет", "Да"]

    SEWERAGE = ["Нет", "Да"]

    WS = ["Нет", "Да"]

    fake_code = Faker("ru_RU")

    def create_fake_cottage(self):
        cottage = Cottage(self.fake_code.bothify(text="#######"))
        cottage.square = self.random_int(150, 500)
        cottage.address = self.random_element(self.ADDRESSES)
        cottage.rooms = self.random_int(10, 25)
        cottage.price = self.random_int(10000000, 200000000)
        cottage.floors = self.random_int(1, 3)
        cottage.year = self.random_int(2015, 2022)
        cottage.electricity = self.random_element(self.ELECTRICITY)
        cottage.heating = self.random_element(self.HEATING)
        cottage.sewerage = self.random_element(self.SEWERAGE)
        cottage.ws = self.random_element(self.WS)
        return cottage


my_faker = Faker()
my_faker.add_provider(CottageProvider)
data = []
for i in range(100000):
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


def find_variants(square: str, address: str, price: str, electricity: str, heating: str, ws: str):
    sqr1 = int(square.split("-")[0])
    sqr2 = int(square.split("-")[1])
    prc1 = int(price.split("-")[0])
    prc2 = int(price.split("-")[1])
    var = pd.DataFrame()
    for i, row in df.iterrows():
        if ((sqr1 <= row["Cottage square"] <= sqr2) and (address in row["Cottage address"])
                and (prc1 <= row["Cottage price"] <= prc2) and (electricity == row["Electricity"])
                and (heating == row["Heating"]) and (ws == row["Water supplying"])):
            r = pd.DataFrame({"Cottage ID": [row["Cottage ID"]], "Cottage square": [row["Cottage square"]],
                              "Cottage address": [row["Cottage address"]], "Number of rooms": [row["Number of rooms"]],
                              "Cottage price": [row["Cottage price"]], "Number of floors": [row["Number of floors"]],
                              "Year of building": [row["Year of building"]], "Electricity": [row["Electricity"]],
                              "Heating": [row["Heating"]], "Sewerage": [row["Sewerage"]],
                              "Water supplying": [row["Water supplying"]]})
            var = pd.concat([var, r], ignore_index=True)
    return var


def info(dat):
    for i, row in dat.iterrows():
        print(f"Cottage ID: {row['Cottage ID']} \n" +
              f"Cottage square: {row['Cottage square']} \n" +
              f"Number of rooms: {row['Number of rooms']} \n" +
              f"Number of floors: {row['Number of floors']} \n" +
              f"Year of building: {row['Year of building']} \n" +
              f"Address: {row['Cottage address']} \n" +
              f"Price: {row['Cottage price']} \n" +
              f"Electricity: {row['Electricity']} \n" +
              f"Heating: {row['Heating']} \n" +
              f"Sewerage: {row['Sewerage']} \n" +
              f"Water Supplying: {row['Water supplying']} \n")


def optimal_meter(res):
    op = res.assign(Price_of_meter=round(res["Cottage price"] / res['Cottage square'], 2))
    m = op["Price_of_meter"].idxmin()
    return res.loc[[m]]


def optimal_dg(n: float, m: float, res):
    op = res.assign(Deviation=n*(res["Cottage square"].max() - res["Cottage square"]) +
                              m*(res["Cottage price"] - res["Cottage price"].min()))
    m = op["Deviation"].idxmin()
    return res.loc[[m]]


# info(find_variants("150-200", "'Березки. River Village', Московская область", "20000000-50000000", "Да",
                   #"Дровяное", "Нет"))
# info(optimal_dg(0.4, 0.6, find_variants("150-200", "'Березки. River Village', Московская область", "20000000-50000000",
                                        #"Да", "Дровяное", "Нет")))
