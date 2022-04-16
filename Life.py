
from store import Store
from working import Gr_garden
from other import Other
import random as r
class Life:

    def drink():
        
        while input("Хотите выпить?(д/н)").lower() == "д":
                print("\n *звук открывающейся бутылки*\n Уууух, холодненькая! \n")
                if Gr_garden.health <= 0:
                        break 
                Store.money -= 500
                Other.day_pass()
                Gr_garden.drink_days +=1
                Gr_garden.motivation +=1

                print("Идёт {} день запоя. Уровень мотивации: {}".format(Gr_garden.drink_days, Gr_garden.motivation))

                if Gr_garden.drink_days >=2:
                    Gr_garden.health -= 1
                if Gr_garden.drink_days ==4:
                    print("Бррр, мне плохо... Ну, с закусочкой должно же получше зайти, а?")
        
                if Gr_garden.drink_days == 5:
                    Other.days += r.randint(3,14)
                    Store.money -= r.randint(2000,25000)
                    Gr_garden.health -=2
                    print("Выписали из инфекционки... Клянусь, больше никогда не буду пить...'А сколько дней прошло? Так, надо проверить деньги!'")  
                    break
                if Gr_garden.drink_days >10:
                    Gr_garden.health -= 10
                