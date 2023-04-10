from art import *
from prettytable import PrettyTable

class Converter:
    def main(self):
        tprint("CONVERTER", font='tarty1',chr_ignore=True)
        while True:
            print("="*32)
            print("Pilih input :")
            print("1. String")
            print("2. Binary")
            print("3. Octal")
            print("4. Decimal")
            print("5. Hexadecimal")
            print("0. Exit")
            print("="*32)

            pilihan = input("Masukan pilihanmu : ")

            # Create a dictionary of lambda functions
            options = {
                '1': lambda: self.convert_string(),
                '2': lambda: self.convert_binary(),
                '3': lambda: self.convert_octal(),
                '4': lambda: self.convert_decimal(),
                '5': lambda: self.convert_hexadecimal(),
                '0': lambda: self.app_exit()
            }

            # Call the lambda function based on user input
            options.get(pilihan, lambda: print("Pilihan tidak valid"))()

    def convert_string(self):
        print("="*32)
        text = input("Masukan string: ")
        formats = [
            ('ASCII', lambda c: str(c)),
            ('Binary', lambda c: format(ord(c), '08b')),
            ('Octal', lambda c: format(ord(c), '03o')),
            ('Decimal', lambda c: str(ord(c))),
            ('Hexadecimal', lambda c: format(ord(c), '02X'))
        ]
        table = PrettyTable(['Format', 'Value'])
        [table.add_row([name, ' '.join(convert(c) for c in text)]) for name, convert in formats]
        print("="*32)
        print(table)
        
    def convert_binary(self):
        print("="*32)
        binary = input("Masukan binary: ")
        try:
            text = ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
            formats = [
                ('ASCII', lambda c: str(c)),
                ('Binary', lambda c: format(ord(c), '08b')),
                ('Octal', lambda c: format(ord(c), '03o')),
                ('Decimal', lambda c: str(ord(c))),
                ('Hexadecimal', lambda c: format(ord(c), '02X'))
            ]
            table = PrettyTable(['Format', 'Value'])
            [table.add_row([name, ' '.join(convert(c) for c in text)]) for name, convert in formats]
            print(table)
            print("="*32)
        except ValueError:
            print("="*32)
            print("Input tidak valid!")
            print("="*32)

    def convert_octal(self):
        print("="*32)
        octal = input("Masukan octal: ")
        text = ''.join(chr(int(octal[i:i+3], 8)) for i in range(0, len(octal), 3))
        formats = [
            ('ASCII', lambda c: c),
            ('Binary', lambda c: format(ord(c), '08b')),
            ('Octal', lambda c: format(ord(c), '03o')),
            ('Decimal', lambda c: str(ord(c))),
            ('Hexadecimal', lambda c: format(ord(c), '02X'))
        ]
        table = PrettyTable(['Format', 'Value'])
        [table.add_row([name, ' '.join(convert(c) for c in text)]) for name, convert in formats]
        print(table)
        print("="*32)
    def convert_decimal(self):
        decimal = input("Masukan decimal: ")
        decimals = decimal.split()
        text = ''.join(chr(int(d)) for d in decimals)
        formats = [
            ('ASCII', lambda c: c),
            ('Binary', lambda c: format(ord(c), '08b')),
            ('Octal', lambda c: format(ord(c), '03o')),
            ('Decimal', lambda c: str(ord(c))),
            ('Hexadecimal', lambda c: format(ord(c), '02X'))
        ]
        table = PrettyTable(['Format', 'Value'])
        [table.add_row([name, ' '.join(convert(c) for c in text)]) for name, convert in formats]
        print(table)

    def convert_hexadecimal(self):
        hexadecimal = input("Masukan hexadecimal: ")
        text = bytearray.fromhex(hexadecimal).decode()
        formats = [
            ('ASCII', lambda c: c),
            ('Binary', lambda c: format(ord(c), '08b')),
            ('Octal', lambda c: format(ord(c), '03o')),
            ('Decimal', lambda c: str(ord(c))),
            ('Hexadecimal', lambda c: format(ord(c), '02X'))
        ]
        table = PrettyTable(['Format', 'Value'])
        [table.add_row([name, ' '.join(convert(c) for c in text)]) for name, convert in formats]
        print(table)

    def app_exit(self):
        tprint("TERIMA KASIH", font='tarty1',chr_ignore=True)
        exit()


converter = Converter()
converter.main()