import tkinter as tk
from tkinter import *
from tkinter import ttk

root = tk.Tk()
root.title("Converter Application AxxA")
root.geometry('1280x720')

notebook = ttk.Notebook(root)
notebook.pack(pady=10,expand=True)


#create frames
frame_ASCII = Frame(notebook, width=1280, height=720, bg='#800000')

frame_Number = Frame(notebook, width=1280, height=720, bg='#800000')

notebook.add(frame_ASCII, text='ASCII Converter')
notebook.add(frame_Number, text='Number Converter')

notebook.pack(expand=True, fill='both')

style = ttk.Style()
style.theme_create("my_theme", parent="alt", settings={
    "TNotebook.Tab": {
        "configure": {
            "tabmargins": [0, 0, 0, 0],
            "background": "#4d4d4d",
            "foreground": "white",
            "padding": [10, 5],
        },
        "map": {
            "background": [("selected", "#800000"), ("!selected", "#4d4d4d")],
            "foreground": [("selected", "white"), ("!selected", "white")],
        }
    }
})

# mengatur tema baru untuk ttk.Notebook
style.theme_use("my_theme")


def string_to_ascii():
    string = string_entry.get()
    ascii_result.config(text="ASCII: " + " ".join(str(ord(c)) for c in string))

def convert(base_from, base_to):
    value = int(value_entry.get(), int(base_from))
    result.config(text=str(base_to.upper()) + ": " + str(format(value, base_to)))

def reset1():
    string_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)
    ascii_result.config(text="")
    result.config(text="")

def reset2():
    string_entry.delete(0, tk.END)
    value_entry.delete(0, tk.END)
    ascii_result.config(text="")
    result.config(text="")

def convert_all():
    value = int(value_entry.get(), int(from_base))
    binary = bin(value)[2:]
    octal = oct(value)[2:]
    decimal = str(value)
    hexadecimal = hex(value)[2:]
    binary_result.config(text="Binary: " + binary)
    octal_result.config(text="Octal: " + octal)
    decimal_result.config(text="Decimal: " + decimal)
    hexadecimal_result.config(text="Hexadecimal: " + hexadecimal)




# String to ASCII conversion
string_label=tk.Label(frame_ASCII,text='Enter String:',font='arial 20 bold')
string_label.place(x=300,y=100)
# string_entry = tk.Entry(frame_ASCII)
# string_entry.pack()
string_entry=tk.Entry(frame_ASCII,font=('times new rommon',20,'bold'),width=22,bd=5)
string_entry.place(x=650,y=100)
# ascii_button = tk.Button(frame_ASCII, text="Convert to ASCII", command=string_to_ascii)
# ascii_button.pack()
ascii_button=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=string_to_ascii)
ascii_button.place(x=300,y=600)
# ascii_result = tk.Label(frame_ASCII, text="")
# ascii_result.pack()
ascii_result=tk.Label(frame_ASCII,font=('times new rommon',20,'bold'),relief=SUNKEN)
ascii_result.place(x=650,y=180)


# Number conversion
number_label = tk.Label(frame_Number, text="Enter number:")
number_label.pack()
value_entry = tk.Entry(frame_Number)
value_entry.pack()

# From base button
from_base = None
from_label = tk.Label(frame_Number, text="From base:")
from_label.pack()
from_button_frame = tk.Frame(frame_Number)
from_button_frame.pack()
def set_from_base(base):
    global from_base
    from_base = base
    from_button.config(text=f"From base: {from_base}")
for base in ['2', '8', '10', '16','' ]:
    from_button = tk.Button(from_button_frame, text=base, command=lambda base=base: set_from_base(base))
    from_button.pack(side=tk.LEFT)

# To base button
to_base = None
to_label = tk.Label(frame_Number, text="To base:")
to_label.pack()
to_button_frame = tk.Frame(frame_Number)
to_button_frame.pack()
def set_to_base(base):
    global to_base
    to_base = base
    to_button.config(text=f"To base: {to_base}")
for base in ['2', '8', '10', '16','' ]:
    from_base_var = tk.StringVar(value="Pick...")
    from_base_dropdown = tk.OptionMenu(frame_Number, set_to_base, "2", "8", "10", "16")
    to_button = tk.Button(to_button_frame, text=base, command=lambda base=base: set_to_base(base))
    to_button.pack(side=tk.LEFT)

convert_button = tk.Button(frame_Number, text="Convert", command=lambda: convert(from_base, to_base))
convert_button.pack()
result = tk.Label(frame_Number, text="")
result.pack()

# Conversion between all bases
convert_all_button = tk.Button(frame_Number, text="Convert All", command=convert_all)
convert_all_button.pack()
binary_result = tk.Label(frame_Number, text="")
binary_result.pack()
octal_result = tk.Label(frame_Number, text="")
octal_result.pack()
decimal_result = tk.Label(frame_Number, text="")
decimal_result.pack()
hexadecimal_result = tk.Label(frame_Number, text="")
hexadecimal_result.pack()

# Reset button
# reset_button = tk.Button(frame_Number, text="Reset", command=reset1)
reset_button=tk.Button(text='Reset',font='arial 20 bold',fg='white',bg='red',width=40,relief=GROOVE,bd=10,command=reset1)
reset_button.place(x=300,y=500)
reset_button = tk.Button(frame_ASCII, text="Reset", command=reset2)
reset_button.pack()

root.mainloop()
