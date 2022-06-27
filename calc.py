from tkinter import *
from tkinter.messagebox import *
from random import *

def counter(key):
    if key in '0123456789+-*/.()':
        entry.insert(END, key)
    elif key == '√':
        entry.insert(END, '**(0.5)')
    elif key == 'x²':
        entry.insert(END, '**(2)')
    elif key == 'x³':
        entry.insert(END, '**(3)')
    elif key == '=':
        try:
            result = eval(entry.get())
            entry.insert(END, '=' + str(result))
        except SyntaxError:
            showerror('Ошибка!',
                      'Ошибка ввода')
        except ZeroDivisionError:
            showerror('Ошибка',
                      'Деление на ноль')
        except NameError:
            showerror('Ошибка',
                      'Недопустимое'
                      ' значение')
    elif key == 'C':
        entry.delete(0, END)
    elif key == '←':
        entry.delete(
            len(entry.get())-1)

def about():
    showinfo('О программе...',
             'Было трудно, но'
             'я сделал это. '
             'Апрель, 2022')

def themes(t):
    if t == 1:
        win.config(bg=
                   'lightgray')
        win.title('Калькулятор. '
                  'Светлая тема')
        for i in buttons:
            i.config(fg='black',
                     bg='white')

    else:
        if t == 2:
            win.config(bg=
                       'darkgray')
            win.title('Калькулятор. '
                      'Темная тема')
            for i in buttons:
                i.config(fg='white',
                         bg='dimgray')

        else:
            if t == 3:
                color_random = choice(colors)
                win.config(bg=
                           'firebrick')
                win.title('Калькулятор. Цветная тема')
                for d in range(0, 8):
                    buttons[d].config(fg='yellow',
                                      bg=color_random)
                color_random = choice(colors)
                for d in range(8, 16):
                    buttons[d].config(fg='yellow',
                                      bg=color_random)
                color_random = choice(colors)
                for d in range(16, 24):
                    buttons[d].config(fg='yellow',
                                      bg=color_random)


def setting():
    win2 = Tk()
    win2.title('Настройки темы')
    win2.geometry('300x150' +
                 '+600+100')
    Label(win2, text='Цветовая'
                     ' гамма')\
        .grid(row=0, column=0)

    t = IntVar()
    cmd = lambda x=1: themes(x)
    R1 = Radiobutton(win2,
                     text='Светлая',
                     variable=t,
                     value=1, command=cmd)
    R1.grid(row=1,
            column=0,
            sticky=W)
    R1.select()

    cmd = lambda x=2: themes(x)
    R2 = Radiobutton(win2,
                     text='Темная',
                     variable=t,
                     value=2, command=cmd)
    R2.grid(row=2,
            column=0,
            sticky=W)
    cmd = lambda x=3: themes(x)
    R3 = Radiobutton(win2,
                     text='Цветная',
                     variable=t,
                     value=3, command=cmd)
    R3.grid(row=3,
            column=0,
            sticky=W)

win = Tk()
win.title('Калькулятор')
win.resizable(width=False,
              height=False)

m = Menu(win)
win.config(menu=m)

item1 = Menu(m, tearoff=0)
m.add_cascade(label='Справка',
              menu=item1)
item1.add_command(
    label='О программе',
    command=about)

m.add_command(label='Настройки',
              command=setting)


entry = Entry(width=60,
              bd=3,
              relief=SUNKEN)
entry.grid(row=0,
           columnspan=8)

colors = ['red', 'green', 'blue', 'purple', 'black', 'gray']

buttons_all = ['7', '8', '9', '0', '+', '-', '*', '/',
               '4', '5', '6', 'x²', 'x³', '√', '(', ')',
               '1', '2', '3', '.', '←', 'C', '=', '',
              ]

buttons = []

c = 0
r = 1
for i in buttons_all:
    cmd = lambda x=i: counter(x)
    btn = Button(win,
                 text=i,
                 width=8,
                 bd=4,
                 command=cmd, font=('bold'))

    btn.grid(row=r, column=c,
             padx=1, pady=1)
    buttons.append(btn)
    c += 1
    if c > 7:
        c = 0
        r += 1


win.mainloop()