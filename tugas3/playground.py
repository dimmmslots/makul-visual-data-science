# siswa = ['adi',"budi","caca"]
# search = input("Masukkan nama siswa: ")
# found = search in siswa
# if found:
#     print("ada")
# else:
#     print("tidak ada")

# text = "Lorem ipsum dolor sit amet".replace(" ", "").lower()
# print(text)

mahasiswa = {
    "0074" : 'dimas',
    '0044' : 'fajar',
    '0104' : 'febi'
}

nim = input("Masukkan NIM: ")
if nim in mahasiswa:
    print(mahasiswa[nim])
else:
    print("Mahasiswa dengan nim tersebut tidak ada")