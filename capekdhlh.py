import tkinter as tk
from tkinter import *
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title('Convertor Application AxxA')
root.geometry('1280x720')

#Create notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10,expand=True)


#create frames
frame_string = Frame(notebook, width=1280, height=720, bg='#4d4d4d')

frame_decimal = Frame(notebook, width=1280, height=720, bg='#4d4d4d')

frame_biner = Frame(notebook, width=1280, height=720, bg='#4d4d4d')

frame_Hexa = Frame(notebook, width=1280, height=720 , bg='#4d4d4d')

frame_Octal = Frame(notebook, width=1280, height=720 , bg='#4d4d4d')

# #add frames to notebook
notebook.add(frame_string, text='String Converter')
notebook.add(frame_biner, text='Binary Converter')
notebook.add(frame_Octal, text='Octal Converter')
notebook.add(frame_decimal, text='Decimal Converter')
notebook.add(frame_Hexa, text='Hexadecimal Converter')

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

style.theme_use("my_theme")

#=======================================================RESET CONVERTER=============================================================
def reset1():
    #String
    input_box.delete(0, tk.END)
    ascii_output.config(text="")
    binary_output.config(text="")
    octal_output.config(text="")
    decimal_output.config(text="")
    hexadecimal_output.config(text="")
    #Decimal
    dec_entry.delete(0, tk.END)
    bin_label2.config(text="")
    oct_label2.config(text="")
    hex_label2.config(text="")
    #Binary
    binary_entry.delete(0, tk.END)
    oct_label3.config(text="")
    decimal_label3.config(text="")
    hex_label3.config(text="")
    #Octal
    octal_entry.delete(0, tk.END)
    bin_label5.config(text="")
    decimal_label5.config(text="")
    hex_label5.config(text="")
    #Hexadecimal
    hexadecimal_entry.delete(0, tk.END)
    bin_label4.config(text="")
    oct_label4.config(text="")
    decimal_label4.config(text="")

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
    ascii_output.config(text=" ".join(map(str, decimal_list)))
    binary_output.config(text=" ".join(binary_list))
    octal_output.config(text=" ".join(octal_list))
    decimal_output.config(text=" ".join(map(str, decimal_list)))
    hexadecimal_output.config(text=" ".join(hexadecimal_list))





tk.Label(frame_string,text='String Converter',font=('times new rommon',40,'bold'),bg='black',fg='#800000',border=0, width=1280,relief=RIDGE).pack(pady=0)

# Create the input label and text box
input_label=tk.Label(frame_string,text='Enter String:',font='arial 20 bold', border=0, bg='#4d4d4d')
input_label.place(x=300,y=100)
input_box=tk.Entry(frame_string,font=('times new rommon',20,'bold'),width=22,bd=5)
input_box.place(x=650,y=100)

# Create the convert button
convert_button=tk.Button(frame_string, text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=converts)
convert_button.place(x=300,y=550)

# create the ASCII output label
ascii_label=tk.Label(frame_string,text='ASCII: ',font='arial 20 bold', border=0, bg='#4d4d4d')
ascii_label.place(x=300,y=180)
ascii_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
ascii_output.place(x=650,y=180)

# Create the binary output label
binary_label=tk.Label(frame_string,text='Binary: ',font='arial 20 bold', border=0, bg='#4d4d4d')
binary_label.place(x=300,y=260)
binary_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
binary_output.place(x=650,y=260)

