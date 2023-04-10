try:
    print('Konversi dari :')
    print('1. Desimal')
    print('2. Biner')
    print('3. Okta')
    print('4. Hexadecimal')
    print('5. ASCII')
    print('6. String')
    print('0. exit')

    masukan = int(input('masukan pilihan : '))
    print('')

    while masukan > 4 or masukan < 0:  # pengecek inputan pemilihan menu
        print('silahkan masukan angka yang ada pada menu.')
        masukan = int(input('masukan pilihan : '))
        print('')

    while masukan != 0:
        tampil = ''
        biner = 0
        hexa = 0
        pembalik = []
        cetak = []

        if masukan == 1:
            print('')
            print('konvert ke')
            print('1. Biner')
            print('2. Okta')
            print('3. Hexadecimal')
            print('4. ASCII')
            print('')
            menu = int(input('masukan pilihan : '))
            print('')
            while menu > 5 or menu < 0:
                print('silahkan masukan angka yang ada pada menu.')
                menu = int(input('masukan pilihan : '))
                print('')

            if menu == 1:
                desimal = int(input('masukan angka desimal:'))
                print('')
                while desimal != 0:
                    hasil = desimal % 2  # angka desimal di modulus 2 untuk memperoleh sisanya
                    # digunakan untuk membalik hasil modulus. kenapa dibalika ? coba search di google dgn key word "cara konversi desimal ke biner"
                    cetak.insert(0, str(hasil))
                    # bilangan desimal dibagi 2 dan tanpa menghasilkan angka koma dengan menggunakan '//' untuk mengubah nilainya. untuk keperluan modulus selanjutnya.
                    desimal = desimal//2
                    if desimal == 0:
                        # perulangan untuk menggabungkan angka angka hasil modulus yang sebelumnya ada di dalam list menjadi string
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

            elif menu == 2:
                desimal = int(input('masukan angka desimal :'))
                print('')
                while desimal != 0:
                    hasil = desimal % 8  # angka desimal di modulus 8 untuk memperoleh sisanya
                    # digunakan untuk membalik hasil modulus. kenapa dibalika ? coba search di google dgn key word "cara konversi desimal ke okta"
                    cetak.insert(0, str(hasil))
                    desimal = desimal//8  # bilangan desimal dibagi 8 dan tanpa menghasilkan angka koma dengan menggunakan '//' untuk mengubah nilainya. untuk keperluan modulus selanjutnya
                    if desimal == 0:
                        # perulangan untuk menggabungkan angka angka hasil modulus yang sebelumnya ada di dalam list menjadi string
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

            elif menu == 3:
                desimal = int(input('masukan angka desimal :'))
                print('')
                while desimal != 0:
                    hasil = desimal % 16  # angka desimal di modulus dengan 16 untuk memperoleh sisanya
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    # digunakan untuk membalik hasil modulus. kenapa dibalika ? coba search di google dgn key word "cara konversi desimal ke heksa"
                    cetak.insert(0, str(hasil))
                    desimal = desimal//16  # bilangan desimal dibagi 16 dan tanpa menghasilkan angka koma dengan menggunakan '//' untuk mengubah nilainya. untuk keperluan modulus selanjutnya
                    if desimal == 0:
                        # perulangan untuk menggabungkan angka angka hasil modulus yang sebelumnya ada di dalam list menjadi string
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

        elif masukan == 2:
            print('konvert ke')
            print('1. Desimal')
            print('2. Okta')
            print('3. Hexadecimal')
            print('4. ASCII')
            menu = int(input('masukan pilihan :'))
            print('')

            while menu > 5 or menu < 0:
                print('silahkan masukan angka yang ada pada menu.')
                menu = int(input('masukan pilihan : '))
                print('')

            if menu == 1:
                bin = input('masukan biner :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])  # membalikkan biner
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)
                print('hasilnya adalah : ', biner)
                print('')
            if menu == 2:
                bin = input('masukan biner :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)

                while biner != 0:
                    hasil = biner % 8
                    cetak.insert(0, str(hasil))
                    biner = biner//8
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')
            if menu == 3:
                bin = input('masukan biner :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

        elif masukan == 3:
            print('konvert ke')
            print('1. Desimal')
            print('2. Biner')
            print('3. Hexadecimal')
            print('4. ASCII')
            menu = int(input('masukan pilihan :'))
            print('')

            while menu > 5 or menu < 0:
                print('silahkan masukan angka yang ada pada menu.')
                menu = int(input('masukan pilihan : '))
                print('')

            if menu == 1:
                bin = input('masukan okta :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(8**i)
                print('hasilnya adalah : ', biner)
                print('')

            if menu == 2:
                bin = input('masukan okta :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 2
                    cetak.insert(0, str(hasil))
                    biner = biner//2
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

            if menu == 3:
                bin = input('masukan okta :')
                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(8**i)

                while biner != 0:
                    hasil = biner % 16
                    if hasil == 10:
                        hasil = 'A'
                    if hasil == 11:
                        hasil = 'B'
                    if hasil == 12:
                        hasil = 'C'
                    if hasil == 13:
                        hasil = 'D'
                    if hasil == 14:
                        hasil = 'E'
                    if hasil == 15:
                        hasil = 'F'
                    cetak.insert(0, str(hasil))
                    biner = biner//16
                    if biner == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

        elif masukan == 4:
            print('konvert ke')
            print('1. Desimal')
            print('2. Biner')
            print('3. Okta')
            print('4. ASCII')
            menu = int(input('masukan pilihan :'))
            print('')

            while menu > 5 or menu < 0:
                print('silahkan masukan angka yang ada pada menu.')
                menu = int(input('masukan pilihan : '))
                print('')

            if menu == 1:
                bin = input('masukan hexa :')
                print('')
                for i in range(len(bin)):
                    if bin[i] == 'A' or bin[i] == 'a':
                        hasil = 10
                    if bin[i] == 'B' or bin[i] == 'b':
                        hasil = 11
                    if bin[i] == 'C' or bin[i] == 'c':
                        hasil = 12
                    if bin[i] == 'D' or bin[i] == 'd':
                        hasil = 13
                    if bin[i] == 'E' or bin[i] == 'e':
                        hasil = 14
                    if bin[i] == 'F' or bin[i] == 'f':
                        hasil = 15
                    hexa += hasil*(16**i)
                print('hasilnya adalah : ', hexa)
                print('')

            if menu == 2:
                bin = input('masukan hexa :')

                for i in range(len(bin)):
                    if bin[i] != 'a' or bin[i] != 'b' or bin[i] != 'c' or bin[i] != 'd' or bin[i] != 'e' or bin[i] != 'f':
                        a = False;
                    else:
                        a = True

                while a == False:
                    for i in range(len(input)):
                        if input[i] != 'a' or input[i] != 'b' or input[i] != 'c' or input[i] != 'd' or input[i] != 'e' or input[i] != 'f':
                            a = False;
                            break
                        else:
                            a = True

                print('')
                for i in range(len(bin)):
                    pembalik.insert(0, bin[i])  # membalikkan biner
                for i in range(len(pembalik)):
                    biner += int(pembalik[i])*(2**i)

                for i in range(len(bin)):
                    if bin[i] == 'A':
                        hasil = 10
                    if bin[i] == 'B':
                        hasil = 11
                    if bin[i] == 'C':
                        hasil = 12
                    if bin[i] == 'D':
                        hasil = 13
                    if bin[i] == 'E':
                        hasil = 14
                    if bin[i] == 'F':
                        hasil = 15
                    hexa += hasil*(16**i)

                while hexa != 0:
                    hasil = hexa % 2
                    cetak.insert(0, str(hasil))
                    hexa = hexa//2
                    if hexa == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

            if menu == 3:
                bin = input('masukan hexa :')
                print('')
                for i in range(len(bin)):
                    if bin[i] == 'A':
                        hasil = 10
                    if bin[i] == 'B':
                        hasil = 11
                    if bin[i] == 'C':
                        hasil = 12
                    if bin[i] == 'D':
                        hasil = 13
                    if bin[i] == 'E':
                        hasil = 14
                    if bin[i] == 'F':
                        hasil = 15
                    hexa += hasil*(16**i)

                while hexa != 0:
                    hasil = hexa % 8
                    cetak.insert(0, str(hasil))
                    hexa = hexa//8
                    if hexa == 0:
                        for i in range(len(cetak)):
                            tampil += cetak[i]
                print('hasilnya adalah : ', tampil)
                print('')

            
                
        print('Konversi dari :')
        print ('1. Desimal')
        print ('2. Biner')
        print('3. Okta')
        print ('4. Hexadecimal')
        print ('5. ASCII')
        print ('0. exit')
        masukan = int (input('masukan pilihan : '))
        print ('')

        
except :
    print ('anda memasukan inputan yang salah. dan maaf program terhenti')