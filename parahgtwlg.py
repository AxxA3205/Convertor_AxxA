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


#create frames
frame_string = Frame(notebook, width=1280, height=720)

frame_decimal = Frame(notebook, width=1280, height=720)

frame_biner = Frame(notebook, width=1280, height=720)

frame_Hexa = Frame(notebook, width=1280, height=720)

frame_Octal = Frame(notebook, width=1280, height=720)

# #add frames to notebook
notebook.add(frame_string, text='String Converter')
notebook.add(frame_decimal, text='Decimal Converter')
notebook.add(frame_biner, text='Binary Converter')
notebook.add(frame_Hexa, text='Hexadecimal Converter')
notebook.add(frame_Octal, text='Octal Converter')

notebook.pack(expand=True, fill='both')

#=======================================================STRING CONVERTER=============================================================

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

def converts():
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


tk.Label(frame_string,text='String Converter',font=('times new rommon',40,'bold'),bg='Black',fg='crimson', relief=RIDGE).pack(pady=10)
# Create the input label and text box
input_label=tk.Label(frame_string,text='Enter String:',font='arial 20 bold')
input_label.place(x=300,y=100)
input_box=tk.Entry(frame_string,font=('times new rommon',20,'bold'),width=22,bd=5)
input_box.place(x=650,y=100)

# Create the convert button
convert_button=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=converts)
convert_button.place(x=300,y=600)

# Create the binary output label
binary_label=tk.Label(frame_string,text='Binary: ',font='arial 20 bold')
binary_label.place(x=300,y=180)
binary_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
binary_output.place(x=650,y=180)

# Create the decimal output label
decimal_label=tk.Label(frame_string,text='Decimal: ',font='arial 20 bold')
decimal_label.place(x=300,y=260)
decimal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_output.place(x=650,y=260)

# Create the hexadecimal output label
hexadecimal_label=tk.Label(frame_string,text='Hexadecimal: ',font='arial 20 bold')
hexadecimal_label.place(x=300,y=340)
hexadecimal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
hexadecimal_output.place(x=650,y=340)

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

#=======================================================DECIMAL CONVERTER=============================================================

def convertd():
    decimal = int(dec_entry.get())

    # Convert to hexadecimal
    hex_value = hex(decimal)
    hex_label.config(text=hex_value)

    # Convert to binary
    bin_value = bin(decimal)
    bin_label.config(text=bin_value)

    # Convert to octal
    oct_value = oct(decimal)
    oct_label.config(text=oct_value)

tk.Label(frame_decimal,text='Decimal Converter',font=('times new rommon',40,'bold'),bg='Black',fg='crimson', relief=RIDGE).pack(pady=10)
# Create the input label and text box
dec_label=tk.Label(frame_decimal,text='Enter decimal:',font='arial 20 bold')
dec_label.place(x=300,y=100)
dec_entry=tk.Entry(frame_decimal,font=('times new rommon',20,'bold'),width=22,bd=5)
dec_entry.place(x=650,y=100)


# Create the convert button
convert_button2=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=convertd)
convert_button2.place(x=300,y=600)


# Create the binary output label
bin_label=tk.Label(frame_decimal,text='Binary: ',font='arial 20 bold')
bin_label.place(x=300,y=180)
bin_label=tk.Label(frame_decimal,font=('times new rommon',20,'bold'),relief=SUNKEN)
bin_label.place(x=650,y=180)



# Create the hexadecimal output label
hex_label=tk.Label(frame_decimal,text='Hexadecimal: ',font='arial 20 bold')
hex_label.place(x=300,y=260)
hex_label=tk.Label(frame_decimal,font=('times new rommon',20,'bold'),relief=SUNKEN)
hex_label.place(x=650,y=260)

# Create the octal output label
oct_label=tk.Label(frame_decimal,text='Octal: ',font='arial 20 bold')
oct_label.place(x=300,y=340)
oct_label=tk.Label(frame_decimal,font=('times new rommon',20,'bold'),relief=SUNKEN)
oct_label.place(x=650,y=340)

#=======================================================BINER CONVERTER=============================================================

def convertb():
    binary = binary_entry.get()

    # Convert to decimal
    decimal_value3 = int(binary, 2)
    decimal_label3.config(text=decimal_value3)

    # Convert to hexadecimal
    hex_value3 = hex(decimal_value3)
    hex_label3.config(text=hex_value3)

    # Convert to octal
    oct_value3 = oct(decimal_value3)
    oct_label3.config(text=oct_value3)

tk.Label(frame_biner,text='Binary Converter',font=('times new rommon',40,'bold'),bg='Black',fg='crimson', relief=RIDGE).pack(pady=10)

binary_label3=tk.Label(frame_biner,text='Enter Binary:',font='arial 20 bold')
binary_label3.place(x=300,y=100)
binary_entry=tk.Entry(frame_biner,font=('times new rommon',20,'bold'),width=22,bd=5)
binary_entry.place(x=650,y=100)

