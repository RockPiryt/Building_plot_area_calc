#Imports
from tkinter import *

#Constans_______________________________________________________________
#Colors
DARK_GREEN ='#125C13'
GREEN ='#3E7C17'
ORANGE='#F4A442'
LIGHT ='#E8E1D9'
RED = '#e23d3d'

TITLE_FONT = ('Arial', 20, 'bold')
LABEL_FONT = ('Arial', 14, 'bold')
BUTTON_FONT = ('Arial', 10, 'bold')

#Window config__________________________________________________________
window = Tk()
window.title('Building plot Converter')
window.iconbitmap('plot.ico')
window.minsize(width=500, height=300)
window.resizable(True,True)
window.config(bg=LIGHT, padx=50, pady=20)

#Layout________________________________________________________________

#Graphics
canvas = Canvas(width=200, height=200, bg=LIGHT, highlightthickness=0)
plot_img=PhotoImage(file='field.png')
canvas.create_image(100,100, image=plot_img)
canvas.grid(row=2, column=2, rowspan=5)


#Labels and entiries#########

title_label = Label(text='Calculate area of your plot', font=TITLE_FONT, bg=LIGHT, fg=DARK_GREEN)
title_label.grid(row=0, column=1, columnspan=3, pady=20)

input_label = Label(text='Enter size of your plot in metr', font=LABEL_FONT, bg=LIGHT)
input_label.grid(row=2, column=3, columnspan=2)

a_label = Label(text='a =', font=LABEL_FONT, bg=LIGHT, fg=ORANGE, anchor='e')
a_label.grid(row=3, column=3, sticky='EW')
a_entry = Entry()
a_entry.grid(row=3, column=4, sticky='EW')

b_label = Label(text='b =', font=LABEL_FONT, bg=LIGHT, fg=ORANGE, anchor='e')
b_label.grid(row=4, column=3, sticky='EW')
b_entry = Entry()
b_entry.grid(row=4, column=4, sticky='EW')

calculate_button = Button(text='Calculate area', bg=RED, fg=LIGHT, font=LABEL_FONT)
calculate_button.grid(row=7, column=0, columnspan=5, sticky='EW')

area_label = Label(text='Your plot have:', font=LABEL_FONT, bg=LIGHT)
area_label.grid(row=8, column=1, columnspan=3,pady=(50, 0))
area_entry= Entry()
area_entry.grid(row=9, column=2, sticky='EW')
area_label = Label(text='m2', font=LABEL_FONT, bg=LIGHT)
area_label.grid(row=9, column=3)


convert_label = Label(text='Convert to diffrent unit', font=TITLE_FONT, bg=LIGHT, fg=DARK_GREEN)
convert_label.grid(row=10, column=1, columnspan=3,pady=(50, 0))

first_value_label = Label(text='First value', font=LABEL_FONT, bg=LIGHT)
first_value_label.grid(row=11, column=0)
first_value_entry= Entry()
first_value_entry.grid(row=11, column=1, sticky='EW', pady=20)
equal_label = Label(text='=', font=LABEL_FONT, bg=LIGHT)
equal_label.grid(row=11, column=2)
second_value_label = Label(text='Second value', font=LABEL_FONT, bg=LIGHT)
second_value_label.grid(row=11, column=3)
second_value_entry= Entry()
second_value_entry.grid(row=11, column=4, sticky='EW')

calculate_button = Button(text='Convert unit', bg=RED, fg=LIGHT, font=LABEL_FONT)
calculate_button.grid(row=12, column=0, columnspan=5, sticky='EW')

window.mainloop()


