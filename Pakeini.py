import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title('Number convertor')
root.geometry('1280x720')

#Create notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10,expand=True)
# #create frames
frame_string = Frame(notebook, width=1280, height=720)

frame_decimal = Frame(notebook, width=1280, height=720)
# #add frames to notebook
notebook.add(frame_string, text='String Converter')
notebook.add(frame_decimal, text='Decimal Converter')

notebook.pack(expand=True, fill='both')

def string_to_ascii(input_str):
    """
    This function takes a string as input and returns the ASCII code for each character in the string
    """
    return [ord(c) for c in input_str]

def ascii_to_binary(ascii_list):
    """
    This function takes a list of ASCII codes as input and returns a list of binary strings for each ASCII code
    """
    return [bin(c)[2:].zfill(8) for c in ascii_list]

def ascii_to_decimal(ascii_list):
    """
    This function takes a list of ASCII codes as input and returns a list of decimal values for each ASCII code
    """
    return [c for c in ascii_list]

def ascii_to_hexadecimal(ascii_list):
    """
    This function takes a list of ASCII codes as input and returns a list of hexadecimal values for each ASCII code
    """
    return [hex(c)[2:].zfill(2) for c in ascii_list]

def ascii_to_octal(ascii_list):
    """
    This function takes a list of ASCII codes as input and returns a list of octal values for each ASCII code
    """
    return [oct(c)[2:].zfill(3) for c in ascii_list]

def convert():
    # Get the input string
    input_str = input_box.get()

    # Convert the input string to ASCII
    ascii_list = string_to_ascii(input_str)

    # Convert ASCII to binary
    binary_list = ascii_to_binary(ascii_list)

    # Convert ASCII to decimal
    decimal_list = ascii_to_decimal(ascii_list)

    # Convert ASCII to hexadecimal
    hexadecimal_list = ascii_to_hexadecimal(ascii_list)

    # Convert ASCII to octal
    octal_list = ascii_to_octal(ascii_list)

    # Update the output labels
    binary_output.config(text=" ".join(binary_list))
    decimal_output.config(text=" ".join(map(str, decimal_list)))
    hexadecimal_output.config(text=" ".join(hexadecimal_list))
    octal_output.config(text=" ".join(octal_list))
    ascii_output.config(text=" ".join(map(str, decimal_list)))

#=======================================================STRING CONVERTER=============================================================

tk.Label(frame_string,text='String Converter',font=('times new rommon',40,'bold'),bg='Black',fg='crimson', relief=RIDGE).pack(pady=10)
# Create the input label and text box
input_label=tk.Label(frame_string,text='Enter String:',font='arial 20 bold')
input_label.place(x=300,y=100)
input_box=tk.Entry(frame_string,font=('times new rommon',20,'bold'),width=22,bd=5)
input_box.place(x=650,y=100)

# input_label = tk.Label(root, text="Enter a string:")
# input_label.pack()
# input_box = tk.Entry(root)
# input_box.pack()

# Create the convert button
convert_button=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=convert)
convert_button.place(x=300,y=600)

# convert_button = tk.Button(root, text="Convert", command=convert)
# convert_button.pack()

# Create the binary output label
binary_label=tk.Label(frame_string,text='Binary: ',font='arial 20 bold')
binary_label.place(x=300,y=180)
binary_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
binary_output.place(x=650,y=180)

# binary_label = tk.Label(root, text="Binary:")
# binary_label.pack()
# binary_output = tk.Label(root, text="")
# binary_output.pack()

# Create the decimal output label
decimal_label=tk.Label(frame_string,text='Decimal: ',font='arial 20 bold')
decimal_label.place(x=300,y=260)
decimal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_output.place(x=650,y=260)

# decimal_label = tk.Label(root, text="Decimal:")
# decimal_label.pack()
# decimal_output = tk.Label(root, text="")
# decimal_output.pack()

# Create the hexadecimal output label
hexadecimal_label=tk.Label(frame_string,text='Hexadecimal: ',font='arial 20 bold')
hexadecimal_label.place(x=300,y=340)
hexadecimal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
hexadecimal_output.place(x=650,y=340)

# hexadecimal_label = tk.Label(root, text="Hexadecimal:")
# hexadecimal_label.pack()
# hexadecimal_output = tk.Label(root, text="")
# hexadecimal_output.pack()

# Create the octal output label
octal_label=tk.Label(frame_string,text='Octal: ',font='arial 20 bold')
octal_label.place(x=300,y=420)
octal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
octal_output.place(x=650,y=420)

# create the ASCII output label
ascii_label=tk.Label(frame_string,text='ASCII: ',font='arial 20 bold')
ascii_label.place(x=300,y=500)
ascii_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
ascii_output.place(x=650,y=500)

# octal_label = tk.Label(root, text="Octal:")
# octal_label.pack()
# octal_output = tk.Label(root, text="")
# octal_output.pack()

# def clear():
#     input_box.set('')
#     binary_output.set('')
#     decimal_output.set('')
#     hexadecimal_output.set('')
#     octal_output.set('')

# clear_button=tk.Button(root,text='Clear',font='arial 20 bold',fg='white',bg='red',width=10,relief=GROOVE,bd=10,command=clear)
# clear_button.place(x=760,y=550)

#=======================================================DECIMAL CONVERTER=============================================================

# Run the main loop
root.mainloop()