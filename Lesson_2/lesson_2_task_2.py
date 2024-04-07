year_as_str=input("Ввведите год")
year = int(year_as_str)

if year%4==1:
        is_year_leap=False
else:
    is_year_leap=True

print("год :",year,is_year_leap)