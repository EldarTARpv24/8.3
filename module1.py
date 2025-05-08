from tkinter import *
import math
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

def leia_juured():
    a_val = sisestus.get().strip()
    b_val = sisestus2.get().strip()
    c_val = sisestus3.get().strip()

    # Сброс цвета на нормальный
    sisestus.configure(bg="lightblue")
    sisestus2.configure(bg="lightblue")
    sisestus3.configure(bg="lightblue")

    # Проверка на пустоту и подсветка только пустых полей
    if not a_val or not b_val or not c_val:
        if not a_val:
            sisestus.configure(bg="red")
        if not b_val:
            sisestus2.configure(bg="red")
        if not c_val:
            sisestus3.configure(bg="red")
        pealkiri2.config(text=" Заполните все поля!")
        return

    try:
        a = float(a_val)
        b = float(b_val)
        c = float(c_val)

        if a == 0:
            pealkiri2.config(text=" 'a' не может быть 0!")
            return

        D = b**2 - 4*a*c

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2*a)
            x2 = (-b - math.sqrt(D)) / (2*a)
            tulemus = f" 2 корня: x₁ = {x1:.2f}, x₂ = {x2:.2f}"
        elif D == 0:
            x = -b / (2*a)
            tulemus = f" 1 корень: x = {x:.2f}"
        else:
            tulemus = " Нет действительных корней"

        pealkiri2.config(text=tulemus)

    except ValueError:
        pealkiri2.config(text="Введите числа!")



def joonista():
    a_val = sisestus.get().strip()
    b_val = sisestus2.get().strip()
    c_val = sisestus3.get().strip()

    if not a_val or not b_val or not c_val:
        pealkiri2.config(text=" Заполните все поля для графика!")
        return

    try:
        a = float(a_val)
        b = float(b_val)
        c = float(c_val)

        # Генерация значений x и y для графика
        x = np.linspace(-10, 10, 400)
        y = a*x**2 + b*x + c

        plt.figure(figsize=(6, 4))
        plt.plot(x, y, label=f'{a}x² + {b}x + {c}')
        plt.axhline(0, color='black',linewidth=1)
        plt.axvline(0, color='black',linewidth=1)
        plt.title(f'График функции: {a}x² + {b}x + {c}')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        pealkiri2.config(text="Введите корректные числа для графика!")





aken = Tk()                      
aken.title("Квадратные уравнения")       
aken.geometry("800x300")        
aken.configure(bg="white")      
aken.resizable(width=False, height=False) 
#------------------------------------------------------------------------------------------------------
# тут заголовки
pealkiri = Label(aken, text="Решение квадратного уравнения", bg="lightblue", font=("Arial", 25), fg="green")  
pealkiri2 = Label(aken, text="Решение", bg="yellow", font=("Arial", 20), fg="black")
pealkiri3 = Label(aken, text="x**2+", bg="white", font=("Arial", 30), fg="green")
pealkiri4 = Label(aken, text="x+", bg="white", font=("Arial", 30), fg="green")
pealkiri5 = Label(aken, text="=0", bg="white", font=("Arial", 30), fg="green")
#------------------------------------------------------------------------------------------------------
# тут поля для ввода 
sisestus=Entry(aken, bg="lightblue", font=("Arial", 30), fg="black", width=3)  
sisestus.insert(0, "")  
#---
sisestus2=Entry(aken, bg="lightblue", font=("Arial", 30), fg="black", width=3)  
sisestus.insert(0, "")
#---
sisestus3=Entry(aken, bg="lightblue", font=("Arial", 30), fg="black", width=3)  
sisestus.insert(0, "")
#Кнопка
nupp = Button(aken, text="Решение", bg="green", font=("Arial", 25), fg="black", relief=RAISED, command=leia_juured)
nupp_2 = Button(aken, text="График", bg="green", font=("Arial", 25), fg="black", relief=RAISED, command=joonista)


#-----------------------------------------------------------------------------------------------------
# Это короче чтобы заголовки и кнопочки там работали
pealkiri.pack()
pealkiri2.place(x=300, y=250)
pealkiri3.place(x=70, y=100)
pealkiri4.place(x=250, y=100)
pealkiri5.place(x=370, y=100)

sisestus.place(x=0, y=100)
sisestus2.place(x=175, y=100)
sisestus3.place(x=300, y=100)

nupp.place(x=425, y=90)
nupp_2.place(x=600, y=90)

#-----------------------------------------------------------------------------------------------------
# Это короче запуск
aken.mainloop()

