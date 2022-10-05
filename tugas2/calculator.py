# minta inputan angka pertama dari user
st_number = input("Enter a number: ")

# minta inputan operator dari user
st_operator = input("Enter an operator: ")

# minta inputan angka kedua dari user
st_number2 = input("Enter another number: ")

# konversi inputan user dari string ke integer
number = int(st_number)
number2 = int(st_number2)
result = 0

# cek operator yang dimasukkan user
if st_operator == "+" : result = number + number2
elif st_operator == "-" : result = number - number2
elif st_operator == "*" : result = number * number2
elif st_operator == "/" : result = number / number2
elif st_operator == "%" : result = number % number2
else : print("Invalid operator")

# print hasil
print(f"{number} {st_operator} {number2} = {result}")