# импортирование модуля для создания графического интерфейса
from tkinter import Tk, Label, CENTER, Entry, Button
from tkinter import messagebox

window = Tk()
window.title('Авторизация')  # окно с титульником "Авторизация"
window.geometry('450x230')  # разрешение окна
window.resizable(False, False)
font_header = ('Arial', 20)  # шрифт
font_entry = ('Arial', 16)  # шрифт
label_font = ('Arial', 14)  # шрифт
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}


def clicked():
    username = username_entry.get()
    password = password_entry.get()
    messagebox.showinfo('Заголовок', '{username}, {password}'
                        .format(username=username, password=password))


main_label = Label(window, text='Авторизация',
                   justify=CENTER, **header_padding)
main_label.pack()


username_label = Label(window, text='Имя пользователя',
                       font=label_font, **base_padding)  # поле для ввода
# имени пользователя

username_label.pack()

username_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
username_entry.pack()
# поле для ввода пароля
password_label = Label(window, text='Пароль',
                       font=label_font, **base_padding)
password_label.pack()

password_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
password_entry.pack()
# кнопка с текстом "Войти"
send_btn = Button(window, text='Войти', command=clicked)
send_btn.pack(**base_padding)

window.mainloop()
