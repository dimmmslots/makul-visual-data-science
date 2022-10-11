# membuat header
import os
os.system("cls")
print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILITNG PERSEGI PANJANG':^40}")
print(f"{'_'*40:^40}")
# membuat input


def luas(panjang, lebar):
    return panjang * lebar


def keliling(panjang, lebar):
    return 2 * (panjang + lebar)


def main():
    os.system("cls")
    p = int(input("Masukkan panjang: "))
    l = int(input("Masukkan lebar: "))
    print(f"Luas = {luas(p, l)}")
    print(f"Keliling = {keliling(p, l)}")
    again = input("Hitung lagi? (y/n) ")
    if again == "y":
        main()
    else:
        print("Terima kasih")
        return False

main()