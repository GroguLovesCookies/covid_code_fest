import math


final_year = 4056
final_month = 2
final_date = 18
digits_of_year = int(str(final_year)[2:5])
century = 40
days = {0:"Monday", 1:"Tueseday", 2:"Wedneseday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
month_codes = {0: 0, 1: 3, 2: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 5, 9: 0, 10: 3, 11: 5}
century_code = (18-century)%7
year_code = (digits_of_year+(digits_of_year-(digits_of_year%4))//4)%7
leap_year_code = 1 if final_year/4 == final_year//4 else 0
day = days[(year_code+month_codes[final_month]+final_date-leap_year_code)%7]
print(day)

