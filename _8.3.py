from tkinter import *
import smtplib
import ssl
import imghdr
from email.message import EmailMessage
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import re


current_theme = "lIGHT THEME"
files = []  

def change_theme(theme):
    global current_theme
    if theme == "lIGHT THEME":
        aken.configure(bg="white")
        pealkiri.configure(bg="lightgreen", fg="black")
        pealkiri2.configure(bg="lightgreen", fg="black")
        pealkiri3.configure(bg="lightgreen", fg="black")
        pealkiri4.configure(bg="lightgreen", fg="black")
        sisestus.configure(bg="lightyellow", fg="black")
        sisestus2.configure(bg="lightyellow", fg="black")
        sisestus3.configure(bg="lightyellow", fg="black")
        nupp.configure(bg="lightgreen", fg="black")
        nupp_2.configure(bg="lightgreen", fg="black")
        clearnupp.configure(bg="red", fg="black")
    elif theme == "DARK THEME":
        aken.configure(bg="black")
        pealkiri.configure(bg="darkgreen", fg="white")
        pealkiri2.configure(bg="darkgreen", fg="white")
        pealkiri3.configure(bg="darkgreen", fg="white")
        pealkiri4.configure(bg="darkgreen", fg="white")
        sisestus.configure(bg="darkgray", fg="white")
        sisestus2.configure(bg="darkgray", fg="white")
        sisestus3.configure(bg="darkgray", fg="white")
        nupp.configure(bg="darkgreen", fg="white")
        nupp_2.configure(bg="darkgreen", fg="white")
        clearnupp.configure(bg="darkred", fg="white")
    current_theme = theme

def toggle_theme():
    global current_theme
    if current_theme == "Светлая тема":
        change_theme("Темная тема")
    else:
        change_theme("Светлая тема")

def validate_subject(teema):
    if not teema.strip():
        messagebox.showerror("Ошибка", "Тема не может быть пустой!")
        return False
    return True 

def change_theme(theme):
    """Функция для изменения темы интерфейса."""
    if theme == "Светлая тема":
        aken.configure(bg="white")
        pealkiri.configure(bg="lightgreen", fg="black")
        pealkiri2.configure(bg="lightgreen", fg="black")
        pealkiri3.configure(bg="lightgreen", fg="black")
        pealkiri4.configure(bg="lightgreen", fg="black")
        sisestus.configure(bg="lightyellow", fg="black")
        sisestus2.configure(bg="lightyellow", fg="black")
        sisestus3.configure(bg="lightyellow", fg="black")
        nupp.configure(bg="lightgreen", fg="black")
        nupp_2.configure(bg="lightgreen", fg="black")
        clearnupp.configure(bg="red", fg="black")
    elif theme == "Темная тема":
        aken.configure(bg="black")
        pealkiri.configure(bg="darkgreen", fg="white")
        pealkiri2.configure(bg="darkgreen", fg="white")
        pealkiri3.configure(bg="darkgreen", fg="white")
        pealkiri4.configure(bg="darkgreen", fg="white")
        sisestus.configure(bg="darkgray", fg="white")
        sisestus2.configure(bg="darkgray", fg="white")
        sisestus3.configure(bg="darkgray", fg="white")
        nupp.configure(bg="darkgreen", fg="white")
        nupp_2.configure(bg="darkgreen", fg="white")
        clearnupp.configure(bg="darkred", fg="white")

def validate_subject(teema):
    if not teema.strip():
        messagebox.showerror("Ошибка", "Тема не может быть пустой!")
        return False
    return True  


def valid_pilt():
    global files  
    files = askopenfilename()  
    pealkiri3.configure(text = "Выбрано: " + files)
    return files


def saada_kiri():
    kellele = sisestus.get()
    kiri = sisestus3.get("1.0", END)
    
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "eldar040503@gmail.com"
    password = "wqwp zjly akcd rwyp"
    context = ssl.create_default_context()
    
    msg = EmailMessage()
    msg.set_content(kiri)
    msg['Subject'] = "E-kiri saatmine"
    msg['From'] = "Eldar Aliev"
    msg['To'] = kellele
    
    if files:  
        with open(files, 'rb') as fpilt:
            pilt = fpilt.read()
            msg.add_attachment(pilt, maintype='image', subtype=imghdr.what(None, pilt))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.send_message(msg)
        messagebox.showinfo("Информация", "Письмо отправлено успешно")
    except Exception as e:
        messagebox.showerror("Произошла ошибка!", e)
    finally:
        server.quit()


def clear_fields():
    sisestus.delete(0, END)
    sisestus2.delete(0, END)
    sisestus3.delete("1.0", END)
    pealkiri3.configure(text="Выбрано: ") 


aken = Tk()
aken.title("Отправка письма")
aken.geometry("600x600")
aken.configure(bg="gray")
aken.resizable(width=False, height=False)

# Надписи
pealkiri = Label(aken, text="Email:", bg="black", font=("Arial", 30), fg="pink", justify="center")
pealkiri2 = Label(aken, text="Teema:", bg="black", font=("Arial", 30), fg="pink", justify="center")
pealkiri3 = Label(aken, text="Lisa", bg="black", font=("Arial", 30), fg="pink", justify="center")
pealkiri4 = Label(aken, text="Kiri:", bg="black", font=("Arial", 30), fg="pink")

# Поля ввода
sisestus = Entry(aken, bg="lightyellow", font=("Arial", 30), fg="pink", width=22)
sisestus.insert(0, "")

sisestus2 = Entry(aken, bg="lightyellow", font=("Arial", 30), fg="pink", width=21)
sisestus2.insert(0, "")

sisestus3 = Text(aken, bg="lightyellow", font=("Arial", 30), fg="pink", width=60)
sisestus3.insert("1.0", "")

# Кнопки
nupp = Button(aken, text="Lisa pilt", bg="black", font=("Arial", 30), fg="pink", relief=RAISED, command=valid_pilt)
nupp_2 = Button(aken, text="Saada", bg="black", font=("Arial", 30), fg="pink", relief=RAISED, command=saada_kiri)
clearnupp = Button(aken, text="Clear", bg="black", font=("Arial", 30), fg="pink", relief=RAISED, command=clear_fields)
theme_button = Button(aken, text="Theme", bg="black", font=("Arial", 20), fg="pink", relief=RAISED, command=toggle_theme)

# Размещение виджетов
pealkiri.place(x=0, y=0)
pealkiri2.place(x=0, y=50)
pealkiri3.place(x=0, y=100)
pealkiri4.place(x=0, y=250)

sisestus.place(x=111, y=0)
sisestus2.place(x=140, y=50)
sisestus3.place(x=75, y=150, height=200, width=350)

nupp.place(x=75, y=350, height=50)
nupp_2.place(x=250, y=350, height=50)
clearnupp.place(x=150, y=420)
theme_button.place(x=150, y=500)

aken.mainloop()