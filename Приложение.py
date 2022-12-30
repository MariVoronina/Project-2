from faker import Faker # библиотека для создания фейковых данных
from faker.providers import BaseProvider # абстрактный класс для написания провайдера
from tkinter import messagebox
import json
import tkinter as tk # библиотека для работы с оконным приложением
from tkinter import *
from tkinter import ttk # модуль, содержащий классы виджетов и методы для изменения их внешнего вида
from tkinter.ttk import Notebook # подмодуль для работы со вкладками в оконном приложении
from tkinter.ttk import Style # класс для работы со стилем
import pandas as pd # модуль для обработки и анализа данных


sqr_list = ["150-200", "200-300", "300-400", "400-500"] # список для выбора площади при работе с интерфейсом
address_list = ["'Emerald Village', Московская область", "'Ренессанс Парк', Московская область",
                "'Березки. River Village', Московская область", "'Довиль', Московская область",
                "'Папушево', Московская область", "'Новое Аристово', Московская область",
                "'Изумрудный город', Ломоносовский район", "'Приветное', Выборгский район СПб",
                "'Онегин Парк', Пушкинский район СПб", "'ПриЛЕСный 2.0', Всеволожский район СПб",
                "'Елагино',  Ломоносовский район СПб", "'Honkanova Concept Residence', Курортный район СПб"]
price_list = ["10000000-50000000", "50000000-100000000", "100000000-150000000", "150000000-200000000"] # список для
# выбора адреса при работе с интерфейсом
elec_list = ["Есть", "Нет"] # список для выбора наличия электричества при работе с интерфейсом
heat_list = ["Газовое", "Электрическое", "Дровяное"] # список для выбора типа отопления при работе с интерфейсом
ws_list = ["Есть", "Нет"] # список для выбора наличия водоснабжения при работе с интерфейсом


# класс для описания фейковых данных
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


# класс, реализующий наш провайдер
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

    ELECTRICITY = ["Нет", "Есть"]

    SEWERAGE = ["Нет", "Есть"]

    WS = ["Нет", "Есть"]

    fake_code = Faker("ru_RU")

    # функция для создания фейковых данных
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

df = pd.DataFrame(data=data) # созданные нами фейковые данные по коттеджам


# функция, которая находит подходящие данные по коттеджам по заданным параметрам
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


# функция, которая реализует "красивый" вывод данных по коттеджам
def info(dat):
    li = []
    for i, row in dat.iterrows():
       li.append(f"ID коттеджа: {row['Cottage ID']} \n" +
              f"Площадь: {row['Cottage square']} \n" +
              f"Количество комнат: {row['Number of rooms']} \n" +
              f"Количество этажей: {row['Number of floors']} \n" +
              f"Год постройки: {row['Year of building']} \n" +
              f"Адрес: {row['Cottage address']} \n" +
              f"Цена: {row['Cottage price']} \n" +
              f"Электричество: {row['Electricity']} \n" +
              f"Отопление: {row['Heating']} \n" +
              f"Наличие канализации: {row['Sewerage']} \n" +
              f"Водоснабжение: {row['Water supplying']} \n")
    return li


# функция, которая подбирает оптимальный вариант по Джеоффриону
def optimal_dg(n: float, m: float, res):
    op = res.assign(Deviation=n*(res["Cottage square"].max() - res["Cottage square"]) +
                              m*(res["Cottage price"] - res["Cottage price"].min()))
    t = op.to_json(orient='index')
    file_name = 'Results.json'
    with open(file_name, 'w+') as f:
        json.dump(t, f)
    m = op["Deviation"].idxmin()
    return res.loc[[m]]


# функция, выводящая список коттеджей, удовлетворяющих запрос
def clicked1():
    #проверяем, заполнены ли все ячейки и выводим сообщение об ошибке в противном случае
    if var1.get() == '' or var2.get() == '' or var3.get() == '' or var4.get() == '' or var5.get() == '' or var6.get() == '':
        messagebox.showinfo('Ошибка', 'Заполните все ячейки!')
    else:
        linfo = info(find_variants(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()))
        wind = tk.Tk()  # создаем окно
        wind.title('Информация о коттеджах')  # задаем название окна
        wind.geometry('1000x700')  # задаем размер окна
        wind.configure(bg='SystemButtonFace')  # задаем цвет фона
        container = ttk.Frame(wind, width=1000, height=700)
        canvas = Canvas(container, width=800, height=700)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas, width=1000, height=700)
        img1 = PhotoImage(master=canvas, file='этаж1.png')  # картинка
        img2 = PhotoImage(master=canvas, file='этаж2.png')  # картинка
        img3 = PhotoImage(master=canvas, file='этаж3.png')  # картинка
        # функция, вызывающаяся всякий раз, когда изменяется содержимое прокручиваемого фрейма
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set, background='SystemButtonFace')

        for i in range(len(linfo)):
            numder_floors = find_variants(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get())["Number of floors"].iloc[i]
            if numder_floors == 1:
                ttk.Label(scrollable_frame, image=img1).grid(row=i, column=0)
            if numder_floors == 2:
                ttk.Label(scrollable_frame, image=img2).grid(row=i, column=0)
            if numder_floors == 3:
                ttk.Label(scrollable_frame, image=img3).grid(row=i, column=0)
            ttk.Label(scrollable_frame,
                      text=linfo[i],
                      wraplength=600, justify="left", background='SystemButtonFace', foreground="darkblue",
                      font=("Times New Roman", 20)).grid(row=i, column=1, padx=(15, 0))

        container.pack()
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        wind.mainloop()



