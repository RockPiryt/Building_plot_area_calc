#Imports
from tkinter import *
from tkinter import ttk
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
COMBOBOX_FONT = ('Arial', 8, 'bold')

#Window config__________________________________________________________
window = Tk()
window.title('Building plot Converter')
window.iconbitmap('plot.ico')
window.minsize(width=500, height=300)
window.resizable(True,True)
window.config(bg=LIGHT, padx=50, pady=20)

#Commands________________________________________________________________

def calculate_area():
    '''Calculate area from 2 values'''

    #Clear previous output
    area_entry.delete(0, END)
    first_value_entry.delete(0, END)

    #Get values from user
    a = float(a_entry.get())
    b = float(b_entry.get())
    print(a)
    print(type(a))

    #Calculate area in m2 - return float
    area_m2 = a * b

    #Return value in area_entry and first_value_entry
    area_entry.insert(0, f'{area_m2}') #index for insert!
    first_value_entry.insert(0, f'{area_m2}') #index for insert!

    return area_m2#float

# c = calculate_area()


# def change_unit(c):
#     system_values = {
#         'm2':1,
#         'ar': 100,
#         'ha':10000,
#         'km2':1000000
#     }
    
#     #Clear previous output
#     second_value_entry.delete(0, END)

#     #Get all information
#     first_unit = input_combobox.get()
#     second_unit = output_combobox.get()
    
#     #convert do base unit
#     base_value = c*system_values[first_unit]
#     #convert to new area value
#     end_value = base_value/system_values[second_unit]

#     #Show converted value
#     second_value_entry.insert(0, str(end_value))





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

#Button calculate
calculate_button = Button(text='Calculate area', bg=RED, fg=LIGHT, font=LABEL_FONT, command=calculate_area)
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

#Values
area_values = ['m2', 'ar', 'ha', 'km2']

# #Dropdown
# input_choice = StringVar()#to see string value in dropdown
# input_choice.set('m2')
# input_dropdown = OptionMenu(window, input_choice, *area_values)
# input_dropdown.grid(row=12, column=0, columnspan=2, sticky='EW')

# output_choice = StringVar()
# output_choice.set('ha')
# output_dropdown = OptionMenu(window, output_choice, *area_values)
# output_dropdown.grid(row=12, column=3, columnspan=2, sticky='EW')

# to_label = Label(text='to', font=LABEL_FONT, bg=LIGHT)
# to_label.grid(row=12, column=2)

#Combobox
input_combobox = ttk.Combobox(window, values=area_values, font=COMBOBOX_FONT, justify='center')
input_combobox.grid(row=12, column=0, columnspan=2, sticky='EW', pady= (0,20))
input_combobox.set('m2')
output_combobox = ttk.Combobox(window, values=area_values, font=COMBOBOX_FONT, justify='center')
output_combobox.grid(row=12, column=3, columnspan=2, sticky='EW', pady= (0,20))
output_combobox.set('ha')

#convert button
convert_button = Button(text='Convert unit', bg=RED, fg=LIGHT, font=LABEL_FONT, command=change_unit)
convert_button.grid(row=14, column=0, columnspan=5, sticky='EW')





window.mainloop()