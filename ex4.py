
from collections import OrderedDict

def Main():

	ValidNum = False
	While not ValidNum:
		Num0=int(input("Insert a valid integer number."))
		If (Num0 >0 and Num0 <1000000):
			ValidNum = True
		else :
			print("Try again")
	write_roman(Num0)
	

def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

def Main():
	ValidNum = False
	While not ValidNum:
		Num0=int(input("Insert a valid integer number."))
		If (Num0 >0 and Num0 <1000000):
			ValidNum = True
		else :
			print("Try again")
	write_roman(Num0)
	

Main()
