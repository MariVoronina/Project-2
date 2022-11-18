from tkinter import *                     # python 3+
from tkinter import ttk
def select():
    sel = "Наша хрень = " + v.get()
    label.config(text=sel)


top = Tk()
top.geometry("200x100")
v = StringVar()
scale = Scale(top, variable=v, from_=0.1, to=0.9, resolution = 0.1, orient=HORIZONTAL, activebackground = "cyan", highlightbackground= "mediumslateblue")
scale.pack(anchor=CENTER)

btn = Button(top, text="Вычислить", command=select)
btn.pack(anchor=CENTER)

label = Label(top)
label.pack()

top.mainloop()
print(v.get())

languages = ["Python", "JavaScript", "C#", "Java", "C++", "Rust", "Kotlin", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "R", "Go", "C",
             "T-SQL", "PL-SQL", "Typescript", "Assembly", "Fortran"]

root = Tk()
root.title("METANIT.COM")
root.geometry("250x200")

languages_var = StringVar(value=languages)
listbox = Listbox(listvariable=languages_var)
listbox.pack(side=LEFT, fill=BOTH, expand=1)

scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

listbox["yscrollcommand"] = scrollbar.set

root.mainloop()



canvas = tk.Canvas(parent)
scroll_y = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)

frame = tk.Frame(canvas)
# group of widgets
for i in range(20):
    tk.Label(frame, text='label %i' % i).pack()
# put the frame in the canvas
canvas.create_window(0, 0, anchor='nw', window=frame)
# make sure everything is displayed before configuring the scrollregion
canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'),
                 yscrollcommand=scroll_y.set)

canvas.pack(fill='both', expand=True, side='left')
scroll_y.pack(fill='y', side='right')




linfo = info(find_variants(var1.get(), var2.get(), var3.get(), var4.get(), var5.get(), var6.get()))
    wind = tk.Tk()  # создаем окно
    wind.title('Information about cottages')  # задаем название окна
    wind.geometry('800x750')  # задаем размер окна
    wind.configure(bg='linen')  # задаем цвет фона

    linfo_var = StringVar(value=linfo)
    listbox = Listbox(listvariable=linfo_var)
    listbox.pack(side=LEFT, fill=BOTH, expand=1)

    scrollbar = ttk.Scrollbar(orient="vertical", command=listbox.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox["yscrollcommand"] = scrollbar.set

    wind.mainloop()