# Create the convert button
convert_button3=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=convertb)
convert_button3.place(x=300,y=600)

# Create the binary output label
decimal_label3=tk.Label(frame_biner,text='Decimal: ',font='arial 20 bold')
decimal_label3.place(x=300,y=180)
decimal_label3=tk.Label(frame_biner,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_label3.place(x=650,y=180)



# Create the hexadecimal output label
hex_label3=tk.Label(frame_biner,text='Hexadecimal: ',font='arial 20 bold')
hex_label3.place(x=300,y=260)
hex_label3=tk.Label(frame_biner,font=('times new rommon',20,'bold'),relief=SUNKEN)
hex_label3.place(x=650,y=260)

# Create the octal output label
oct_label3=tk.Label(frame_biner,text='Octal: ',font='arial 20 bold')
oct_label3.place(x=300,y=340)
oct_label3=tk.Label(frame_biner,font=('times new rommon',20,'bold'),relief=SUNKEN)
oct_label3.place(x=650,y=340)

#=======================================================HEXA CONVERTER=============================================================

def converth():
    hexadecimal = hexadecimal_entry.get()

    # Convert to decimal
    decimal_value4 = int(hexadecimal, 16)
    decimal_label4.config(text=decimal_value4)

    # Convert to binary
    bin_value4 = bin(decimal_value4)
    bin_label4.config(text=bin_value4)

    # Convert to octal
    oct_value4 = oct(decimal_value4)
    oct_label4.config(text=oct_value4)

tk.Label(frame_Hexa,text='Hexadecimal Converter',font=('times new rommon',40,'bold'),bg='Black',fg='crimson', relief=RIDGE).pack(pady=10)

hex_label4=tk.Label(frame_Hexa,text='Enter Hexadecimal:',font='arial 20 bold')
hex_label4.place(x=300,y=100)
hexadecimal_entry=tk.Entry(frame_Hexa,font=('times new rommon',20,'bold'),width=22,bd=5)
hexadecimal_entry.place(x=650,y=100)

# Create the convert button
convert_button4=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=converth)
convert_button4.place(x=300,y=600)

# Create the binary output label
decimal_label4=tk.Label(frame_Hexa,text='Decimal: ',font='arial 20 bold')
decimal_label4.place(x=300,y=180)
decimal_label4=tk.Label(frame_Hexa,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_label4.place(x=650,y=180)



# Create the hexadecimal output label
bin_label4=tk.Label(frame_Hexa,text='Hexadecimal: ',font='arial 20 bold')
bin_label4.place(x=300,y=260)
bin_label4=tk.Label(frame_Hexa,font=('times new rommon',20,'bold'),relief=SUNKEN)
bin_label4.place(x=650,y=260)

# Create the octal output label
oct_label4=tk.Label(frame_Hexa,text='Octal: ',font='arial 20 bold')
oct_label4.place(x=300,y=340)
oct_label4=tk.Label(frame_Hexa,font=('times new rommon',20,'bold'),relief=SUNKEN)
oct_label4.place(x=650,y=340)

#=======================================================OCTAL CONVERTER=============================================================

def converto():
    octal = octal_entry.get()

    # Convert to decimal
    decimal_value5 = int(octal, 8)
    decimal_label5.config(text=decimal_value5)

    # Convert to binary
    bin_value5 = bin(decimal_value5)
    bin_label5.config(text=bin_value5)

    # Convert to hexadecimal
    hex_value5 = hex(decimal_value5)
    hex_label5.config(text=hex_value5)


tk.Label(frame_Octal,text='Octal Converter',font=('times new rommon',40,'bold'),bg='Black',fg='crimson', relief=RIDGE).pack(pady=10)

oct_label5=tk.Label(frame_Octal,text='Enter Octal:',font='arial 20 bold')
oct_label5.place(x=300,y=100)
octal_entry=tk.Entry(frame_Octal,font=('times new rommon',20,'bold'),width=22,bd=5)
octal_entry.place(x=650,y=100)

# Create the convert button
convert_button4=tk.Button(text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=converto)
convert_button4.place(x=300,y=600)

# Create the binary output label
decimal_label5=tk.Label(frame_Octal,text='Decimal: ',font='arial 20 bold')
decimal_label5.place(x=300,y=180)
decimal_label5=tk.Label(frame_Octal,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_label5.place(x=650,y=180)



# Create the hexadecimal output label
bin_label5=tk.Label(frame_Octal,text='Binary: ',font='arial 20 bold')
bin_label5.place(x=300,y=260)
bin_label5=tk.Label(frame_Octal,font=('times new rommon',20,'bold'),relief=SUNKEN)
bin_label5.place(x=650,y=260)

# Create the octal output label
hex_label5=tk.Label(frame_Octal,text='Hexadecimal: ',font='arial 20 bold')
hex_label5.place(x=300,y=340)
hex_label5=tk.Label(frame_Octal,font=('times new rommon',20,'bold'),relief=SUNKEN)
hex_label5.place(x=650,y=340)

root.mainloop()