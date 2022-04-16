import imp
from random import randint 
import json
from store import Store

class Other:
    weather = 0
    days = 0
    month_list = ["Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
    month_limit = ["31","30","31","30","31","31","30","31","30","31"] 
    month = str
    C = 0
    temp_C = 0
    temp = 0

    with open('items.json', 'r', encoding = 'utf-8') as items:
            list = json.loads(items.read())
            
    def day_pass():
            Other.days +=1
            Other.weather()
            print(f"Дата: {Other.month_list[0]}, {Other.days}")

            if Other.days > int(Other.month_limit[0]):
                Other.month_limit.pop(0)
                Other.month_list.pop(0)
                Other.days = 0

    def set_temp():
        Other.temp_C = Other.C + Other.temp
        
    
    def weather():
        if len(Other.month_list)>=6:
            if len(Other.month_list)==9:
                Other.C = randint(-2,4)
            elif len(Other.month_list)==8:
                Other.C  = randint(6,10)
            elif len(Other.month_list)==7:
                Other.C  = randint(15,19)
            elif len(Other.month_list)==6:
                Other.C  = randint(19,30)
            elif len(Other.month_list)==5:
                Other.C  = randint(31,35)

            if int(Other.month_limit[0])/2 < Other.days:
                Other.C += 4

        elif len(Other.month_list)<=3:
            if len(Other.month_list)==4:
                Other.C  = randint(28,35)
            elif len(Other.month_list)==3:
                Other.C  = randint(14,22)
            elif len(Other.month_list)==2:
                Other.C  = randint(6,13)
            elif len(Other.month_list)==1:
                Other.C  = randint(-4,8)
            
            if int(Other.month_limit[0])/2 < Other.days:
                Other.C -= 4
                     
        print(f"температура сегодня: {Other.C}°C")
