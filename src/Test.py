# import tkinter as tk
#
# root = tk.Tk()
#
# canvas1 = tk.Canvas(root, width=400, height=300)
# canvas1.pack()
#
# entry1 = tk.Entry(root)
# canvas1.create_window(200, 140, window=entry1)
#
#
# def getSquareRoot():
#     x1 = entry1.get()
#
#     label1 = tk.Label(root, text=float(x1)**0.5)
#     canvas1.create_window(200, 230, window=label1)
#
#
# button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
# canvas1.create_window(200, 180, window=button1)
#
# root.mainloop()


from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F2B90C')

def display_selected(choice):
    choice = variable.get()
    print(choice)


countries = ['Bahamas','Canada', 'Cuba','United States']


# setting variable for Integers
variable = StringVar()
variable.set(countries[3])

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *countries,
    command=display_selected
)

# positioning widget
dropdown.pack(expand=True)

# infinite loop
ws.mainloop()
