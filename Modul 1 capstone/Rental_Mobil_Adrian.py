listPenyewa = [
    {
      'Nama' : 'Carl Johnson',
      'Merek Mobil' : 'Toyota',
      'Tipe Mobil' : 'Yaris',
      'Durasi Peminjaman' : 1
    },
    {
        'Nama' : 'Big Smoke',
        'Merek Mobil' : 'Toyota',
        'Tipe Mobil' : 'Avanza',
        'Durasi Peminjaman' : 5
    },
    {
        'Nama' : 'Wu Zi Mu',
        'Merek Mobil' : 'Honda',
        'Tipe Mobil' : 'Jazz',
        'Durasi Peminjaman' : 2
    },
    {
        'Nama' : 'Eddie Pulaski',
        'Merek Mobil' : 'Honda',
        'Tipe Mobil' : 'City',
        'Durasi Peminjaman' : 1
    }
]

# Menampilkan daftar seluruh penyewa mobil
def tampilkanPenyewa():
    print('Daftar Penyewa\n')
    print('Index\t| Nama            \t| Merek Mobil \t| Tipe Mobil  \t| Durasi Peminjaman (Hari)')
    for i in range(len(listPenyewa)):
        print('{}\t| {}      \t| {}  \t| {}  \t| {}'.format(i, listPenyewa[i]['Nama'], listPenyewa[i]['Merek Mobil'], listPenyewa[i]['Tipe Mobil'], listPenyewa[i]['Durasi Peminjaman']))

# Fungsi untuk menambahkan penyewa baru ke dalam dictionary
def addPenyewa():
    while True:
        print('Note: Case sensitive!')
        namaSewa = input('Masukkan Nama Penyewa: ')    
        cari = False # untuk melakukan pencarian
        for i in listPenyewa: # For loop digunakan agar bisa menampilkan notifikasi bahwa input yang dimasukkan ternyata sudah ada nantinya
            if i['Nama'] == namaSewa:
                cari = True
                break
        
        if not cari:
            merekMobil = input('Masukkan Merek Mobil: ')
            tipeMobil = input('Masukkan Tipe Mobil: ')
            durasi = int(input('Masukkan Durasi Sewa (per Hari): '))
            konfirmasi = input('Apakah anda ingin menyimpan data? (ya/tidak): ')
            if konfirmasi == 'ya':
                listPenyewa.append({
                'Nama': namaSewa,
                'Merek Mobil': merekMobil,
                'Tipe Mobil': tipeMobil,
                'Durasi Peminjaman': durasi
                })
                tampilkanPenyewa()
                print('Penyewa berhasil ditambahkan')
                break
            elif(konfirmasi == 'tidak'):
                print('Penyimpanan data dibatalkan')
                break
            else:
                print('Input yang anda masukkan salah')
        else:
            print('Penyewa sudah ada')
            break
        
def pencarian():
    print('Note: Case Sensitive!')
    user_input = input('Masukkan Nama Penyewa: ')
    for i in listPenyewa:
        if i['Nama'] == user_input:
            print('Nama: {}, Merek Mobil: {}, Tipe Mobil: {}, Durasi Peminjaman {}'.format(i['Nama'], i['Merek Mobil'], i['Tipe Mobil'], i['Durasi Peminjaman']))
            break
    else:
        print('Nama tidak ditemukan')

def hapusPenyewa():
    while True:
        tampilkanPenyewa()
        penyewa = int(input('Masukkan indeks penyewa yang ingin dihapus: '))
        if penyewa >= len(listPenyewa):
            print('Indeks yang anda masukkan belum ada')
            break
        else:
            konfirmasi1 = input('Apakah anda yakin ingin menghapus data tersebut? (ya/tidak): ')
            if(konfirmasi1 == 'ya'):
                listPenyewa.pop(penyewa)
                print('Data dihapus')
                break
            elif(konfirmasi1 == 'tidak'):
                print('Penghapusan data dibatalkan')
                break
            else:
                print('Input yang anda masukkan salah')


