huruf = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def enkripsi(kalimat, cipher_key):
    kalimat = kalimat.lower()
    hasil_enkripsi = ""
    for karakter in kalimat:
        if karakter in huruf:
            index_lama = huruf.index(karakter)
            index_baru = (index_lama + cipher_key) % len(huruf)
            abjad_baru = huruf[index_baru]
            hasil_enkripsi = hasil_enkripsi + abjad_baru
        else:
            hasil_enkripsi = hasil_enkripsi + " "
    return hasil_enkripsi


def dekripsi(kalimat, cipher_key):
    kalimat = kalimat.lower()
    hasil_enkripsi = ""
    for karakter in kalimat:
        if karakter in huruf:
            index_lama = huruf.index(karakter)
            index_baru = abs((index_lama - cipher_key) % len(huruf))
            abjad_baru = huruf[index_baru]
            hasil_enkripsi = hasil_enkripsi + abjad_baru
        else:
            hasil_enkripsi = hasil_enkripsi + " "
    return hasil_enkripsi


pilihan = int(input("Pilih aksi yang akan dilakukan ( 1 = Enkripsi, 2 = Dekripsi): "))

if pilihan == 1:
    kalimat = input("Masukkan kalimat yang ingin dienkripsi: ")
    key = int(input("Masukkan cipher key yang anda inginkan (dalam angka, misal 9): "))
    kalimat_hasil = enkripsi(kalimat, key)
    print("Kalimat yang dimasukkan adalah:", kalimat)
    print(
        "Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key:",
        key,
        "adalah",
        kalimat_hasil,
    )
elif pilihan == 2:
    kalimat = input("Masukkan kalimat yang ingin didekripsi: ")
    key = int(input("Masukkan cipher key yang anda inginkan (dalam angka, misal 9): "))
    kalimat_hasil = dekripsi(kalimat, key)
    print("Kalimat yang dimasukkan adalah:", kalimat)
    print(
        "Hasil Dekripsi kalimat menggunakan Caesar Cipher dengan key:",
        key,
        "adalah",
        kalimat_hasil,
    )