def select():
    winds = tk.Tk()  # создаем окно
    winds.title('Оптимальный вариант')  # задаем название окна
    winds.geometry('800x450')  # задаем размер окна
    winds.configure(bg='paleturquoise')  # задаем цвет фона
    n12 = float(str(v.get()))
    m12 = 1 - n12
    result = info(optimal_dg(n12, m12, find_variants(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get())))
    ttk.Label(winds,
              text=result[0],
              wraplength=800, justify="center", background='paleturquoise', foreground="darkblue",
              font=("Times New Roman", 20)).pack()
    winds.mainloop()


window = tk.Tk()
window.title('Cottage')
window.geometry('750x750')
style = Style()
style.theme_use('default')
style.configure('TNotebook.Tab', background="paleturquoise", font=('URW Gothic L','25','bold')) # неактивная вкладка окна будет цвета paleturquoise


note = Notebook(window) # создаем виджет Notebook
frame1 = Frame(note, width= 750, height=750) # добавляем рамку для первой вкладки
frame1.configure(background="paleturquoise")
note.add(frame1, text= 'Выбор дома') # добавляем имя вкладки

# frame1
ttk.Label(frame1, text = "Площадь:", font = ("Times New Roman", 25), background = 'paleturquoise', foreground ="darkblue").grid(column = 0,
		row = 1, padx = 10, pady = 25) # создаем виджет для отображения текста
v1 = StringVar() # переменная, содержащая строковые данные
var1 = ttk.Combobox(frame1, width = 20, textvariable = v1, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем площадь
var1['values'] = sqr_list
var1.grid(column = 1, row = 1) # расположение в окне
var1.current()


ttk.Label(frame1, text = "Адрес:", font = ("Times New Roman", 25), background = 'paleturquoise',foreground ="darkblue").grid(column = 0,
		row = 2, padx = 10, pady = 25)
v2 = StringVar()
var2 = ttk.Combobox(frame1, width = 20, textvariable = v2, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем адрес
var2['values'] = address_list # в качестве сроковых данных используем список адресов
var2.grid(column = 1, row = 2)
var2.current()


ttk.Label(frame1, text = "Цена:", font = ("Times New Roman", 25), background = 'paleturquoise',foreground ="darkblue").grid(column = 0,
		row = 3, padx = 10, pady = 25)
v3 = StringVar()
var3 = ttk.Combobox(frame1, width = 20, textvariable = v3, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем цену
var3['values'] = price_list # в качестве сроковых данных используем список цен
var3.grid(column = 1, row = 3)
var3.current()

ttk.Label(frame1, text = "Электричество:", font = ("Times New Roman", 25), background = 'paleturquoise',foreground ="darkblue").grid(column = 0,
		row = 4, padx = 10, pady = 25)
v4 = StringVar()
var4 = ttk.Combobox(frame1, width = 20, textvariable = v4, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем наличие электричества
var4['values'] = elec_list # в качестве сроковых данных используем список да/нет
var4.grid(column = 1, row = 4)
var4.current()

ttk.Label(frame1, text = "Отопление:", font = ("Times New Roman", 25), background = 'paleturquoise',foreground ="darkblue").grid(column = 0,
		row = 5, padx = 10, pady = 25)
v5 = StringVar()
var5 = ttk.Combobox(frame1, width = 20, textvariable = v5, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем отопление
var5['values'] = heat_list # в качестве сроковых данных используем список типов отопления
var5.grid(column = 1, row = 5)
var5.current()

ttk.Label(frame1, text = "Водоснабжение:", font = ("Times New Roman", 25), background = 'paleturquoise',foreground ="darkblue").grid(column = 0,
		row = 6, padx = 10, pady = 25)
v6 = StringVar()
var6 = ttk.Combobox(frame1, width = 20, textvariable = v6, font=("Times New Roman", 20)) # выпадающий список, в котором выбираем наличие водоснабжения
var6['values'] = ws_list # в качестве сроковых данных используем список да/нет
var6.grid(column = 1, row = 6)
var6.current()

button1 = Button(frame1, text="Вывести информацию", font = ("Times New Roman", 25),
                 background="darkblue", foreground ='paleturquoise', command=clicked1).grid(column = 1, row =7) #кнопка для построения вывода информации


ttk.Label(frame1, text = "Цена        Площадь", font = ("Times New Roman", 15), justify="left", background = 'paleturquoise',foreground ="darkblue").grid(column = 0,
		row = 8)


v = StringVar()
scale = Scale(frame1, variable=v, from_=0.1, to=0.9, resolution = 0.1, orient=HORIZONTAL, activebackground = "cyan", highlightbackground= "darkblue").grid(column = 0, row =9)


btn = Button(frame1, text="Выбрать оптимальный",font = ("Times New Roman", 25), background="darkblue", foreground ='paleturquoise', command=select).grid(column = 1, row =9)
#кнопка для выбора оптимального
note.pack(expand= True, fill=BOTH)
window.mainloop()
