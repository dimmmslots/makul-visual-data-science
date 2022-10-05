degree = input("masukkan derajat = ")

while not degree.isdigit():
    degree = input("masukkan derajat = ")
degree = int(degree)

scale = ""

# check if scale string length is greater than 0 and scale is string
while len(scale) > 0 and scale.isalpha():
    scale = scale.lower()

while(scale != "c" and scale != "f" and scale != "k" and scale != "r"):
    scale = input("Masukkan skala (C/F/K/R) = ")
    
if scale == "c":
    print(f"{degree} Celcius = {degree*1.8+32} Fahrenheit")
    print(f"{degree} Celcius = {degree+273.15} Kelvin")
    print(f"{degree} Celcius = {degree*0.8} Reamur")
elif scale == "f":
    print(f"{degree} Fahrenheit = {(degree-32)/1.8} Celcius")
    print(f"{degree} Fahrenheit = {(degree-32)/1.8+273.15} Kelvin")
    print(f"{degree} Fahrenheit = {(degree-32)/2.25} Reamur")
elif scale == "k":
    print(f"{degree} Kelvin = {degree-273.15} Celcius")
    print(f"{degree} Kelvin = {(degree-273.15)*1.8+32} Fahrenheit")
    print(f"{degree} Kelvin = {(degree-273.15)*0.8} Reamur")
elif scale == "r":
    print(f"{degree} Reamur = {degree*1.25} Celcius")
    print(f"{degree} Reamur = {degree*2.25+32} Fahrenheit")
    print(f"{degree} Reamur = {degree*1.25+273.15} Kelvin")