# Create the octal output label
octal_label=tk.Label(frame_string,text='Octal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
octal_label.place(x=300,y=340)
octal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
octal_output.place(x=650,y=340)

# Create the decimal output label
decimal_label=tk.Label(frame_string,text='Decimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
decimal_label.place(x=300,y=420)
decimal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_output.place(x=650,y=420)

# Create the hexadecimal output label
hexadecimal_label=tk.Label(frame_string,text='Hexadecimal: ',font='arial 20 bold',border=0, bg='#4d4d4d')
hexadecimal_label.place(x=300,y=500)
hexadecimal_output=tk.Label(frame_string,font=('times new rommon',20,'bold'),relief=SUNKEN)
hexadecimal_output.place(x=650,y=500)

# Create the reset button
reset_button=tk.Button(frame_string, text='Del',font='arial 15 bold',fg='white',bg='red',width=5, height=0,relief=GROOVE,bd=4,command=reset1)
reset_button.place(x=1010,y=100)

#=======================================================DECIMAL CONVERTER=============================================================

def convertd():

    dec_value2 = int(dec_entry.get())

    # Convert to binary using a loop
    bin_value2 = ""
    quotient2 = dec_value2
    while quotient2 > 0:
        bin_value2 = str(quotient2 % 2) + bin_value2
        quotient2 = quotient2 // 2
    bin_label2.config(text=bin_value2)

    # Convert to hexadecimal using a loop
    hex_value2 = ""
    quotient2 = dec_value2
    while quotient2 > 0:
        remainder2 = quotient2 % 16
        if remainder2 < 10:
            hex_value2 = str(remainder2) + hex_value2
        else:
            hex_value2 = chr(remainder2 + 55) + hex_value2
        quotient2 = quotient2 // 16
    hex_label2.config(text=hex_value2)

    # Convert to octal using a loop
    octal_value2 = ""
    quotient2 = dec_value2
    while quotient2 > 0:
        octal_value2 = str(quotient2 % 8) + octal_value2
        quotient2 = quotient2 // 8
    oct_label2.config(text=octal_value2)

tk.Label(frame_decimal,text='Decimal Converter',font=('times new rommon',40,'bold'),bg='black',fg='#800000',border=0, width=1280,relief=RIDGE).pack(pady=0)

# Create the input label and text box
dec_label2=tk.Label(frame_decimal,text='Enter Decimal:',font='arial 20 bold', border=0, bg='#4d4d4d')
dec_label2.place(x=300,y=100)
dec_entry=tk.Entry(frame_decimal,font=('times new rommon',20,'bold'),width=22,bd=5)
dec_entry.place(x=650,y=100)


# Create the convert button
convert_button2=tk.Button(frame_decimal, text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=convertd)
convert_button2.place(x=300,y=550)


# Create the binary output label
bin_label2=tk.Label(frame_decimal,text='Binary: ',font='arial 20 bold', border=0, bg='#4d4d4d')
bin_label2.place(x=300,y=180)
bin_label2=tk.Label(frame_decimal,font=('times new rommon',20,'bold'),relief=SUNKEN)
bin_label2.place(x=650,y=180)



# Create the hexadecimal output label
hex_label2=tk.Label(frame_decimal,text='Hexadecimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
hex_label2.place(x=300,y=340)
hex_label2=tk.Label(frame_decimal,font=('times new rommon',20,'bold'),relief=SUNKEN)
hex_label2.place(x=650,y=340)

# Create the octal output label
oct_label2=tk.Label(frame_decimal,text='Octal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
oct_label2.place(x=300,y=260)
oct_label2=tk.Label(frame_decimal,font=('times new rommon',20,'bold'),relief=SUNKEN)
oct_label2.place(x=650,y=260)

reset_button=tk.Button(frame_decimal ,text='Del',font='arial 15 bold',fg='white',bg='red',width=5, height=0,relief=GROOVE,bd=4,command=reset1)
reset_button.place(x=1010,y=100)

#=======================================================BINER CONVERTER=============================================================

def convertb():
    
    bin_value3 = binary_entry.get()

    # Convert to decimal using a loop
    decimal_value3 = 0
    power3 = 0
    for digit3 in bin_value3[::-1]:
        decimal_value3 += int(digit3) * (2 ** power3)
        power3 += 1
    decimal_label3.config(text=decimal_value3)

    # Convert to hexadecimal using a loop
    hex_value3 = ""
    while decimal_value3 > 0:
        remainder3 = decimal_value3 % 16
        if remainder3 < 10:
            hex_value3 = str(remainder3) + hex_value3
        else:
            hex_value3 = chr(remainder3 + 55) + hex_value3
        decimal_value3 = decimal_value3 // 16
    hex_label3.config(text=hex_value3)

    # Convert to octal using a loop
    octal_value3 = ""
    while len(bin_value3) % 3 != 0:
        bin_value3 = "0" + bin_value3
    for i in range(0, len(bin_value3), 3):
        octal_value3 += str(int(bin_value3[i:i+3], 2))
    oct_label3.config(text=octal_value3)

tk.Label(frame_biner,text='Binary Converter',font=('times new rommon',40,'bold'),bg='black',fg='#800000',border=0, width=1280,relief=RIDGE).pack(pady=0)

binary_label3=tk.Label(frame_biner,text='Enter Binary:',font='arial 20 bold', border=0, bg='#4d4d4d')
binary_label3.place(x=300,y=100)
binary_entry=tk.Entry(frame_biner,font=('times new rommon',20,'bold'),width=22,bd=5)
binary_entry.place(x=650,y=100)

# Create the convert button
convert_button3=tk.Button(frame_biner ,text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=convertb)
convert_button3.place(x=300,y=550)

# Create the binary output label
decimal_label3=tk.Label(frame_biner,text='Decimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
decimal_label3.place(x=300,y=260)
decimal_label3=tk.Label(frame_biner,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_label3.place(x=650,y=260)

# Create the hexadecimal output label
hex_label3=tk.Label(frame_biner,text='Hexadecimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
hex_label3.place(x=300,y=340)
hex_label3=tk.Label(frame_biner,font=('times new rommon',20,'bold'),relief=SUNKEN)
hex_label3.place(x=650,y=340)

# Create the octal output label
oct_label3=tk.Label(frame_biner,text='Octal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
oct_label3.place(x=300,y=180)
oct_label3=tk.Label(frame_biner,font=('times new rommon',20,'bold'),relief=SUNKEN)
oct_label3.place(x=650,y=180)

reset_button=tk.Button(frame_biner, text='Del',font='arial 15 bold',fg='white',bg='red',width=5, height=0,relief=GROOVE,bd=4,command=reset1)
reset_button.place(x=1010,y=100)

#=======================================================HEXA CONVERTER=============================================================

def converth():

    hex_value4 = hexadecimal_entry.get()

    # Convert to decimal using a loop
    decimal_value4 = 0
    power4 = 0
    for digit4 in hex_value4[::-1]:
        if digit4.isdigit():
            decimal_value4 += int(digit4) * (16 ** power4)
        else:
            decimal_value4 += (ord(digit4.lower()) - 87) * (16 ** power4)
        power4 += 1
    decimal_label4.config(text=decimal_value4)

    # Convert to binary using a built-in function
    bin_value4 = format(decimal_value4, 'b')
    bin_label4.config(text=bin_value4)

    # Convert to octal using a loop
    octal_value4 = ""
    while decimal_value4 > 0:
        remainder4 = decimal_value4 % 8
        octal_value4 = str(remainder4) + octal_value4
        decimal_value4 = decimal_value4 // 8
    oct_label4.config(text=octal_value4)


tk.Label(frame_Hexa,text='Hexadecimal Converter',font=('times new rommon',40,'bold'),bg='black',fg='#800000',border=0, width=1280,relief=RIDGE).pack(pady=0)

hex_label4=tk.Label(frame_Hexa,text='Enter Hexadecimal:',font='arial 20 bold', border=0, bg='#4d4d4d')
hex_label4.place(x=300,y=100)
hexadecimal_entry=tk.Entry(frame_Hexa,font=('times new rommon',20,'bold'),width=22,bd=5)
hexadecimal_entry.place(x=650,y=100)

# Create the convert button
convert_button4=tk.Button(frame_Hexa,text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=converth)
convert_button4.place(x=300,y=550)

# Create the binary output label
decimal_label4=tk.Label(frame_Hexa,text='Decimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
decimal_label4.place(x=300,y=340)
decimal_label4=tk.Label(frame_Hexa,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_label4.place(x=650,y=340)

# Create the Binary output label
bin_label4=tk.Label(frame_Hexa,text='Binary: ',font='arial 20 bold', border=0, bg='#4d4d4d')
bin_label4.place(x=300,y=180)
bin_label4=tk.Label(frame_Hexa,font=('times new rommon',20,'bold'),relief=SUNKEN)
bin_label4.place(x=650,y=180)

# Create the octal output label
oct_label4=tk.Label(frame_Hexa,text='Octal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
oct_label4.place(x=300,y=260)
oct_label4=tk.Label(frame_Hexa,font=('times new rommon',20,'bold'),relief=SUNKEN)
oct_label4.place(x=650,y=260)

reset_button=tk.Button(frame_Hexa,text='Del',font='arial 15 bold',fg='white',bg='red',width=5, height=0,relief=GROOVE,bd=4,command=reset1)
reset_button.place(x=1010,y=100)

#=======================================================OCTAL CONVERTER=============================================================

def converto():

    octal_value = octal_entry.get()

    # Convert to decimal using a loop
    decimal_value5 = 0
    power5 = 0
    for digit5 in octal_value[::-1]:
        decimal_value5 += int(digit5) * (8 ** power5)
        power5 += 1
    decimal_label5.config(text=decimal_value5)

    # Convert to binary using a built-in function
    bin_value5 = format(decimal_value5, 'b')
    bin_label5.config(text=bin_value5)

    # Convert to hexadecimal using a built-in function
    hex_value5 = format(decimal_value5, 'x')
    hex_label5.config(text=hex_value5)

tk.Label(frame_Octal,text='Octal Converter',font=('times new rommon',40,'bold'),bg='black',fg='#800000',border=0, width=1280,relief=RIDGE).pack(pady=0)

oct_label5=tk.Label(frame_Octal,text='Enter Octal:',font='arial 20 bold', border=0, bg='#4d4d4d')
oct_label5.place(x=300,y=100)
octal_entry=tk.Entry(frame_Octal,font=('times new rommon',20,'bold'),width=22,bd=5)
octal_entry.place(x=650,y=100)

# Create the convert button
convert_button5=tk.Button(frame_Octal ,text='Converter',font='arial 20 bold',fg='white',bg='green',width=40,relief=GROOVE,bd=10,command=converto)
convert_button5.place(x=300,y=550)

# Create the binary output label
decimal_label5=tk.Label(frame_Octal,text='Decimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
decimal_label5.place(x=300,y=260)
decimal_label5=tk.Label(frame_Octal,font=('times new rommon',20,'bold'),relief=SUNKEN)
decimal_label5.place(x=650,y=260)

# Create the hexadecimal output label
bin_label5=tk.Label(frame_Octal,text='Binary: ',font='arial 20 bold', border=0, bg='#4d4d4d')
bin_label5.place(x=300,y=180)
bin_label5=tk.Label(frame_Octal,font=('times new rommon',20,'bold'),relief=SUNKEN)
bin_label5.place(x=650,y=180)

# Create the octal output label
hex_label5=tk.Label(frame_Octal,text='Hexadecimal: ',font='arial 20 bold', border=0, bg='#4d4d4d')
hex_label5.place(x=300,y=340)
hex_label5=tk.Label(frame_Octal,font=('times new rommon',20,'bold'),relief=SUNKEN)
hex_label5.place(x=650,y=340)

reset_button=tk.Button(frame_Octal, text='Del',font='arial 15 bold',fg='white',bg='red',width=5, height=0,relief=GROOVE,bd=4,command=reset1)
reset_button.place(x=1010,y=100)

root.mainloop()