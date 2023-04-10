import PySimpleGUI as sg

# Fungsi untuk mengonversi string menjadi bilangan desimal
def string_to_decimal(string):
    decimal = ""
    for char in string:
        decimal += str(ord(char))
    return decimal

# Fungsi untuk mengonversi string menjadi bilangan biner
def string_to_binary(string):
    binary = ""
    for char in string:
        binary += format(ord(char), '08b')
    return binary

# Fungsi untuk mengonversi string menjadi bilangan oktal
def string_to_octal(string):
    octal = ""
    for char in string:
        octal += format(ord(char), '03o')
    return octal

# Fungsi untuk mengonversi string menjadi bilangan heksadesimal
def string_to_hexadecimal(string):
    hexadecimal = ""
    for char in string:
        hexadecimal += format(ord(char), '02X')
    return hexadecimal

# Layout UI
layout = [
    [sg.Text('Konversi String', font=('Helvetica', 20))],
    [sg.Text('Masukkan string yang ingin dikonversi:')],
    [sg.InputText(key='string')],
    [sg.Button('Konversi'), sg.Button('Keluar')],
    [sg.Radio('Desimal', 'conversion', key='decimal'), 
     sg.Radio('Biner', 'conversion', key='binary'), 
     sg.Radio('Oktal', 'conversion', key='octal'), 
     sg.Radio('Hexadesimal', 'conversion', key='hexadecimal'), 
     sg.Radio('ASCII', 'conversion', key='ascii')],
    [sg.Text('Hasil:', font=('Helvetica', 12)), sg.Text('', font=('Helvetica', 12), key='output')]
]

# Membuat window
window = sg.Window('Konversi String', layout)

# Loop untuk menangani event dari user
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break
    if event == 'Konversi':
        string = values['string']
        if values['decimal']:
            hasil = string_to_decimal(string)
        elif values['binary']:
            hasil = string_to_binary(string)
        elif values['octal']:
            hasil = string_to_octal(string)
        elif values['hexadecimal']:
            hasil = string_to_hexadecimal(string)
        elif values['ascii']:
            hasil = ' '.join(str(ord(char)) for char in string)
        window['output'].update(hasil)

window.close()