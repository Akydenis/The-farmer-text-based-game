
from store import Store
from working import Gr_garden, Harvest, Working
from Life import Life
from other import Other
import random as r

class Game:
    print("приветствие")
    def main_menu(self):
            print("К чему хотите приступить? \n 0 - просмотреть статистику и инвентарь \n 1 - отправиться на закупку материалов \n 2 - приступить к работе \n 3 - выпить алкоголь \n 4 - бездельничать \n 5 - отправиться на рынок")
            ask_answer = input("Выберите цифру, соответствующую желаемому действию: \n ")
            if ask_answer == "1":
                Store.shop()
            elif ask_answer == "2":
                Gr_garden.work()
            elif ask_answer == "3":
                Life.drink()
            elif ask_answer == "4":
                Other.day_pass()
            elif ask_answer == "5":
                if Gr_garden.amount_harvest <=0:
                    print("Вам пока нечем торговать. А пропитые почки и за дёшево никому не нужны!")
                else:
                    Harvest.selling()
            elif ask_answer == "0":
                Game.ShowParameters()
            else:
                print(" \n ============== \n Некорректный выбор, попробуйте ещё раз \n ============== \n")



    def ShowParameters():
        print(Gr_garden.inventory, Gr_garden.health,"здоровья и ", Gr_garden.motivation," мотивации при запасе денег: ",  Store.money)
        print(Gr_garden.drink_days,"дней в запое. ", Other.days, "дней прошло.", Gr_garden.grow_days, "дней до первого урожая.", "Температура в теплице ", Other.temp_C,"°C")
        
  

if __name__ == '__main__':
    while True:
        game = Game()
        game.main_menu()
        if Gr_garden.health <=0:
            print("Алкоголизм погубил вас и ваши старания!")
            break
        if Gr_garden.health >= 10:
                Gr_garden.health = 10
        if Gr_garden.drink_days <= 0:
                    Gr_garden.drink_days = 0

        
                
            

        


      