def updateData():
    print('Note: Case Sensitive!')
    namaUpdate = input('Masukkan Nama: ')
    cari = False

    for i in listPenyewa:
        if i['Nama'] == namaUpdate:
            cari = True
            print(f'Data yang akan di update: {i}')
            konfirmasi2 = input('Apakah anda ingin mengganti data? (ya/tidak): ') # konfirmasi pertama
            if(konfirmasi2 == 'ya'):
                key = input('Masukkan key yang ingin diubah: ') # variabel ini di taruh disini dikarenakan jika ditaruh di bawah func, maka print data yg akan di updt akan muncul pada saat funct selesai (tidak sesuai dengan flowchart)
                value = input('Masukkan nilai baru: ')
                # i[key] = value
                konfirmasi3 = input('Lanjutkan update data? (ya/tidak): ') # konfirmasi kedua setelah memasukkan user input kolom yg akan di update
                if(konfirmasi3 == 'ya'):
                    i[key] = value # di sini input key yang dimasukkan, valuenya akan diganti dengan value yg baru
                    print('Update data berhasil')
                elif(konfirmasi3 == 'tidak'):
                    print('Update dibatalkan')
                    break
                else:
                    print('Input yang anda masukkan salah')
            elif(konfirmasi2 == 'tidak'):
                print('Update data dibatalkan')
                break
            else:
                print('Input yang anda masukkan salah')
    if cari == False: # Di sini, jika kondisi dari cari tidak berubah menjadi true, atau berarti 'Nama' yang dimasukkan tidak ada maka akan di tampilkan notid 'data tidak ada'
        print('Data tidak ada')
        
def pilihanRead():
    while True:
        menuDaftar = input('''
        Menu Daftar Mobil:
        1. Tampilkan Daftar Penyewa
        2. Cari Penyewa
        3. Kembali ke Menu Utama

        Masukkan angka Menu:
        ''')

        if(menuDaftar == '1'):
            tampilkanPenyewa() 
        elif(menuDaftar == '2'):
            pencarian()
        elif(menuDaftar == '3'):
            print(menuUtama)
            break
        elif(menuDaftar > '3'):
            print('Input yang Anda masukkan salah')

def pilihanTambah():
    while True:
        menuTambah = input('''
        Menu Tambahkan Penyewa:
        1. Tambahkan Penyewa
        2. Kembali ke Menu Utama

        Masukkan angka menu:
        ''')

        if(menuTambah == '1'):
            addPenyewa()
        elif(menuTambah == '2'):
            print(menuUtama)
            break
        elif(menuTambah > '2'):
            print('Menu yang anda masukkan salah')

def pilihanUpdate():
    while True:
        menuUpdate = input('''
        Menu Update Data
        1. Update/Ubah Data
        2. Kembali ke Menu Utama

        Masukkan angka menu:
        ''')

        if(menuUpdate == '1'):
            updateData()
        elif(menuUpdate == '2'):
            print(menuUtama)
            break
        else:
            print('Menu yang anda masukkan salah')

def pilihanDel():
    while True:
        menuDel = input('''
        Menu Hapus Data:
        1. Hapus Data
        2. Kembali ke Menu Utama

        Masukkan angka menu: 
        ''')

        if(menuDel == '1'):
            hapusPenyewa()
        elif(menuDel == '2'):
            print(menuUtama)
            break
        else:
            print('Menu yang anda masukkan salah')

while True:
    menuUtama = input('''
    Selamat Datang di Adrian Rental

        Menu Utama:
        1. Tampilkan Daftar Penyewa
        2. Tambahkan Penyewa
        3. Update Data Penyewa
        4. Hapus Penyewa
        5. Keluar

        Masukkan angka Menu: 
        ''')
    
    if(menuUtama == '1'):
        pilihanRead()
    elif(menuUtama == '2'):
        pilihanTambah()
    elif(menuUtama == '3'):
        pilihanUpdate()
    elif(menuUtama == '4'):
        pilihanDel()
    elif(menuUtama == '5'):
        break
    else:
        print('Menu yang anda masukkan salah')

