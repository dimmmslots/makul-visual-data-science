index = 0
rak_buku = []
while True:
    print('Input Data Buku')
    judul = input('Judul buku :')
    pengarang = input('Nama Pengarang :')
    tahun = input('Tahun Terbit :')
    buku = [judul, pengarang, tahun]
    jawab=input('ketik data lagi = ? (y/n)')
    if jawab=="n":
        break
    rak_buku.insert(index, buku)
    index += 1
    # print all data and its index
    for i in range(len(rak_buku)):
        print(i+1, rak_buku[i])