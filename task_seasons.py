month_number = input()
try:
    if month_number.isdigit():
        seasons = {
          (12, 1, 2)  : "winter" ,
          (3, 4, 5)   : "spring" ,
          (6, 7, 8)   : "summer" ,
          (9, 10, 11) : "autumn" ,
        }
        for key, value in seasons.items():
            for num in key:
               if int(num) == int(month_number):
                   answer = key
        print(seasons.setdefault(answer))     
except (ValueError, TypeError): 
    print('Введите число от 1 до 12')
