from calendar import c
import json
import random as r
import time
from store import Store
from other import Other

class Gr_garden:
    grow_days = 0
    work_days = 0
    drink_days = 0
    motivation = 10
    health = 10
    inventory = []
    harvest_start = False
    quality_coef = 0
    amount_harvest = 100

    def work():
        print(" \n Вы вышли на свой участок. Работы - непочатый край. \n Работая много дней подряд, не допускайте падения мотивации до нуля, иначе уйдёте в запой на какое-то время \n")
        while input("Вы хотите поработать на земле? (д/н): ").lower() == "д":
            if Gr_garden.motivation >=1:
                print("\n Очень жаль, а могли ведь пойти в погроммисты и зашибать 300кк далларов/нано-сек")        
                
                Gr_garden.work_days +=4
                Gr_garden.motivation -=0.5
                Gr_garden.drink_days -=1
                Other.day_pass()

                Store.money-=1000
                Gr_garden.health += 0.5

                if Store.seed_bought:
                    if Gr_garden.grow_days >=0:
                        Gr_garden.grow_days -=1
                        
                    elif Gr_garden.grow_days <=0:
                        Gr_garden.harvest_start = True
                        

                        
                
                print("вы проработали {} дней. Уровень мотивации: {}".format(Gr_garden.work_days, Gr_garden.motivation))
            
                if len(Store.items_to_use) >=1:
                    if Working.do_work(Working.list[str(Store.ask_answer)]['work_days']):
                        Gr_garden.inventory.append({Working.list[str(Store.ask_answer)]['name']})
                        print("вы завершили работы:", Gr_garden.inventory)
                        Done.motiv_up()
                        Working.get_coef()

                        if Store.garden_bought:
                            Other.temp += int(Other.list[str(Store.ask_answer)]['temp'])
                            print("Теперь температура воздуха равна", Other.temp, "°C")
                            Other.set_temp()

                        
                        if len(Store.items_to_use) >=1:
                            Store.items_to_use.remove({Working.list[str(Store.ask_answer)]['name']})
                            Done.job_is_done(Done.list[str(Store.ask_answer)]['grow_days'])
                            

                if Store.seed_bought:
                    if len(Gr_garden.inventory) >= 1:
                        Gr_garden.grow_days -=1
                        Harvest.temperature_to_harvest()
                
                if Gr_garden.harvest_start:
                    Harvest.harvest_day()
                    Other.set_temp()
                    
            
            else:
                print("\n Не могу снова пахать, пропади оно пропадом! Да я жизни не вижу, от зари до зари с согнутой спиной! \n Я бы выпил сейчас....")
                break 
        

        

class Working:
        with open('items.json', 'r', encoding = 'utf-8') as items:
            list = json.loads(items.read())
            quality_coef = list[str(Store.ask_answer)]['quality']
            quantity = list[str(Store.ask_answer)]['contains']
        def do_work(days_cost):
            if Gr_garden.work_days >= days_cost:
                Gr_garden.work_days -= days_cost
                return True
            else:
                return False   
            
        def get_coef():
            with open('items.json', 'r', encoding = 'utf-8') as items:
                list = json.loads(items.read())
                quality_coef = list[str(Store.ask_answer)]['quality']
                Gr_garden.quality_coef+=quality_coef
                print("получен коэффициент урожайности {:.1f}".format(Gr_garden.quality_coef))



class Done():
    with open('items.json', 'r', encoding = 'utf-8') as items:
        list = json.loads(items.read())
    def job_is_done(grow_days):
        Gr_garden.grow_days += grow_days
    def motiv_up():
        Gr_garden.motivation += 1
        print("уровень мотивации повысился (+1)")


class Harvest:
    harvest_days = 0
    player_price = 0
    market_price = 150
    sell_coef = 0

    def get_harvest():
        Gr_garden.amount_harvest = Working.quantity*0.1*Working.quality_coef*0.1*Harvest.harvest_days
        print(f"Сегодня вы собрали {int(Gr_garden.amount_harvest)} килограмм урожая")
        Done.motiv_up()

    def harvest_day():
        Harvest.harvest_days +=1

        if Harvest.harvest_days%3 == 0:
            Harvest.get_harvest()

    def temperature_to_harvest():
            if Other.temp_C <=4:
                print(f"Растения погибли от критически низкой температуры: {Other.temp_C} °C. Впрочем, ещё можно успеть повторно закупить и высадить семена")
                Gr_garden.motivation = 0
                Gr_garden.harvest_start = False
                Store.seed_bought = False
            elif Other.temp_C >4 and Other.temp_C <=12:
                Gr_garden.quality_coef - 0.1
                Working.quantity - 300
            elif Other.temp_C >12 and Other.temp_C <=18:
                Working.quantity - 100
            elif Other.temp_C >18:
                Gr_garden.quality_coef +0.2


    def selling():
        Harvest.player_price = int(input("введите цену за килограмм, по которой вы собираетесь реализовать продукцию"))
        hours_on_market = 5
        comment = " часа осталось до конца торговли"

        customers = r.randint(150, 350)/r.randint(5,10)
        rich_customers = customers - 0.1*customers
        middle_customers = customers - 0.4*customers
        poor_customers = customers - (rich_customers+middle_customers)
        customers_buy = 0
        
        if Harvest.player_price > Harvest.market_price:
            customers = customers-poor_customers
            Harvest.sell_coef = (Harvest.player_price - Harvest.market_price)/10*0.2
            customers_buy = r.randint(1, 2)
        else:
            Harvest.sell_coef = (Harvest.market_price - Harvest.player_price)/10*0.5
            customers_buy = r.randint(1, 3)

        

        print(Harvest.sell_coef, "this is ur sell coef")
        print(customers, "that many people on market today")
        print(customers_buy, "thats how much kg they wanna buy")
        
        customers_per_hour = int(customers/hours_on_market)
        customers_buy = customers_buy*customers_per_hour

            

        for hours in range(hours_on_market,0,-1):
            if hours >1:
                customers_buy += r.randint(-1,2)
                Gr_garden.amount_harvest -= customers_buy
                print(Gr_garden.amount_harvest, "кто-то купил")
                print(str(hours), comment)
                time.sleep(5)
            else:
                print("остался последний час торговли на рынке!")
                if Gr_garden.amount_harvest > 0:
                    if input("желаете ли снизить цену? (д/н)").lower == "д":
                        Harvest.player_price = int(input("введите цену за килограмм, по которой вы собираетесь реализовать продукцию"))
        print("Вам пора ехать на участок, на сегодня торговля окончена!")
